# Google platform rules

Read this only for the named Google codebase or an explicit comparison request. These conditions are not general Rust restrictions. Attribution and pinned source: [sources.md](sources.md).

## Chromium

Sources: [small crates](https://google.github.io/styleguide/rustguide.html#small-crates), [layout](https://google.github.io/styleguide/rustguide.html#structure), [imports](https://google.github.io/styleguide/rustguide.html#import-macro), [async](https://google.github.io/styleguide/rustguide.html#async-await-chrome), [threads](https://google.github.io/styleguide/rustguide.html#std-thread).

- Prefer small crates, often a single file centered on one abstraction. Coherence requirements or foundational libraries can justify larger crates. Decide whether APIs belong together before subdividing into modules.
- Files within a `rust_library` share one directory; nested source directories usually indicate a need to split. Third-party code also built with Cargo follows the conventional Cargo layout instead.
- Use `chromium::import!()` and the repository's formatting entrypoint, such as `git cl format`. Free functions from small first-party crates may be imported directly.
- The reviewed guide disallows `async`/`.await` and standard-library thread creation in Chromium; use its sequencing facilities.
- Use `rust_gtest_interop` for integration with C++ test binaries. Follow the repository's actual harness.
- Style arbiters may approve particular unstable features, usually with a stabilization path. Verify current repository policy before using one.

The glob-import exception for C++ interoperability permits merging namespace fragments from several crates into a private module. It does not authorize publicly exporting the merged namespace.

## Android

The reviewed guide permits required unstable features for embedded programming after platform review. An ordinary application targeting Android does not automatically inherit this exception or Google's build policies.

## Fuchsia

Use `fuchsia_sync::Mutex` and the `#[fuchsia::test]` harness in Fuchsia. Consult its current [unstable-feature policy](https://fuchsia.dev/fuchsia-src/development/languages/rust/unstable) and [testing documentation](https://fuchsia.dev/fuchsia-src/development/languages/rust/testing.md) for platform work.

## Panic strategy

The reviewed source states that Chromium, Android, and Fuchsia require `panic=abort`, excluding Google's defense-in-depth `catch_unwind` exception there. Verify the current target configuration before making a claim about a particular build. Application platform names alone do not establish the panic strategy.

On other projects, use the project's Cargo/module layout, async runtime, synchronization primitives, formatter, and tests. Do not transplant these platform rules based solely on the programming language.
