# Coldtea AGENTS.md field study: working notes

Source: [What the 100 biggest GitHub repos put in their AGENTS.md files](https://www.coldtea.ai/blog/agents-md-field-study), Ohans Emmanuel, published August 21, 2026. Consult the source for the full study and copyable baseline.

## What the study measured

The author examined the root `AGENTS.md` files of the 100 most-starred public GitHub repositories (11.4 million combined stars) that had such a file. Files were fetched at HEAD on August 21, 2026; content analysis covers 99 non-empty files. Sections were classified using headings and keyword patterns, so individual percentages have some noise. This is a descriptive sample of large repositories, not evidence that any one rule causes better outcomes or applies to every project.

The study characterizes these files as operating manuals: project orientation and verification account for roughly half of the content. Architecture/structure (18.9%), testing/validation (17.2%), setup/build commands (12.8%), dedicated dos and don'ts (11.3%), Git/PR workflow (10.9%), and style/conventions (6.7%) were the largest named themes. Median length was 1,198 words, with a wide range (1 to 13,718); the article explicitly advises keeping its starter under two pages while tailoring it. Treat both figures as observations, not targets.

## Topic prevalence

Share of the 100 files addressing each topic, as reported by the article:

| Topic | Repositories |
| --- | ---: |
| Explicit don't-rules | 86% |
| Commit and PR guidelines | 79% |
| Testing instructions | 74% |
| Code style and linting | 73% |
| Links to other docs | 73% |
| CI and pre-commit checks | 71% |
| Build and setup commands | 62% |
| Project structure | 60% |
| Security and secrets | 54% |
| Fenced shell commands | 48% |
| Names a specific agent | 48% |
| Error-handling rules | 42% |
| Monorepo or nested files | 40% |
| Project overview | 36% |
| Naming conventions | 33% |
| Single-test command | 25% |

The article's eight-item self-check is: at least one explicit don't; commit/PR conventions; how to run tests; style/lint commands; required pre-PR checks; build/setup commands; project map; and a single-test command. These are prompts for a tailored review, not pass/fail requirements.

## Shape of the article's starter

The suggested template orders concise sections for project overview, structure, setup/build, testing, style, Git workflow, and boundaries. It uses concrete commands and paths; recommends both full-suite and focused test commands; links deeper documentation rather than duplicating it; and includes project-specific prohibitions around tests, unrelated changes, dependencies, secrets, and reporting failures. The article advises replacing placeholders, deleting inapplicable material, and tailoring the result.

## Application guidance

- Prefer verified commands, paths, and project facts over template placeholders.
- A rule's value depends on this repository. Recommend boundaries when they address a real risk or recurring mistake; avoid generic prohibition padding.
- Where a topic is already covered by a canonical doc or config, link to it instead of copying content that can drift.
- Keep root guidance useful across the project; place genuinely local guidance in nested files when the repo already uses that pattern.
- Explain evidence and tradeoffs so the project owner can choose. Do not present prevalence as proof of best practice.
