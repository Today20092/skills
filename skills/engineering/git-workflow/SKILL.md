---
name: git-workflow
description: Prepare task branches, pull requests, releases, and Git handoffs. Use when choosing a base or PR target, integrating work, or checking what is merged and deployed.
---

# Git workflow

Default release path: **feature branch → PR to `main` → passing checks → authorized merge → automatic deployment**. Use a batch branch only for a deliberately combined release. A preview environment does not require an intermediate Git branch.

## Start or resume

1. Read the repository's Git and release guidance and inspect its actual CI/deployment configuration. Fetch remote state before choosing a base. Identify the current branch, worktree, uncommitted files, and existing PRs. Preserve unrelated work.
2. Give each independent writing task its own branch and worktree, using the host's managed tools when available. Record the owning task, absolute worktree path, branch, base commit, and PR target. Recheck the assignment on resume and before committing; branch changes or another active writer require isolation before further edits. Read-only review can share a checkout.
3. Base independently shippable work on current `origin/main` and target `main`. An explicit target for the current task takes precedence. Surface stale repository rules that conflict with this policy and bring the authorized policy change into the same plan. If production automation is absent, report it and scope its setup separately; a merge alone is not evidence of deployment.

## Integration and release

- **Independent change:** one coherent PR into `main`; unrelated features use separate PRs. Related UI changes can share one task and PR.
- **Batch:** choose the batch explicitly, record its base/target, integrate the selected work, and verify the combined candidate before its release PR to `main`.
- **Stack:** use only for dependent changes that benefit from separate review. Every layer merged to `main` must be safe to deploy. A stack does not eliminate checks or deployments.

Run focused checks while editing and the repository's required integration gates on the final candidate. Before verification or release preparation, read [verification.md](references/verification.md) for tested-source records, isolated test resources, and live-service checks.

Review the exact PR diff and required check results before merging. Creating a PR and merging it are separate actions: a PR request alone does not authorize a merge. Existing authorization to merge into `main` covers its configured automatic deployment; no second deployment approval is needed. Confirm the deployment result for the merged commit before reporting it as deployed.

After authorized cleanup, retire only integrated task branches and finished worktrees. Account for uncommitted work, unique commits, and needed ignored files first. Use the existing cleanup skill when available. Preserve shared branches and active tasks.

## Handoff

End Git/release work with these four facts, using verified state or an explicit unknown:

- **Local:** branch, commit, and whether edits remain; include the worktree path when several exist.
- **PR:** link, target, and required-check result for its current head, or “none.”
- **Merged:** yes/no/unknown; include the merge commit when known.
- **Deployed:** environment, deployed commit and URL with successful deployment evidence, or the blocker/not checked/not applicable.

Distinguish preview from production. State missing live-service verification even when deployment succeeded. For advice-only requests, say no Git changes were made; do not perform release operations just to fill the template.
