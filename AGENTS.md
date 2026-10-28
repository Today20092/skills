# Personal skills collection

This repository contains the owner's reusable agent skills. Keep one canonical directory per skill under `skills/<category>/<name>/` and list each published skill in the root README.

When adding or changing a skill, apply skill-creator and writing-for-agents when available. Preserve existing activation policy unless the user requests a change. Keep conditional references beside the skill, with links explaining when to read them.

When moving a skill, account for every supporting file, relative link, installation example, and source notice. Validate frontmatter and local links, then verify discovery with the Skills CLI. Changes to an instruction-only skill do not require executing the external operations it describes.

Use the existing categories when they fit. Add a category when real skills justify it. Category directories have no SKILL.md of their own, so they do not shadow nested skills during discovery.
