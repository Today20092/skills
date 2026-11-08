# Design sources

Research resumed on 2026-11-08. Existing options include [Trail of Bits git-cleanup](https://github.com/trailofbits/skills/tree/main/plugins/git-cleanup) and [alexei-led cc-thingz](https://github.com/alexei-led/cc-thingz). The earlier research session compared several more skills, but its source files and license checks were not retained here.

The chosen design combines deterministic Git checks with model review of uncertain branches, worktree ownership, and extra folders. A small model reviews first; unresolved comparisons can reach a stronger model. Explicitly approved abandonment uses a named `--discard` option and the same state checks. Preview, approval, conservative retention, and evidence per removal address the requested workflow. This repository contains a custom implementation; no upstream scripts were imported. Upstream licensing must be reviewed before copying future code.

Git's [worktree documentation](https://git-scm.com/docs/git-worktree) specifies NUL-delimited porcelain output for reliable parsing and the clean-worktree checks used by removal. The script adds checks for ignored files and ongoing Git operations.

Forge PR state is deliberately not sufficient evidence: the PR may target a different integration branch, or the local branch may have advanced. This version uses local ancestry and patch equivalence against the selected base. Unproven branches remain for review.
