# Design sources

Research resumed on 2026-11-08. Existing options include [Trail of Bits git-cleanup](https://github.com/trailofbits/skills/tree/main/plugins/git-cleanup) and [alexei-led cc-thingz](https://github.com/alexei-led/cc-thingz). The earlier research session compared several more skills, but its source files and license checks were not retained here.

The chosen design combines deterministic Git checks with model review of uncertain branches, worktree ownership, and extra folders in the current session. It uses no subagents or model switching. The cleanup request authorizes automatic removal of proven finished work after a concise plan. Unmerged abandonment requires explicit permission and uses a named `--discard` option with the same state checks. This repository contains a custom implementation; no upstream scripts were imported. Upstream licensing must be reviewed before copying future code.

Git's [worktree documentation](https://git-scm.com/docs/git-worktree) specifies NUL-delimited porcelain output for reliable parsing and the clean-worktree checks used by removal. The script adds checks for ignored files and ongoing Git operations.

Forge PR state is deliberately not sufficient evidence: the PR may target a different integration branch, or the local branch may have advanced. This version uses local ancestry and patch equivalence against the selected base. Unproven branches remain for review.

The tree-equality and simulated-merge checks follow [worktrunk](https://github.com/max-sixty/worktrunk)'s documented `wt remove` integration conditions (checked 2026-11-11). The simulated merge proves squash merges that were edited during merge or where the base later changed the same files, which patch-id matching misses. Only the Git commands were reused; no worktrunk code was copied.
