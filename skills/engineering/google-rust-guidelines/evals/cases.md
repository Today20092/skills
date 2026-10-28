# Behavioral cases

Run each request with the skill loaded and only the stated scenario context. For independent evaluation, provide the request and context without the acceptance notes below. Reviews must not mutate files or publish changes.

## Requests and context

1. **Application ownership.** “Review this design using Google Rust Guidelines.” A desktop application has two long-lived worker threads sharing an immutable `Arc<Config>`; cloning it gives each thread ownership. Results are returned in a `Vec<Row>`, immediately indexed by the UI. The project uses stable Rust, nested Cargo modules, and ordinary unit tests.
2. **Published compatibility.** “Apply Google's non-exhaustive recommendation to our existing public API.” A published crate exposes `pub enum Mode { Read, Write }` and `pub struct Options { pub limit: usize }`. Downstream consumers exhaustively match Mode and use `Options { limit: 5 }`. No breaking release or migration is authorized.
3. **Recoverable errors.** “Review this function; do not edit.” `fn load(path: &Path) -> String { std::fs::read_to_string(path).unwrap() }` reads a user-selected file. Missing files and permission failures should be shown in the application's UI.
4. **Platform routing.** “Use the Google guide to plan a new Chromium first-party Rust component.” The component belongs to Chromium's source tree and existing build system; it needs asynchronous coordination and tests. Contrast with an independent Cargo service using its existing async runtime.
5. **Project precedence.** “Review style in our library.” Repository policy intentionally uses public fallible `new() -> Result<Self, Error>` constructors; stable toolchain configuration is pinned. A reviewer proposes renaming all constructors to `try_new` and switching to nightly for formatter options.
6. **Safety and poison.** “Assess these proposed fixes.” A performance patch introduces unchecked slice access without a benchmark. A separate patch resolves a poisoned mutex with `poison.into_inner()`; there is no invariant-restoration design. The crate uses `panic=abort`, and a proposed `catch_unwind` is described as guaranteeing recovery.

## Acceptance notes

1. Recognize legitimate shared ownership and non-deep Arc cloning; accept the vector based on consumers; avoid Chromium layout, async, and testing restrictions.
2. Identify downstream compatibility breaks before mutation; distinguish closed-domain and record-update exceptions; propose an adoption/migration decision rather than silently breaking callers.
3. Recommend a recoverable Result contract and caller/UI handling. Replacing unwrap with expect is insufficient. Respect review-only scope.
4. Reach platform guidance for Chromium, account for sequences/build/test conventions, and preserve the ordinary service's established runtime.
5. Treat constructor spelling as a Google preference subordinate to repository policy and compatibility; do not change toolchain solely for formatting.
6. Require a safe alternative assessment, a safety argument and benchmark evidence for the performance rationale; reject uninformed poisoned-state recovery and the false abort-recovery guarantee.

Passing these cases is evidence about applicability and scope, not proof that the skill can verify all Rust programs.
