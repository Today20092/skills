#!/usr/bin/env python3
"""Preview or apply a git cleanup of finished local branches and worktrees.

Preview (default) prints a plan with a plan id. `--apply <id>` re-derives the plan
and deletes only when the id still matches. Stdlib only; git runs without a shell.
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time

PROTECTED = {
    "main",
    "master",
    "trunk",
    "develop",
    "dev",
    "staging",
    "production",
    "qa",
    "uat",
}
PROTECTED_PREFIXES = ("release/", "hotfix/")


def git(repo, *args, stdin=None):
    return subprocess.run(
        ["git", "-C", repo, *args],
        input=stdin,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def out(repo, *args):
    p = git(repo, *args)
    if p.returncode:
        raise RuntimeError(p.stderr.strip() or f"git {args[0]} failed")
    return p.stdout.strip()


def norm(path):
    return os.path.normcase(os.path.realpath(path)) if path else ""


def find_repos(root):
    root = os.path.abspath(root)
    for d, dirs, _ in os.walk(root):
        if ".git" in dirs:
            yield d
            dirs[:] = []
        elif d.count(os.sep) - root.count(os.sep) >= 4:
            dirs[:] = []
        else:
            dirs[:] = [x for x in dirs if x != "node_modules"]


def find_base(repo, override):
    if override:
        return override
    candidates = [
        git(repo, "symbolic-ref", "--short", "refs/remotes/origin/HEAD").stdout.strip(),
        "origin/main",
        "origin/master",
        "main",
        "master",
    ]
    for ref in candidates:
        if (
            ref
            and git(
                repo, "rev-parse", "--verify", "--quiet", ref + "^{commit}"
            ).returncode
            == 0
        ):
            return ref
    return None


def worktrees(repo):
    found, cur = [], None
    for line in out(repo, "worktree", "list", "--porcelain", "-z").split("\0") + [""]:
        if not line:
            if cur:
                found.append(cur)
            cur = None
            continue
        key, _, value = line.partition(" ")
        if key == "worktree":
            cur = {"path": value}
        elif cur is not None:
            cur[key] = value
    return found


def evidence(repo, base, tip, branch):
    """Return (is_merged, reason). Merged means the work is already in `base`."""
    if git(repo, "merge-base", "--is-ancestor", tip, base).returncode == 0:
        return True, f"merged: tip is in {base}"
    base_tree = out(repo, "rev-parse", f"{base}^{{tree}}")
    if out(repo, "rev-parse", f"{tip}^{{tree}}") == base_tree:
        return True, f"same files: tip tree equals {base}"
    mb = git(repo, "merge-base", base, tip).stdout.strip()
    if mb:
        cherry = out(repo, "cherry", base, tip).splitlines()
        if cherry and all(line.startswith("-") for line in cherry):
            return (
                True,
                f"rebase-merged: {len(cherry)} commits patch-equivalent in {base}",
            )
        # Exit 0 = clean merge, 1 = conflict, other = error or Git older than 2.38.
        sim = git(repo, "merge-tree", "--write-tree", base, tip)
        if sim.returncode == 0 and sim.stdout.split()[:1] == [base_tree]:
            return True, f"merge adds nothing: merging into {base} changes no files"
        diff = out(repo, "diff", "--no-ext-diff", "--no-textconv", mb, tip)
        if diff.strip():
            pid = git(repo, "patch-id", "--stable", stdin=diff).stdout.split()[:1]
            log = out(
                repo,
                "log",
                "--no-ext-diff",
                "--no-textconv",
                "-p",
                "--no-merges",
                "-n",
                "1000",
                f"{mb}..{base}",
            )
            seen = {
                line.split()[0]
                for line in git(
                    repo, "patch-id", "--stable", stdin=log
                ).stdout.splitlines()
            }
            if pid and pid[0] in seen:
                return True, f"squash-merged: branch diff matches one commit in {base}"
    return False, ""


def is_new_empty(repo, branch, min_age):
    """True for a branch created recently that never held a commit."""
    log = out(
        repo,
        "reflog",
        "show",
        "--date=unix",
        "--format=%gd\t%gs",
        f"refs/heads/{branch}",
    ).splitlines()
    if len(log) != 1 or "Created from" not in log[0]:
        return False
    created = int(log[0].split("\t")[0].rsplit("@{", 1)[1].rstrip("}"))
    return time.time() - created < min_age * 86400


def worktree_blocker(wt, primary, here):
    path = wt["path"]
    if norm(path) in (norm(primary), here):
        return "checked out in the primary or current worktree"
    if "locked" in wt:
        return "worktree is locked"
    if "prunable" in wt or not os.path.isdir(path):
        return "missing worktree; review its registration separately"
    if out(path, "status", "--porcelain", "--untracked-files=all", "--ignored"):
        return "worktree has changes, untracked files, or ignored files"
    for marker in (
        "MERGE_HEAD",
        "CHERRY_PICK_HEAD",
        "REVERT_HEAD",
        "rebase-merge",
        "rebase-apply",
        "sequencer",
    ):
        if os.path.exists(
            out(path, "rev-parse", "--path-format=absolute", "--git-path", marker)
        ):
            return "worktree has an operation in progress"
    return None


def classify(repo, base, min_age, discard=()):
    wts = worktrees(repo)
    primary = wts[0]["path"] if wts else repo
    here = norm(git(os.getcwd(), "rev-parse", "--show-toplevel").stdout.strip())
    by_branch = {wt["branch"]: wt for wt in wts if "branch" in wt}
    rows = []

    def add(kind, label, reason, cmds=()):
        rows.append(
            {
                "kind": kind,
                "label": label,
                "reason": reason,
                "cmds": [list(c) for c in cmds],
            }
        )

    fmt = "%(refname:short)\t%(objectname)\t%(upstream:track)"
    for line in out(repo, "for-each-ref", f"--format={fmt}", "refs/heads").splitlines():
        branch, tip, track = (
            line.split("\t") if line.count("\t") == 2 else (*line.split("\t"), "")
        )
        if (
            branch in PROTECTED
            or branch.startswith(PROTECTED_PREFIXES)
            or base.endswith("/" + branch)
            or base == branch
        ):
            continue
        wt = by_branch.get("refs/heads/" + branch)
        label = f"branch {branch}" + (f" + worktree {wt['path']}" if wt else "")
        blocker = worktree_blocker(wt, primary, here) if wt else None
        if blocker:
            add("keep", label, blocker)
            continue
        merged, reason = evidence(repo, base, tip, branch)
        if branch in discard:
            merged, reason = True, "discard requested: may contain unique work"
        if (
            merged
            and reason.startswith("merged")
            and track != "[gone]"
            and is_new_empty(repo, branch, min_age)
        ):
            add("keep", label, f"new empty branch (younger than {min_age} days)")
        elif merged:
            cmds = [["branch", "-D", branch]]
            if wt and "prunable" not in wt:
                cmds.insert(0, ["worktree", "remove", wt["path"]])
            add("remove", label, reason, cmds)
            rows[-1]["tip"] = tip
        elif reason:
            add("keep", label, reason)
        else:
            ahead = out(repo, "rev-list", "--count", f"{base}..{tip}")
            add(
                "keep",
                label,
                (
                    "review: remote gone, no merge evidence; "
                    if track == "[gone]"
                    else ""
                )
                + f"{ahead} commits not in {base}",
            )

    for wt in wts[1:]:
        if "branch" in wt:
            continue
        label = f"detached worktree {wt['path']}"
        blocker = worktree_blocker(wt, primary, here)
        if blocker:
            add("keep", label, blocker)
        elif evidence(repo, base, wt["HEAD"], None)[0]:
            add(
                "remove",
                label,
                f"merged: HEAD is in {base}",
                [["worktree", "remove", wt["path"]]],
            )
            rows[-1]["tip"] = wt["HEAD"]
        else:
            add("keep", label, f"commits not in {base}")
    return rows


def fetch(repo):
    if not out(repo, "remote"):
        return True
    return git(repo, "fetch", "--prune").returncode == 0


def plan_id(results):
    lines = sorted(
        json.dumps([repo, base, r], sort_keys=True)
        for repo, base, rows, _ in results
        for r in rows
        if r["kind"] == "remove"
    )
    return hashlib.sha1("\n".join(lines).encode()).hexdigest()[:8]


def build(repos, args):
    results, fetched = [], True
    for repo in repos:
        fetched &= fetch(repo)
        base = find_base(repo, args.base)
        if not base:
            sys.exit(f"{repo}: no base branch found; pass --base <ref>")
        stale = len(
            [
                x
                for x in out(repo, "worktree", "prune", "--dry-run", "-v").splitlines()
                if x
            ]
        )
        results.append(
            (
                repo,
                out(repo, "rev-parse", base),
                classify(repo, base, args.min_age, args.discard),
                stale,
            )
        )
    return results, fetched


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "--repo", default=".", help="repo to clean (default: current directory)"
    )
    ap.add_argument("--root", help="clean every repo found under this folder instead")
    ap.add_argument("--base", help="base ref override, e.g. origin/main")
    ap.add_argument(
        "--discard",
        action="append",
        default=[],
        metavar="BRANCH",
        help="include a named branch even without merge evidence; preview and approval required",
    )
    ap.add_argument(
        "--min-age",
        type=int,
        default=7,
        help="days before an empty branch counts as finished",
    )
    ap.add_argument(
        "--apply", metavar="PLAN_ID", help="delete what the previewed plan listed"
    )
    args = ap.parse_args()
    if args.discard and args.root:
        ap.error("--discard requires a single --repo, not a folder sweep")

    repos = (
        list(find_repos(args.root))
        if args.root
        else [out(args.repo, "rev-parse", "--show-toplevel")]
    )
    if not all(repos):
        sys.exit("not a git repository")
    for branch in args.discard:
        if git(
            repos[0], "show-ref", "--verify", "--quiet", f"refs/heads/{branch}"
        ).returncode:
            ap.error(f"unknown local branch: {branch}")
    results, fetched = build(repos, args)
    pid = plan_id(results)

    if not args.apply:
        print(
            f"GIT CLEANUP plan={pid}"
            + ("" if fetched else "  WARNING: fetch failed, refs may be stale")
        )
        for repo, base, rows, stale in results:
            print(f"\nrepo {repo}  base {base}")
            for kind in ("remove", "keep"):
                for r in rows:
                    if r["kind"] == kind:
                        print(f"  {kind.upper():6} {r['label']} -- {r['reason']}")
            if stale:
                print(f"  PRUNE  {stale} worktree registrations whose folder is gone")
        return
    if not fetched:
        sys.exit("fetch failed; refusing to apply on stale refs")
    if args.apply != pid:
        sys.exit(f"plan changed since preview (now {pid}); preview again")
    failed = False
    for repo, base_tip, rows, _ in results:
        for r in (r for r in rows if r["kind"] == "remove"):
            current, fresh = build([repo], args)
            if not fresh or current[0][1] != base_tip or r not in current[0][2]:
                sys.exit("candidate changed; preview again")
            for cmd in r["cmds"]:
                p = git(repo, *cmd)
                failed |= p.returncode != 0
                print(
                    ("OK    " if p.returncode == 0 else "FAILED")
                    + f" {repo}: git {' '.join(cmd)}"
                    + ("" if p.returncode == 0 else f" -- {p.stderr.strip()}")
                )
                if p.returncode:
                    break
        p = git(repo, "worktree", "prune")
        failed |= p.returncode != 0
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
