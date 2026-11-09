# Agent guardrails

Written 2026-11-09 from general knowledge. Tool names here are leads: confirm current status, versions and flags in step 3 of the skill before recommending one.

## Layers

Mark each layer covered, gap or not applicable. A layer is covered only when a check runs without a person and fails on a violation.

| Layer | Drift it stops | Typical guardrail |
|---|---|---|
| Format | Noisy diffs, style churn | One formatter owner per file type, in check mode |
| Lint | Known bug patterns, framework misuse | Linter with framework rules |
| Types | Guessed shapes, unhandled cases | Strict compiler flags, framework checker |
| Data at trust boundaries | Unchecked input reaching core code | Schema validation at each entry point |
| Architecture | Imports across module seams, logic in the wrong layer | Dependency rules, custom structural rules |
| Dead code and duplication | Parallel helpers, abandoned exports | Unused-code and copy detection |
| Behavior | Regressions, tests that prove nothing | Single-run tests; mutation tests on hot modules |
| Rendered product | Broken flows, inaccessible or shifted UI | Browser tests, accessibility engine, screenshots |
| Dependencies | Stale or risky packages, unreproducible setups | Pinned tools, lockfile checks, update bot, scanner |
| Enforcement | Checks skipped or weakened | See below |

## Enforcement

A guardrail an agent can skip or weaken gives false confidence.

- One command runs every check, and agent instructions name it.
- Fast checks run in pre-commit or agent hooks; everything runs in CI.
- Suppressions need a written reason, enforced by a lint rule where one exists, such as requiring a description on `@ts-expect-error`.
- Changes to check configs get human review. Use CODEOWNERS or an agent hook where the project has them.

## Agent-usability test

Prefer the guardrail that passes all of these:

- **Tight:** fast enough to run after each change, with a path-scoped mode where supported.
- **Deterministic:** the same input gives the same result; no network or shared state unless the check needs it.
- **Noninteractive:** no prompts, single-run mode, meaningful exit codes.
- **Directive:** the failure gives file, line and the fix. Write custom rule messages as instructions: "Import from `@/lib/db`, the only module that owns the client."
- **Separated:** check mode is read-only; fixing is a distinct command.

## Per-stack starting points

Reuse what the project already has. Take only what fills a marked gap.

| Stack | Leads |
|---|---|
| TypeScript/JavaScript | `strict`, `noUncheckedIndexedAccess`; typescript-eslint or Oxlint; Biome, Prettier or Oxfmt; Knip; dependency-cruiser; ast-grep for project-specific rules; jscpd; Vitest; Stryker |
| React | Hooks and React Compiler lint rules; Playwright; axe-core |
| Astro | `astro check`; eslint-plugin-astro for template rules; Prettier's Astro plugin or current Oxfmt/Biome support; browser and axe tests against the built site |
| HTML | html-validate; axe-core on rendered pages |
| CSS | Stylelint, with rules that require design tokens for color and spacing |
| Tailwind | One owner for class sorting; eslint-plugin-better-tailwindcss for unknown or conflicting classes; a rule limiting arbitrary values where tokens exist |
| shadcn/ui | Treat `components/ui` as owned code with its own edit policy; restrict direct primitive imports outside it; check the current CLI for upstream comparison; pair with the shadcn skill or MCP |
| Python | Ruff; ty, Pyright or mypy; uv; import-linter; pytest |
| Rust | rustfmt; Clippy; cargo-deny; cargo-nextest |
| Go | gofmt; golangci-lint; govulncheck; `go test -race` |

For agents, also check whether the framework ships an MCP server, a docs index or an agent skill. Current docs prevent stale-API drift that no linter catches.

## Structural adoptions

Some tools change how code is written instead of checking it. Effect is the main TypeScript example: errors, dependencies and concurrency appear in the type signature, so the compiler reports a forgotten failure case.

The payoff is highest in services heavy with async work, I/O and failure handling. The cost is that its style spreads through the code, every contributor must learn it, and agents need docs for the exact installed major version.

- Check the current major version's stability, and whether a lint plugin or language service exists for it, before recommending it.
- Default to **trial**: one hot module, with a pass condition. Default to **skip** for static sites and simple CRUD.
- Consider the lighter option first when the gap is narrow: a schema library at trust boundaries, or a stricter lint rule.
- Migrate behind a module's existing interface so the rest of the code does not change with it.
