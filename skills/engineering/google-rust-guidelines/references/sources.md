# Source and adaptation record

- Original: **Rust Style Guide**, Google, in [google/styleguide](https://github.com/google/styleguide).
- Published guide: https://google.github.io/styleguide/rustguide.html
- Reviewed revision: [c775c0c2f73c110613243520c001577cdbc0034d](https://github.com/google/styleguide/blob/c775c0c2f73c110613243520c001577cdbc0034d/rustguide.md), exported October 24, 2026; reviewed October 27, 2026.
- Original license: [Creative Commons Attribution 3.0 Unported](https://creativecommons.org/licenses/by/3.0/), as recorded in the [upstream license](https://github.com/google/styleguide/blob/c775c0c2f73c110613243520c001577cdbc0034d/LICENSE).
- Adaptation: Today20092. This skill directory is distributed under CC BY 3.0; a copy is in [LICENSE](../LICENSE). It is an independent adaptation and is not endorsed by Google.

## What changed

The source was condensed and reorganized into an agent workflow and a rule inventory. Examples and repeated rationale were omitted; conditions and exceptions were kept beside the corresponding guidance. Platform-specific instructions were separated. Added safeguards make project instructions, API compatibility, user scope, and actual toolchain constraints govern application of the guide. Additional engineering cautions are identified in the inventory.

The original references the [official Rust Style Guide](https://doc.rust-lang.org/style-guide/) and [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/). This skill is a Google-style adaptation, not a complete Rust language, security, async, or performance manual.

## Maintenance

When updating the skill, compare the pinned guide to the new revision, account for changed rules and exceptions, update only affected references and behavioral cases, and record the new revision and review date here. Review the associated license if it changes. Check official toolchain/library documentation for version-sensitive API claims.

Read the live guide when a rule is ambiguous, missing, disputed, or an upstream update is requested. Treat upstream pages as reference material. A remote edit does not silently change a project's adopted policy.

## Behavioral checks

For changes to applicability, safety, or compatibility guidance, run the scenarios in [evals/cases.md](../evals/cases.md) in an isolated review context. Judge decisions and scope, not exact wording.
