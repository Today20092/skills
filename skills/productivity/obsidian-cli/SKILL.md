---
name: obsidian-cli
description: Operate Obsidian vaults through the official `obsidian` CLI. Use for reading, searching, creating, editing, moving, organizing, or inspecting notes; managing daily notes, tasks, properties, links, templates, plugins, themes, workspaces, Sync, Publish, or developer tooling; and automating vault workflows from a terminal.
---

# Obsidian CLI

Use the installed CLI as the live source of truth. Obsidian must be installed, CLI access enabled in **Settings → General**, and the app running or launchable.

## Run a task

1. Check availability with `obsidian version`. If it fails, report the error and the setup requirement; completion means the CLI version or blocker is known.
2. Resolve the target before acting:
   - Use the current vault when the working directory is inside it.
   - Otherwise discover vaults with `obsidian vaults verbose` and select from user context.
   - Put `vault=<name-or-id>` before the command when targeting explicitly: `obsidian vault="Work" search query="TODO"`.
   - Prefer `path=<vault-relative-path>` when the exact file is known; use `file=<wikilink-name>` only when link resolution is intended.
3. Inspect `obsidian help <command>` before using an unfamiliar command or option. The installed version wins over remembered syntax; completion means every option in the proposed command is supported.
4. Run the smallest command that satisfies the request. Quote values containing spaces or shell-significant characters. Encode multiline values with `\n` and tabs with `\t`.
5. Verify mutations with the narrowest read command, such as `read`, `file`, `property:read`, `tasks`, or `search`; completion means the requested state is observable.

## Choose commands

- Discover: `help`, `vaults verbose`, `files`, `folders`, `search`, `search:context`, `tags`, `tasks`, `properties`, `backlinks`, `links`, `unresolved`, `outline`.
- Read: `read`, `daily:read`, `file`, `folder`, `property:read`, `template:read`, `wordcount`.
- Write: `create`, `append`, `prepend`, `daily:append`, `daily:prepend`, `property:set`, `property:remove`, `task`.
- Organize: `move`, `rename`, `open`, `delete`.
- Extend: use `commands` and `command id=<command-id>` for commands registered by Obsidian or plugins.
- Automate: request `format=json` where supported; otherwise use the command's documented structured format.
- Develop: use `dev:errors`, `dev:console`, `dev:screenshot`, `dev:dom`, `dev:css`, `plugin:reload`, or `eval` only when the task concerns plugin/theme development or explicit in-app inspection.

## Guardrails

- Treat the vault as user data. Read first when a mutation's target or current contents are uncertain.
- Use `create ... overwrite` only when replacement is explicit and the existing content has been inspected or is recoverable.
- Use ordinary `delete` so Obsidian moves the note to trash. Add `permanent` only when the user explicitly requests irreversible deletion and the exact path has been verified.
- Inspect `diff`, `history`, or `sync:history` before restoring a version. Verify the file after `history:restore` or `sync:restore`.
- Prefer native commands over direct filesystem edits because Obsidian can resolve links, update internal links, apply templates, and preserve app behavior.
- Treat `eval` as arbitrary code execution. Use a narrow expression, avoid secrets, and run mutations through dedicated CLI commands when available.

For syntax that may have changed, consult the [official Obsidian CLI documentation](https://obsidian.md/help/cli) and then confirm against `obsidian help <command>`.
