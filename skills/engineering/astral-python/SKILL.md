---
name: astral-python
description: Build and maintain Python projects with Astral's uv, Ruff, and ty toolchain. Use when creating, changing, testing, linting, formatting, type-checking, packaging, or running Python projects and scripts.
---

# Astral Python projects

Use the complete Astral toolchain for Python: uv for environments, dependencies, packaging, and execution; Ruff for formatting and linting; and ty for type checking. New projects use all three. Existing projects keep established non-Astral quality gates unless the task explicitly includes migrating them.

## Read the project

Inspect `pyproject.toml`, `uv.lock`, the README, task scripts, and CI configuration relevant to the request. Preserve the project's Python versions, dependency groups, commands, and configured quality tools. Classify the work as creating a new project, maintaining an Astral project, or migrating an existing project before changing its toolchain.

## Run with uv

Route Python environments, dependencies, execution, and tools through uv:

| Task | Command |
|---|---|
| Run a script | `uv run script.py` |
| Run a module | `uv run -m module` |
| Run a project command | `uv run <command>` |
| Add dependencies | `uv add pkg` |
| Add development dependencies | `uv add --dev pkg` |
| Import requirements | `uv add -r requirements.txt` |
| Remove dependencies | `uv remove pkg` |
| Sync the environment | `uv sync` |
| Create an environment | `uv venv` |
| Run a one-off tool | `uvx tool` |
| Install a persistent tool | `uv tool install tool` |

Use `uv run` for project tools so they run in the project environment. Use `uvx` for an ad hoc tool evaluation; add a development dependency when the project or CI needs a reproducible version.

## Check with Ruff and ty

Run the narrowest relevant tests, then Ruff formatting and linting and ty type checking. Use the project's pinned commands when configured.

For a new project, add Ruff and ty as development dependencies and configure both in `pyproject.toml`:

```text
uv add --dev ruff ty
uv run ruff format --check .
uv run ruff check .
uv run ty check
```

For an existing project missing one or more quality tools, evaluate the missing Astral tool with `uvx`, then pin and configure it when adoption is in scope:

```text
uvx ruff format --check .
uvx ruff check .
uvx ty check
```

When maintaining an existing project, preserve its configured formatter, linter, and type checker unless migration is requested. Before replacing Black, Flake8, isort, mypy, Pyright, or another gate, account for its rules, suppressions, plugins, CI integration, and supported Python version; migrate configuration and verify equivalent coverage before removing it.

**Complete when:** New projects use uv, Ruff, and ty with reproducible pinned checks. Existing projects use their configured gates, or complete the requested migration without losing covered behavior. Dependency metadata remains consistent, and relevant tests and quality checks pass or their exact blockers are reported.
