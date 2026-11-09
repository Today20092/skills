---
name: project-tool-fit
description: >-
  Guardrail a project's toolchain: assess and apply the formatters, linters, type checks, tests and architecture rules that keep any stack maintainable under agent coding. Use for tool recommendations, toolchain audits, agent-feedback improvements, or adopt/replace decisions on project tooling.
---

# Project tool fit

Find where agents can drift in this project, and turn each costly drift into a **guardrail**: a check that fails with a clear fix, so the next agent corrects itself. Recommend the smallest useful set, explain it in the user's terms, and apply what the user picks.

## 1. Establish the project and need

Read the project's agent instructions, glossary and ADRs in `docs/adr/`. Follow `GLOSSARY-MAP.md` to the relevant `GLOSSARY.md` when present. Inspect the manifests, actual file types and check commands relevant to the request. Follow into resolved lockfiles, workspaces, CI, tool configs and constraints where they could change the decision. Use structural code discovery when relationships matter.

Record the scope, stack, current tools and their responsibilities. Separate observed failures/timings from suspected gaps. For a new project, use its intended workflows and risks as the baseline and label assumptions. If several projects are requested, assess each separately and identify shared recommendations afterward.

Done when each investigated need has a project fact or an explicit assumption.

## 2. Find the drift

For a question about one named tool or replacement, go straight to step 3.

If the user named a pain point, start there. Otherwise walk back a good stretch of `git log` to find hot spots, and weight them first. Look for friction an agent would hit or cause:

- Rules in agent instructions, READMEs or review comments that a tool could enforce. Each one is a guardrail candidate.
- Commits that repair style, imports, types or previously working behavior.
- Conventions the code follows only in places: error handling, data validation, file layout, design tokens, component use.
- Dependencies that cross module seams, duplicated helpers, dead exports.
- Escape hatches: `any`, `@ts-ignore`, disabled rules, skipped tests, and their recent growth.
- Checks that are slow, need a person, hang in watch mode, or fail without saying what to change.

Read [Agent guardrails](references/agent-guardrails.md) and mark each layer **covered**, **gap** or **not applicable**, with project evidence.

Done when every layer is marked. A working setup is a valid outcome: when the evidence shows the layers are covered and the user did not request a survey or replacement comparison, give an early keep/skip result with the evidence limits.

## 3. Research candidates by need

Use the guardrails reference for per-stack starting points. For JS/TS tooling, read the relevant sections of [Oxc and FOSS research](references/oxc-and-foss-tool-fit.md): the tool and compatibility sections for ordinary applications; component/integration sections for compiler, bundler, editor or AST-tool projects; the inventory for organization-wide requests. Both references are dated starting points, not closed catalogs or installation lists.

Use the installed documentation skill/Context7 for current library and CLI docs when available; otherwise consult owning docs and source. Use official repositories, package-specific releases, manifests, licenses and issue/release notes for evidence. Research the strongest plausible alternatives to a proposed replacement and compare keeping the current tool. Stop expanding a category once its need has a defensible choice. Browse more broadly when the user asks for a comprehensive survey, stating the surveyed scope.

Refresh material claims for shortlisted tools: supported versions and file types, runtime/OS/architecture, maintained releases, license, plugin/config compatibility, automation outputs and installation requirements. Cite primary sources and date observations. Distinguish source licenses from hosted service terms; mark unknown licenses or compatibility as unresolved. Public source, a free plan and FOSS are different claims.

Done when each shortlist entry has current evidence for its required capabilities and license, or a named evidence gap that limits the recommendation.

## 4. Decide fit

Map the current responsibility to candidate coverage, gaps and the tool that will retain responsibility. Apply these checks where relevant:
- Separate script linting, framework/template rules, semantic linting, compiler diagnostics, declaration builds, formatting and rendered accessibility.
- Check configured rules, processors, plugins, overrides, ignores, globals, framework versions and monorepo boundaries before replacing a checker.
- Check formatter languages/plugins, import or Tailwind sorting, save actions and representative output. Give each file type one formatting owner.
- Check Node's existing capabilities and the current build pipeline before adding a runner, transformer, parser, resolver or minifier. Ordinary apps may already use these indirectly.
- Check dynamic loading and published entry points before acting on unused-code reports.
- Treat experimental replacements as bounded trials. Upstream benchmarks and compatibility goals are hypotheses until verified on this project.
- Prefer existing commands and pinned local tools. Apply the agent-usability test in the guardrails reference. Check mode and write/fix mode have different effects.
- Include setup, maintenance, execution cost and lost coverage in the decision. A second tool must fill a gap or produce a measured benefit.
- Honor ADRs. Surface a candidate that contradicts one only when the friction warrants reopening it, and say so.

Assign **adopt**, **trial**, **keep**, or **skip**. A trial states the uncertainty, representative test and pass condition. Recommend speed improvements as measured only after a comparable local baseline; otherwise say the speed benefit is unverified.

Done when every recommendation names its benefit, existing overlap, material limit and verification method. Keep uncertain tools out of an unconditional adoption recommendation.

## 5. Report and ask

Write in wait-what style: the missing context first, then short sentences, familiar verbs and project glossary terms, with each technical term explained where it first appears.

For a question about one tool, answer in the conversation. For a project assessment, write a self-contained HTML file to the OS temp directory as `tool-fit-<timestamp>.html`, so nothing lands in the repo. Open it and give the absolute path. Lead with the coverage map of guardrail layers, then one card per recommendation, strongest first, and end with a **Top recommendation**: what to apply first and why.

Each recommendation carries:
- **Verdict:** adopt, trial, keep or skip, as a badge.
- **Drift prevented:** the project evidence: file, commit, workflow, gap or measured cost.
- **Before / after:** what an agent can do wrong today, and what it sees once the guardrail exists.
- **Benefit:** the concrete gain for future maintenance and for the agent.
- **Tradeoff:** overlap, migration effort, compatibility or operational limits.
- **Next step:** the smallest trial/setup, affected files, validation and rollback.
- **Source/confidence:** primary evidence; distinguish documented capability from local proof.

Then ask: "Which of these would you like to apply?" For a keep/skip result, explain why no setup is needed. When setup was already requested, proceed within that scope.

## 6. Apply what the user picks

Grill the user first (use the grilling skill when available) on any pick that changes how code is written, such as a typed-effect library or new layering rules: scope, first module, what stays out.

When the user rejects a candidate for a reason a future run would need, offer an ADR: "Want me to record this so future tool reviews don't re-suggest it?"

Apply one guardrail at a time, with the existing package manager and project conventions. Change only the selected dependency, config, script and CI files; add editor integration when requested. Preserve existing coverage until the replacement passes the stated comparison. Keep bulk formatting in its own commit where practical, and explain any unavoidable output changes.

For each guardrail:
1. Run it on the project and record the existing violations.
2. Ratchet: fix them when few, otherwise baseline them so new code must pass and old code can only improve.
3. Add it to the project's single check command, then to the hooks and CI the project uses.
4. Prove it goes **red**: introduce one representative violation, confirm the failure names the fix, and revert it.
5. Replace the matching prose in agent instructions with a pointer to the check command. Leave instructions that no tool enforces.

For performance claims, measure comparable commands and disclose cache/environment differences. Report what changed, what passed, skipped checks and remaining risk. Global installations and external service changes require authorization within their actual scope.

Done when each picked guardrail has gone red and then green, or its blocking evidence is explicit. Stop once the picks are applied.
