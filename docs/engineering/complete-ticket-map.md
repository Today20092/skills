Quickstart:

```bash
npx skills add mattpocock/skills --skill=complete-ticket-map
```

```bash
npx skills update complete-ticket-map
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/complete-ticket-map)

## What it does

`complete-ticket-map` runs a dependency-linked ticket set to completion. It discovers the graph, shows a mobile-friendly ASCII status map, dispatches ready tickets into separate implementation tasks, verifies their handoffs, integrates finished branches, and advances the newly unblocked frontier.

The orchestrator remains a control tower rather than becoming another implementation session. Workers retain code exploration and command output; the parent keeps only compact state, decisions, and exceptions.

## When to reach for it

You invoke this by typing `/complete-ticket-map`—the agent will not reach for it on its own.

Use it after a multi-ticket plan already exists and you want Codex to coordinate the whole build without manually opening each implementation task. Use [to-tickets](https://aihero.dev/skills-to-tickets) first when the work has not been split into dependency-linked tickets.

## The control tower

Each ticket gets one worker task and one owner. Independent ready tickets run together only when isolated worktrees make that safe; otherwise the same graph runs sequentially. Green nodes are integrated, blue nodes are active, amber nodes are ready, gray nodes are blocked, pink nodes need input, and red nodes failed.

The map changes only when state changes. Quiet waits stay quiet, and workers return bounded handoffs instead of pouring their logs into the orchestrator’s context.

## Where it fits

`complete-ticket-map` is the orchestration step for the multi-session branch of the main flow:

```txt
grill-with-docs → to-spec → to-tickets → complete-ticket-map → implement workers
```

Its key neighbours are [to-tickets](https://aihero.dev/skills-to-tickets), which creates the dependency graph, and [implement](https://aihero.dev/skills-implement), which each worker applies to one ticket. When you are unsure which flow fits, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.
