# Personal Skills

My reusable agent skills, organized by category. This repository is the maintained home for skills I create or adapt for my own workflows.

## Install

Browse the available skills:

```sh
npx skills add Today20092/skills --list
```

Install one skill:

```sh
npx skills add Today20092/skills --skill everything-search
```

Add `--global` to install across projects. The installer lets you choose a supported agent; add `-a codex` to select Codex explicitly.

## Engineering

Use [$project-tool-fit](skills/engineering/project-tool-fit/SKILL.md) to find where agents can drift in any stack, recommend the formatters, linters, type checks, tests and architecture rules that stop it, and apply the ones you pick. Includes [per-stack guardrails](skills/engineering/project-tool-fit/references/agent-guardrails.md) and [research covering all 68 public Oxc repositories](skills/engineering/project-tool-fit/references/oxc-and-foss-tool-fit.md).

| Skill | Purpose |
| --- | --- |
| [agents-md-field-study](skills/engineering/agents-md-field-study/SKILL.md) | Review project agent instructions against a field study, then apply the improvements you select. |
| [astral-python](skills/engineering/astral-python/SKILL.md) | Build and maintain Python projects with Astral's uv, Ruff, and ty toolchain. |
| [git-cleanup](skills/engineering/git-cleanup/SKILL.md) | Automatically clean finished local Git work, with model review of uncertain items and a concise findings report. |
| [google-rust-guidelines](skills/engineering/google-rust-guidelines/SKILL.md) | Apply Google's Rust guidance to implementation, API design, and review while respecting project conventions and platform-specific exceptions. |
| [web-ui-accessibility](skills/engineering/web-ui-accessibility/SKILL.md) | Design, improve, or audit reusable website sections, page layouts, consistency, usability, and WCAG 2.2 AA accessibility. Invoke explicitly with `$web-ui-accessibility`. |

## Productivity

| Skill | Purpose |
| --- | --- |
| [everything-search](skills/productivity/everything-search/SKILL.md) | Search the Windows Everything index and work with its query language, saved searches, GUI commands, and SDK. [Requirements and usage](docs/everything-search.md). |
| [obsidian-cli](skills/productivity/obsidian-cli/SKILL.md) | Operate Obsidian vaults through the official CLI. [Requirements and usage](docs/obsidian-cli.md). |

## Categories

Skills live at `skills/<category>/<skill-name>/SKILL.md`. Categories organize the repository and this catalog; installation still selects the skill's unique name. The Skills CLI discovers this nested layout. A category folder should contain skill directories, without its own `SKILL.md`.

Start with Engineering and Productivity. Add a narrower category, such as Architecture or Rust, when the collection has skills that benefit from it. A skill has one canonical location, even when several topics apply. Category folders do not promise category filters in every agent's UI.

## Add or update a skill

Use a lowercase, hyphenated skill name and describe its purpose and activation conditions in `SKILL.md` frontmatter. Preserve the skill's invocation policy when moving it. Keep supporting files beside the skill and update this catalog when adding, removing, or moving one.

## Consolidation

This collection brings together the skills formerly maintained in `skills-making`, `everything-search-skill`, and `obsidian-cli`. The inherited Matt Pocock catalog and ticket-workflow customizations have been removed from the current collection. Existing Git history is preserved.

## License

The repository's original material is [MIT licensed](LICENSE), except where a skill specifies otherwise. [Google Rust Guidelines](skills/engineering/google-rust-guidelines/references/sources.md) is an attributed adaptation under [CC BY 3.0](skills/engineering/google-rust-guidelines/LICENSE). The Obsidian CLI skill retains its [original copyright notice](skills/productivity/obsidian-cli/LICENSE). Source acknowledgments and third-party documentation links remain with each skill.
