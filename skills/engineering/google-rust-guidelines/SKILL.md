---
name: google-rust-guidelines
description: Apply Google's Rust style guidance when writing, refactoring, or reviewing Rust code, designing Rust APIs, or assessing Google-style adoption. Resolve application, library, and platform context before recommending changes.
license: CC-BY-3.0
---

# Google Rust Guidelines

Apply the relevant guidance to the requested Rust work. This is an independent adaptation of Google's guide, with project-context safeguards. Attribution, reviewed revision, and update procedure are in [sources.md](references/sources.md).

## Establish context

Read the applicable repository instructions, affected code and callers, toolchain/MSRV, formatter and lint configuration, and relevant checks. Classify the affected interfaces by actual consumers: application-internal or reusable across projects. A Cargo library target or workspace boundary alone does not establish a reusable public API.

Use the user's request and repository conventions to set scope. Existing compatibility promises, runtime requirements, and toolchain constraints take precedence over this adaptation. If Google-style adoption is explicitly requested, identify conflicting project choices and migration consequences before changing contracts. Preserve accepted deviations; explain consequential conflicts rather than silently broadening the task.

Context is sufficient when the affected consumers, governing conventions, and requested operation are known. Ask only for a missing decision that changes the implementation.

## Consult the relevant rules

Read the corresponding sections of [rules.md](references/rules.md):

- Modules, imports, formatter configuration: **Organization and formatting**.
- Ownership or cloning: **Ownership**.
- Function signatures, types, traits, naming, public compatibility: **API design**.
- Error handling, concurrency, unsafe, macros, implementation, documentation: **Implementation and safety**.

Read [google-platforms.md](references/google-platforms.md) only when the code belongs to Chromium, Android, or Fuchsia, or the user asks about those environments. Identify the actual codebase; running on Android or using a browser library does not make a project part of Google's platform repositories.

The references are an attributed rule inventory with exceptions, not authorization to migrate the whole repository. For a full-guide review, account for every inventory section and mark irrelevant platform sections inapplicable. For a focused task, apply only rules that affect the requested scope.

## Apply and verify

For implementation, make the smallest coherent change that meets the task and applicable rules. Update affected callers, tests, fixtures, and documentation. Check compatibility before changing signatures, visibility, traits, constructor names, or public attributes. In application code, require a demonstrated benefit before generalizing an API.

For review, report findings without editing. For each finding, identify the location, applicable rule and exception, concrete effect, and suggested correction. Distinguish correctness or compatibility defects from optional style preferences. Review surrounding callers before declaring a preference a defect.

Use the repository's established formatting, linting, testing, and build commands for the affected scope. Verify version-sensitive language, library, and tool behavior against the pinned toolchain and official documentation; use Context7 when available, otherwise official sources. This skill itself requires no particular connector. Change dependencies, toolchains, lint policy, or CI only when the task calls for that change.

Completion means the requested scope is handled, relevant failure cases and callers are checked, and remaining limitations are reported. State what changed or was found, the important tradeoffs or justified deviations, and checks actually run. A successful formatter or linter alone does not establish semantic correctness.
