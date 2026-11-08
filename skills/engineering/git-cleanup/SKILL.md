---
name: git-cleanup
description: Clean finished local Git branches and worktrees with a preview and approved apply. Use for merged branches, abandoned empty branches, and stale worktree registrations.
metadata:
  preferred-model: haiku
---
# Git cleanup

Use the script for Git checks and deletion; use the model to review uncertain work. Start with a small-model subagent (Haiku preferred) when the host supports it, and relay its findings to the user. Escalate unresolved comparisons to an available stronger model; otherwise ask the user. The metadata is a preference; model selection belongs to the host runner and is not enforced by this skill.

## Preview

1. Confirm the target repository from the user's request or current directory. Use one repository by default. Use `--root <folder>` only for an explicitly requested folder sweep; discovery stops after four levels and skips nested repositories.
2. Run `uv run <skill-dir>/scripts/git_cleanup.py --repo <repo>`. Requires Git, Python 3, and uv. The script fetches and prunes remote-tracking refs, but leaves remote branches on the server unchanged. Use `--base <ref>` when the detected integration branch differs from the project's workflow. Add `--min-age <days>` to change the seven-day grace period for newly created empty branches.
3. Review uncertain items using [model review](references/model-review.md). Give KEEP, REMOVE recommendation, or ASK for each reviewed item, with evidence. The model may recommend keeping a script candidate too; if so, pause apply, since the script applies its whole REMOVE list.
4. For branches recommended for abandonment, preview again with a separate `--discard <branch>` for each exact name. This can include unique work, but retains worktree blockers and protected branches. Show the exact REMOVE list, unique-work warnings, reasons, KEEP blockers, PRUNE count, base, and plan ID in plain English. Ask approval for that concrete plan, explicitly naming unmerged work to discard. If the user already approved that exact unchanged plan, continue.

Done when the user can identify every proposed removal. Keep uncertain work. A missing upstream alone is not merge evidence. Protected integration/release branches are excluded. Squash/rebase evidence uses patch equivalence; squash lookup is bounded to the last 1,000 base commits.

## Apply

After approval, repeat the same command and options with `--apply <plan-id>`. The script fetches again, compares the plan including commit tips, and checks each candidate again before removal. A changed plan needs a new preview and approval. Report partial failures; preserve failed worktrees and their branches.

Worktree removal uses Git without force. Primary/current, locked, dirty, ignored-file, and operation-in-progress worktrees are retained. Clean worktrees can still belong to running agents: have the user stop those sessions before approving removal. Avoid concurrent Git edits during apply; the checks do not provide a repository-wide lock.

Done when the script reports its result and you summarize removals and blockers. Use only the script's approved operations; leave arbitrary sibling directories, remote branches, stashes, and object databases alone.

For implementation checks, run `uv run <skill-dir>/scripts/test_git_cleanup.py`; it creates disposable repositories, never cleans the user's repositories. See [design sources](references/design-sources.md) for the comparison behind this implementation.
