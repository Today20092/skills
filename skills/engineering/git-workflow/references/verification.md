# Verification and release evidence

## Reuse checks for the source they tested

Read the repository's scripts and CI first. Use its existing commands and required gates.

During edits, run affected tests. Before integration/release, verify the final candidate with the required full gate. Keep a short record with the PR evidence or existing task record:

```text
Source: <commit SHA; clean, or exact patch/tree identity if dirty>
Command: <exact command and relevant non-secret options>
Environment: <runtime, lockfile, test config, local/preview/service target>
Result: <passed/failed/skipped, result artifact or CI run>
```

A commit SHA alone does not identify uncommitted source. Reuse a result only when the tested source and relevant environment are unchanged. New commits, merges, rebases, dependency/config changes, or changed service state require checks appropriate to that change and the repository's integration gate. Re-run required CI even when local evidence exists. Keep independent merge-candidate verification where the repository requires it.

Record one reason for repeating a full local suite: changed source/environment, required gate, or diagnosis. While an identical run is still active, use its result instead of starting another.

## Isolate test resources

Use existing runner options to give each simultaneous run its own port, temporary database/runtime state, and report directory. Keep those values together in the task's existing launcher/configuration. Select an available port before launch and verify the server belongs to the task before reusing it. A distinct port alone does not isolate a shared database directory.

If isolation is unsupported, serialize the conflicting runs. Do not stop another task's server or a live upload to free a resource. Investigate database locks and ownership before changing dependencies. Once the cause is known, put the allocation or isolation in the shared test launcher rather than repeating shell workarounds in each task.

Make browser readiness explicit: wait for the application and required fonts, choose the intended scroll position, and address controls by role and accessible name within their relevant section. Keep real tests for carousel boundaries, sticky-header obstruction, broken images and changing progress values when those behaviors are affected. Preserve traces on failure. A viewport reset for an isolated accessibility scan does not prove the actual scrolled interaction works.

## Verify the service flow that changed

Before release, read the project's setup guide and list the changed external-service assumptions: account/environment, required binding and secret names, migrations, and the user-visible flow. Check presence without printing secret values. Use the existing deploy/setup path; prefer available credentials over a new login flow.

Test safely in an isolated staging/preview environment where available. Service tests do not authorize sending real customer mail, uploading private media, or mutating unrelated production data. Use controlled recipients and fixtures within the task's authorization. If access or authorization is missing, finish independent work and state the exact blocked check. Keep any repository-required release gate blocked rather than claiming readiness.

For a testimonial feature, the acceptance flow is:

1. A controlled client submits a quote and consent.
2. The intended reviewer receives the email.
3. The approval link opens a confirmation; confirmation publishes the quote.
4. Rejected or unapproved quotes remain hidden; expired/reused approval links fail safely.
5. The public page shows the approved quote. Remove or clearly segregate test data.

A local mock verifies application behavior; it does not verify real delivery. A successful deployment or health response verifies availability; it does not verify the service flow. Record the deployed commit and which service checks passed or remain unverified.

## Turn repeated failures into checks

For mechanical release rules, extend the repository's existing workflow/configuration tests. Check real invariants such as PR targets, permitted deployment refs, required binding names, and test-state isolation. Keep judgement about feature scope and safe batch boundaries in review guidance. Implement repository-specific checks when requested; this skill supplies the process, not an assumed working CI setup.
