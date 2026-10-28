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

| Skill | Purpose |
| --- | --- |
| [agents-md-field-study](skills/engineering/agents-md-field-study/SKILL.md) | Review project agent instructions against a field study, then apply the improvements you select. |

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

The Google Rust guidelines skill is under consideration; it has not been added yet.

## License

[MIT](LICENSE). The Obsidian CLI skill also retains its [original copyright notice](skills/productivity/obsidian-cli/LICENSE). Source acknowledgments and third-party documentation links remain with each skill.
