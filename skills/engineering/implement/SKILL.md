---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

When implementing a ticket, read its **Working branch** before changing code. Start only when its blockers are complete on that branch. Switch to the named branch if it exists; otherwise create it from the updated default branch. The branch is ready when `git branch --show-current` exactly matches the ticket.

Use /tdd where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, use /code-review to review the work.

Commit your work to the ticket's working branch. When implementing a spec without a ticket, commit to the current branch.
