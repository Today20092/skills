---
name: git-cleanup
description: Automatically clean finished local Git branches and worktrees, with a concise findings report. Use for merged work, old empty branches, and stale worktree registrations; review uncertain work with the model.
---
# Git cleanup

Run this workflow directly in the current session. Use the script for Git checks and deletion; review uncertain work yourself and report the findings to the user. Do not delegate to subagents or switch models. Ask the user when evidence or intent remains unclear.

## Preview

1. Confirm the target repository from the user's request or current directory. Use one repository by default. Use `--root <folder>` only for an explicitly requested folder sweep; discovery stops after four levels and skips nested repositories.
2. Run `uv run <skill-dir>/scripts/git_cleanup.py --repo <repo>`. Requires Git, Python 3, and uv. The script fetches and prunes remote-tracking refs, but leaves remote branches on the server unchanged. Use `--base <ref>` when the detected integration branch differs from the project's workflow. Add `--min-age <days>` to change the seven-day grace period for newly created empty branches.
3. Review uncertain items using [model review](references/model-review.md). Give KEEP, REMOVE recommendation, or ASK for each reviewed item, with evidence. The model may recommend keeping a script candidate too; if so, pause apply, since the script applies its whole REMOVE list.
4. Present the concise plan using the report format below, then apply proven finished work automatically in the same run. The user's cleanup request authorizes removal of merged branches, eligible old empty branches, clean finished worktrees, and stale records. A pushed branch alone is not finished: retain it unless merge evidence exists. Honor an explicit preview-only request.
5. Keep uncertain items out of the automatic cleanup. Ask only about named unmerged work that the model recommends discarding. After explicit approval, preview again with a separate `--discard <branch>` for each approved name, disclose its unique commits, and apply that plan. This option retains worktree blockers and protected branches.

Done when the user can identify every proposed removal. Keep uncertain work. A missing upstream alone is not merge evidence. Protected integration/release branches are excluded. Squash/rebase evidence uses patch equivalence; squash lookup is bounded to the last 1,000 base commits.

## Apply

Repeat the same command and options with `--apply <plan-id>` immediately after presenting the automatic plan; no confirmation pause is needed for proven finished work. The script fetches again, compares the plan including commit tips, and checks each candidate again before removal. If the plan changes, preview and review it again. Reconfirm a discard only if its named branch, tip, or scope changed. Report partial failures; preserve failed worktrees and their branches.

Worktree removal uses Git without force. Primary/current, locked, dirty, ignored-file, and operation-in-progress worktrees are retained. Clean worktrees can still belong to running agents: retain worktrees with active or unclear ownership. Avoid concurrent Git edits during apply; the checks do not provide a repository-wide lock.

Done when the script reports its result and you summarize removals and blockers. Use only the script's approved operations; leave arbitrary sibling directories, remote branches, stashes, and object databases alone.

## Report format

Follow the wait-what style without requiring that skill to be installed: give brief context, use short sentences and plain words, and explain unfamiliar Git terms once. A worktree is an extra working folder for a repository. Use the target repository's `GLOSSARY.md` terms when present; follow `GLOSSARY-MAP.md` if it has several glossaries. Apply ASD-STE100 Simplified Technical English principles; keep exact branch names, paths, and command options unchanged.

Every preview must contain these blocks, in this order:

1. **Scope and status:** one short sentence naming the repository and what happens next: "I found 3 finished branches and 2 extra worktree folders. I will remove them now." Use actual counts. Say "Preview only" when requested. Report any blocker that affects this result.
2. **Findings and suggestions:** use one table per repository, with one row per branch/worktree pair or separate folder. Include every proposed removal and every reviewed KEEP or ASK item. Use these columns:

   | Item | What I found | Suggestion | Why / evidence |
   | --- | --- | --- | --- |
   | Exact branch name and worktree path, if any | Short observed fact | REMOVE, KEEP, or ASK | Commit, PR, task, or path supporting the suggestion |

   Separate observed facts from model judgment. Say "Unknown" when evidence is missing. Explain technical results in plain words, such as "Its changes are already in main." Mark each discard as **UNMERGED WORK: N unique commits**, and show its full tip SHA. Keep protected branches in a short separate bullet if the script excludes them. State the PRUNE count separately as stale Git records, not folders to delete.
3. **Action:** give separate totals for branches, worktree folders, and stale records. The table must identify exact removal names/paths. Retain the exact script options and plan ID for apply; show the ID to the user only when needed to resolve a changed plan. If no automatic action remains, say "Nothing to remove automatically." Ask only about unresolved items where the user's answer can change the action; explicitly name unique work before requesting permission to discard it.

Keep raw logs out of the main report. Include a short error excerpt only when it explains a blocker. Group unrelated configuration problems under "Other setup issues" and state whether they affect cleanup; do not mix them with cleanup findings.

After apply, give one completion sentence with counts and a compact table of **Removed**, **Kept**, or **Failed** items. Give a reason and next step for each failure. Avoid repeating the full preview. Summarize routine protected branches in one bullet; show individual kept items only when their reason matters. Only a successful apply establishes that an item was removed.

For implementation checks, run `uv run <skill-dir>/scripts/test_git_cleanup.py`; it creates disposable repositories, never cleans the user's repositories. See [design sources](references/design-sources.md) for the comparison behind this implementation.
