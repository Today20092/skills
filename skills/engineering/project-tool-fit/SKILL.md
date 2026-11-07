---
name: project-tool-fit
description: >-
  Assess Oxc and other FOSS tools against a project's needs, existing checks and compatibility. Use for tool recommendations, toolchain assessments, AI-agent feedback improvements, or deciding whether to adopt or replace project tooling.
---

# Project tool fit

Assess which tools would improve this project. Recommend the smallest useful change, explain it in the user's terms, and offer a concrete setup.

## 1. Establish the project and need

Read the project's agent instructions and glossary. Follow `GLOSSARY-MAP.md` to the relevant `GLOSSARY.md` when present. Inspect the manifests, actual file types and check commands relevant to the request. Follow into resolved lockfiles, workspaces, CI, tool configs and constraints where they could change the decision. Use structural code discovery when relationships matter.

Record the scope, current tools and their responsibilities, and the problem each candidate would solve. Separate observed failures/timings from suspected gaps. For a new project, use its intended workflows and risks as the baseline and label assumptions. If several projects are requested, assess each separately and identify shared recommendations afterward.

Done when each investigated need has a project fact or an explicit assumption. A working existing setup is a valid outcome. When sufficient evidence supports keeping it, and the user did not request a survey or replacement comparison, give an early keep/skip result with the evidence limits. Resume candidate research when a gap or comparison warrants it.

## 2. Research candidates by need

For JS/TS tooling assessment, read the relevant sections of [Oxc and FOSS research](references/oxc-and-foss-tool-fit.md): the tool and compatibility sections for ordinary applications; component/integration sections for compiler, bundler, editor or AST-tool projects; the inventory for organization-wide requests. The 68-repository inventory is a dated snapshot, not a required installation list.

Research other FOSS tools for the needs found in step 1, including needs outside Oxc's scope. The reference's alternatives table is a starting point, not a closed catalog. Examples of branches:
- Code feedback: linting, formatting, type checks, tests, unused dependencies and public exports.
- Product behavior: browser flows, accessibility, performance and diagnostics.
- Delivery: dependency risk, containers, reproducible environments, tool versions and repeated tasks.
- Data/search: storage, analytical queries, transcripts or retrieval, only when these are actual project needs.

Use the installed documentation skill/Context7 for current library and CLI docs when available; otherwise consult owning docs and source. Use official repositories, package-specific releases, manifests, licenses and issue/release notes for evidence. Research the strongest plausible alternatives to a proposed replacement and compare keeping the current tool. Stop expanding a category once its need has a defensible choice. Browse more broadly when the user asks for a comprehensive survey, stating the surveyed scope.

Refresh material claims for shortlisted tools: supported versions and file types, runtime/OS/architecture, maintained releases, license, plugin/config compatibility, automation outputs and installation requirements. Cite primary sources and date observations. Distinguish source licenses from hosted service terms; mark unknown licenses or compatibility as unresolved. Public source, a free plan and FOSS are different claims.

Done when each shortlist entry has current evidence for its required capabilities and license, or a named evidence gap that limits the recommendation.

## 3. Decide fit

Map the current responsibility to candidate coverage, gaps and the tool that will retain responsibility. Apply these checks where relevant:
- Separate script linting, framework/template rules, semantic linting, compiler diagnostics, declaration builds, formatting and rendered accessibility.
- Check configured rules, processors, plugins, overrides, ignores, globals, framework versions and monorepo boundaries before replacing a checker.
- Check formatter languages/plugins, import or Tailwind sorting, save actions and representative output. Give each file type one formatting owner.
- Check Node's existing capabilities and the current build pipeline before adding a runner, transformer, parser, resolver or minifier. Ordinary apps may already use these indirectly.
- Check dynamic loading and published entry points before acting on unused-code reports.
- Treat experimental replacements as bounded trials. Upstream benchmarks and compatibility goals are hypotheses until verified on this project.
- Prefer existing commands and pinned local tools. Evaluate agent usability through reproducible noninteractive runs, clear exit codes, useful diagnostics and verified structured reports where supported. Check mode and write/fix mode have different effects. Avoid watch mode for a one-time agent check.
- Include setup, maintenance, execution cost and lost coverage in the decision. A second tool must fill a gap or produce a measured benefit.

Assign **adopt**, **trial**, **keep**, or **skip**. A trial states the uncertainty, representative test and pass condition. Recommend speed improvements as measured only after a comparable local baseline; otherwise say the speed benefit is unverified.

Done when every recommendation names its benefit, existing overlap, material limit and verification method. Keep uncertain tools out of an unconditional adoption recommendation.

## 4. Explain and offer setup

Use the user's wait-what style: give the missing context first, then use short sentences, familiar verbs and project glossary terms. Explain technical terms when first needed. Aim for ASD-STE100-style clarity without claiming formal compliance. This behavior is self-contained; another installed skill is not required.

Lead with the decision and why it matters to this project. Show only the strongest recommendations and significant keep/skip decisions in the main answer. Put an extensive requested survey in a linked research artifact using the project's documentation convention.

For each proposed tool give:
- **Project evidence:** the file, workflow, gap or measured cost.
- **Benefit:** a concrete improvement for the user and, when relevant, the AI agent.
- **Tradeoff:** overlap, migration effort, compatibility or operational limits.
- **Next step:** the smallest trial/setup, affected files, validation and rollback.
- **Source/confidence:** primary evidence; distinguish documented capability from local proof.

When recommending a change, close with a specific setup offer, such as “I can add Oxlint to the existing check command and retain the template accessibility checks.” For a keep/skip result, explain why no setup is needed. Assessment authorizes investigation and recommendations. If setup is already requested or authorized, proceed within that scope instead of asking again.

## 5. Set up when requested

Use the existing package manager and project conventions. Make only the selected dependency, config, script and CI changes; configure editor integration when requested. Prepare a reviewable diff and preserve existing coverage until the replacement passes the stated comparison. Keep bulk formatting separate where practical. Explain any unavoidable output changes.

Run the relevant checks and compare diagnostics, representative formatting, builds/declarations or runtime behavior according to the replacement's contract. For performance claims, measure comparable commands and disclose cache/environment differences. Report what changed, what passed, skipped checks and remaining risk. Global installations and external service changes require authorization within their actual scope.

Done when the selected setup is verified or its blocking evidence is explicit. Stop once the project's identified needs are covered.
