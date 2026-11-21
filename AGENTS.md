# Personal skills collection

This repository contains the owner's reusable agent skills. Keep one canonical directory per skill under `skills/<category>/<name>/` and list each published skill in the root README.

When adding or changing a skill, apply skill-creator and writing-for-agents when available. Preserve existing activation policy unless the user requests a change. Keep conditional references beside the skill, with links explaining when to read them.

When moving a skill, account for every supporting file, relative link, installation example, and source notice. Validate frontmatter and local links, then verify discovery with the Skills CLI. Changes to an instruction-only skill do not require executing the external operations it describes.

Use the existing categories when they fit. Add a category when real skills justify it. Category directories have no SKILL.md of their own, so they do not shadow nested skills during discovery.

## Git workflow

One task = one branch = one pull request into `main`; no integration branch. Work in a worktree the host manages (a T3 Code thread on the main checkout moves itself with `t3_worktree_handoff`), commit work in progress instead of stashing (stashes are shared by every worktree), and end every task with a commit and a PR to `main`. Merge only when the user asks, with a merge commit. Merged branches are deleted automatically.
