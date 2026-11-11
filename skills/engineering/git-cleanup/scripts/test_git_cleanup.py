#!/usr/bin/env python3
"""Self-check: build a scratch repo covering each branch case, then preview and apply."""

import os
import subprocess
import sys
import tempfile

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "git_cleanup.py")


def git(cwd, *args):
    subprocess.run(
        ["git", "-C", cwd, "-c", "user.name=t", "-c", "user.email=t@t", *args],
        check=True,
        capture_output=True,
    )


def commit(cwd, name):
    with open(os.path.join(cwd, name), "w") as f:
        f.write(name)
    git(cwd, "add", name)
    git(cwd, "commit", "-m", name)


def run(repo, *args):
    return subprocess.run(
        [sys.executable, SCRIPT, "--repo", repo, *args],
        capture_output=True,
        text=True,
        cwd=repo,
    )


with tempfile.TemporaryDirectory() as tmp:
    repo = os.path.join(tmp, "repo")
    os.mkdir(repo)
    git(repo, "init", "-b", "main")
    commit(repo, "base")
    for name in ("merged", "squash", "active", "dirty", "clean"):
        git(repo, "checkout", "-b", name, "main")
        commit(repo, name + "1")
        if name == "squash":
            commit(repo, name + "2")
        git(repo, "checkout", "main")
    for name in ("merged", "dirty", "clean"):
        git(repo, "merge", "--no-ff", name, "-m", "merge " + name)
    git(repo, "merge", "--squash", "squash")
    git(repo, "commit", "-m", "squash")
    # Squash edited during merge: patch-ids differ, so only the simulated merge proves it.
    git(repo, "checkout", "-b", "edited", "main")
    commit(repo, "edited1")
    git(repo, "checkout", "main")
    git(repo, "merge", "--squash", "edited")
    commit(repo, "edited-extra")
    # Same files as main but different commits: proven by tree equality.
    git(repo, "checkout", "-b", "sametree", "main")
    git(repo, "commit", "--allow-empty", "-m", "empty")
    git(repo, "checkout", "main")
    git(repo, "branch", "fresh")
    git(repo, "worktree", "add", os.path.join(tmp, "wt-dirty"), "dirty")
    git(repo, "worktree", "add", os.path.join(tmp, "wt-clean"), "clean")
    open(os.path.join(tmp, "wt-dirty", "scratch.txt"), "w").write("x")
    for name in ("ignored", "locked"):
        git(repo, "branch", name, "merged")
        path = os.path.join(tmp, "wt-" + name)
        git(repo, "worktree", "add", path, name)
        if name == "locked":
            git(repo, "worktree", "lock", path)
        else:
            exclude = subprocess.run(
                ["git", "-C", repo, "rev-parse", "--git-path", "info/exclude"],
                capture_output=True,
                text=True,
                check=True,
            ).stdout.strip()
            with open(os.path.join(repo, exclude), "a") as f:
                f.write("\nignored.bin\n")
            with open(os.path.join(path, "ignored.bin"), "w") as f:
                f.write("keep")

    preview = run(repo)
    print(preview.stdout)
    assert preview.returncode == 0, preview.stderr
    lines = preview.stdout.splitlines()

    def row(kind, name):
        return any(
            line.strip().startswith(kind) and f"branch {name}" in line for line in lines
        )

    for name in ("merged", "squash", "edited", "sametree", "clean"):
        assert row("REMOVE", name), name
    assert "merge adds nothing" in preview.stdout
    assert "same files" in preview.stdout
    for name in ("active", "dirty", "fresh", "ignored", "locked"):
        assert row("KEEP", name), name
    assert not any("branch main" in line for line in lines)

    plan = preview.stdout.split("plan=")[1].split()[0]
    assert run(repo, "--apply", "deadbeef").returncode != 0
    commit(repo, "base-advanced")
    assert run(repo, "--apply", plan).returncode != 0
    preview = run(repo)
    assert preview.returncode == 0, preview.stderr
    plan = preview.stdout.split("plan=")[1].split()[0]
    applied = run(repo, "--apply", plan)
    print(applied.stdout, applied.stderr)
    assert applied.returncode == 0
    left = subprocess.run(
        ["git", "-C", repo, "branch", "--format=%(refname:short)"],
        capture_output=True,
        text=True,
    ).stdout.split()
    assert sorted(left) == ["active", "dirty", "fresh", "ignored", "locked", "main"], (
        left
    )
    assert not os.path.exists(os.path.join(tmp, "wt-clean"))
    assert os.path.exists(os.path.join(tmp, "wt-dirty", "scratch.txt"))
    assert run(repo, "--discard", "missing-branch").returncode != 0
    options = [
        "--discard",
        "active",
        "--discard",
        "dirty",
        "--discard",
        "locked",
        "--discard",
        "main",
    ]
    preview = run(repo, *options)
    assert preview.returncode == 0, preview.stderr
    assert "REMOVE branch active -- discard requested" in preview.stdout
    assert "REMOVE branch dirty" not in preview.stdout
    assert "REMOVE branch locked" not in preview.stdout
    assert "REMOVE branch main" not in preview.stdout
    plan = preview.stdout.split("plan=")[1].split()[0]
    git(repo, "checkout", "active")
    commit(repo, "later-work")
    git(repo, "checkout", "main")
    assert run(repo, *options, "--apply", plan).returncode != 0
    preview = run(repo, *options)
    plan = preview.stdout.split("plan=")[1].split()[0]
    assert run(repo, *options, "--apply", plan).returncode == 0
    assert (
        subprocess.run(
            ["git", "-C", repo, "show-ref", "--verify", "refs/heads/active"],
            capture_output=True,
        ).returncode
        != 0
    )
print("ok")
