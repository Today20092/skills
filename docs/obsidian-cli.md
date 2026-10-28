# Obsidian CLI skill

[![skills.sh](https://skills.sh/b/Today20092/skills)](https://skills.sh/Today20092/skills)

An agent skill for operating Obsidian vaults through the official `obsidian` command-line interface.

## Why this exists

Agents can edit Markdown directly, but Obsidian's CLI understands the application: vault selection, wikilink resolution, templates, properties, tasks, link-aware moves, history, Sync, Publish, plugins, and developer tools. This skill routes vault work through those native commands and adds safeguards for destructive operations.

It uses the installed CLI's `obsidian help <command>` output as the source of truth instead of copying Obsidian's evolving command catalog into the skill.

## Install

Install globally for Codex:

```shell
npx skills add Today20092/skills --skill obsidian-cli -g -a codex
```

Or install interactively for another supported agent:

```shell
npx skills add Today20092/skills --skill obsidian-cli
```

Obsidian 1.12.7 or newer must be installed. Enable **Command line interface** under **Settings → General**. See the [official Obsidian CLI documentation](https://obsidian.md/help/cli).

## Use

Ask the agent naturally:

- “Search my vault for notes about causal inference.”
- “Append this task to today's daily note.”
- “Rename this note and preserve its internal links.”
- “Show unresolved links in my Work vault.”
- “Reload my plugin and report console errors.”

The skill resolves the target vault and file, checks live command help when needed, runs the smallest native command, and verifies mutations with a read operation.

## How it was made

The skill was built from [Obsidian's official CLI documentation](https://obsidian.md/help/cli) and tested against the installed CLI.

Its writing follows Matt Pocock's [`writing-great-skills`](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-great-skills) approach:

- Predictable process over fixed output.
- A model-invoked description with distinct trigger branches.
- Ordered steps with checkable completion criteria.
- The live environment as the source of truth, avoiding a stale documentation cache.
- Progressive disclosure through official documentation and command help.
- Aggressive pruning of duplication and no-op instructions.

The result is intentionally one skill with no scripts or bundled command reference. The Obsidian CLI already provides both.

## License

[MIT](../skills/productivity/obsidian-cli/LICENSE)
