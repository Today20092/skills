# Rust rule inventory

Adapted from Google's Rust Style Guide; see [provenance and license](sources.md). The linked section names below identify upstream guidance. Apply the context and precedence in [SKILL.md](../SKILL.md). “Google preference” identifies a style choice, not a claim that other valid Rust is incorrect.

## Organization and formatting

Sources: [public rules](https://google.github.io/styleguide/rustguide.html#public-rules), [code organization](https://google.github.io/styleguide/rustguide.html#code-organization), [formatting](https://google.github.io/styleguide/rustguide.html#code-formatting).

- Favor readability, maintainability, ecosystem consistency, and changes that tools can understand. Google builds on the official Rust Style Guide and Rust API Guidelines, with explicit deviations. Apply API rules more strictly to reusable libraries; keep applications direct and sized to actual needs.
- Name a leaf module/file after its principal abstraction, when it has one. Give other modules a descriptive purpose name. Keep non-leaf modules mainly declarations and re-exports; a small amount of coordinating implementation is acceptable. Inline tests and cross-language binding modules do not invalidate leaf status.
- Prefer explicit imports. Permitted glob cases include inline `use super::*`, enum-centric functions, and re-exports in structural parent modules. Third-party preludes are a reviewer judgment; avoid defining new preludes by default. Private C++ namespace merging has a separate exception in [platform guidance](google-platforms.md).
- Group each `use` statement within one module, corresponding to `imports_granularity = Module`; avoid nested module paths inside its braces. Import traits locally when their methods are used in only a small part of a file.
- Qualify external free-function calls with the module name. Exceptions cover sufficiently distinctive imported names, colliding module names, and Chromium's small first-party crates. Import types and traits for unqualified use; qualification or aliases are reasonable for ambiguity, families of related types, generated code/macros, or an otherwise unwieldy import list.
- Use the project's formatter. Google's formatting choices include 100 columns, lowercase hex digits, formatting macro matchers, and escaping invisible literal characters. Options unavailable on the supported stable toolchain may be omitted. Verify availability before changing configuration; an unsupported formatting option is not a reason to upgrade the toolchain.
- Reserve `rustfmt::skip` for generated code or meaningful manual alignment, such as a matrix. Personal formatting preference is insufficient.

Chromium's small-crate and flat-layout conventions live only in the platform reference.

## Ownership

Sources: [shared ownership](https://google.github.io/styleguide/rustguide.html#avoid-rc-arc), [borrowing](https://google.github.io/styleguide/rustguide.html#prefer-borrows).

- Prefer unique ownership and borrowing when they express the object relationships clearly. `Rc` and `Arc` are appropriate when the alternative becomes unreasonably complicated to implement or maintain.
- Use a deep clone when independent owned data is needed. Prefer borrowing over cloning merely to bypass a borrow problem, but allow a pragmatic clone when lifetime relationships become excessively complex. Consider actual performance constraints.
- Cloning an `Rc` or `Arc` shares ownership; it is not a deep copy of the wrapped data. Do not report it as unnecessary deep copying.

## API design

Sources: [context](https://google.github.io/styleguide/rustguide.html#api-design-context), [inputs and outputs](https://google.github.io/styleguide/rustguide.html#inputs-and-outputs), [types](https://google.github.io/styleguide/rustguide.html#types), [traits](https://google.github.io/styleguide/rustguide.html#traits).

### Inputs, outputs, and domain types

- For immutable borrows, prefer `&T` over `&Box<T>`, `&[T]` over `&Vec<T>`, `&str` over `&String`, and `Option<&T>` over `&Option<T>`. The underlying purpose matters; non-linear string structures such as ropes need their own interface.
- Reusable libraries should consider returning iterators so callers choose consumption and allocation. Returning `Vec<T>` is appropriate when already available or naturally constructed, when most callers collect or index it, when constructing an owned collection is the purpose, or when a clearer loop makes an immaterial allocation. Application simplicity is an explicit exception.
- Reusable functions that only iterate should consider `IntoIterator` inputs. Slices are fine for application APIs when additional flexibility is unnecessary.
- Consider `impl Into<T>` for library call-site ergonomics, balanced against code size, inference, and API complexity. Google's application guidance strongly favors concrete parameters instead.
- Replace an ambiguous Boolean parameter with a meaningful enum. An obvious Boolean can stay; an argument comment can clarify intent.
- Use newtypes for semantic distinctions, type safety, a separate API, or future representation flexibility. Use named fields when tuple positions become unclear; one-field newtypes and obvious local tuples are exceptions.

### Traits and conversions

- Anticipate common user needs in foundational libraries; add application trait implementations when needed.
- Use the matching standard trait when the behavior really satisfies its contract. An inherent convenience method may coexist for discoverability. Derive implementations when they express the intended semantics.
- Google prefers generic inputs over `dyn Trait` in libraries, with code-size concerns as an exception. Treat dispatch strategy as a design choice grounded in actual constraints.
- Define a trait for generic programming, trait-based inputs/outputs, or extensions. Ordinary functionality belongs in inherent implementations; code organization alone does not justify a trait.
- Extension traits add methods to foreign types and conventionally end in `Ext`. Google generally assigns ownership to the original type's team; foundational extensions with substantial, widely understood value are an exception. Input traits implemented on foreign types are a different case.
- For public-field types, consider traits common to their fields. Google recommends `Copy` for error types where feasible and for types likely to remain copyable; most types can offer `Clone` unless representing external resources. These preferences do not justify discarding useful error context or promising incorrect semantics.
- Implement `Default` for a meaningful default state or zero-argument `new()`; public-field options bags should offer it. Deriving a syntactically available default is not evidence that the value is valid.
- Equality and ordering must satisfy their trait laws. Google prefers the partial traits unless stronger guarantees apply. Likely map keys need `Hash` and `Eq`; add total ordering only when the domain provides it. Preserve consistency between equality, hashing, and ordering.
- Pair a major `From` construction path with a discoverable inherent constructor. Use `From` only for conversions satisfying its contract, not fallible conversions.

### Naming and accessors

Sources: [naming](https://google.github.io/styleguide/rustguide.html#naming), [accessors](https://google.github.io/styleguide/rustguide.html#getters-and-setters).

- Match the standard meanings and receiver conventions of `as_`, `to_`, and `into_`. Prefer descriptive type lifetimes; `'_`, highly generic abstractions, and up to two simple local input/output or higher-ranked lifetimes can use short names.
- Choose short, meaningful generic names informed by their role or trait bound; `T` and `U` suit unconstrained abstractions. Avoid obscure abbreviations or words shortened by deleting letters; familiar domain-independent abbreviations can remain.
- Google's constructor naming preference is `new()`, `new_with_foo()` for alternatives, and `try_new()` for a constructor returning `Result`. Value conversions use `from_foo()` with an appropriate `From` implementation. This is a Google convention, not a universal Rust requirement or permission to break an existing API.
- Accessors use `foo()` for a borrow or copy, `foo_mut()` for a mutable borrow, `take_foo()` to extract and clear, `set_foo()` to replace by value, and `replace_foo()` to replace and return the old value.
- Closure accessors such as `with_foo()` and `with_mut_foo()` can bound interior-mutability access or allow follow-up validation without exposing guards. Forward the closure result when useful. Assess reentrancy and lock scope before choosing this design; add accessors only when needed.

### Public contracts

Sources: [API completeness](https://google.github.io/styleguide/rustguide.html#expected-api-sets), [hidden items](https://google.github.io/styleguide/rustguide.html#doc-hidden), [const functions](https://google.github.io/styleguide/rustguide.html#const-functions), [operators](https://google.github.io/styleguide/rustguide.html#operator-overloads), [enums](https://google.github.io/styleguide/rustguide.html#non-exhaustive-enums), [structs](https://google.github.io/styleguide/rustguide.html#non-exhaustive-structs), [function results](https://google.github.io/styleguide/rustguide.html#must-use-on-functions), [result types](https://google.github.io/styleguide/rustguide.html#must-use-on-types).

- Pair `len()` with `is_empty()`. Treat another owner's `doc(hidden)` items as private.
- Publish a `const fn` only with a commitment to its continued const usability or a client migration. Preserve mathematical/logical meaning in operator overloads.
- Google favors `non_exhaustive` for enums and public-field structs exposed across teams. Exceptions include stable, closed domains and a commitment to migrating all affected clients; structs also have an exception when callers need record-update construction. Small internal APIs can ignore this preference.
- Adding `non_exhaustive` to an existing API can itself break downstream matching or construction. Treat adoption as a compatibility change, not an automatic cleanup. A non-exhaustive struct cannot be built with a struct literal outside its defining crate.
- Mark a function `must_use` when ignoring its result defeats correct use, including pure computations and critical status information. A return type already marked `must_use`, such as `Result`, makes an extra function attribute unnecessary. Put the attribute on custom result types or lazy computations when that captures the contract.

## Implementation and safety

### Failures, matching, and concurrency

Sources: [errors](https://google.github.io/styleguide/rustguide.html#reporting-errors), [poison](https://google.github.io/styleguide/rustguide.html#poison), [panic catching](https://google.github.io/styleguide/rustguide.html#catch-unwind), [matching](https://google.github.io/styleguide/rustguide.html#dont-check-then-unwrap), [expect](https://google.github.io/styleguide/rustguide.html#expect-over-unwrap), [enum matching](https://google.github.io/styleguide/rustguide.html#non-exhaustive-enum-matching), [assertions](https://google.github.io/styleguide/rustguide.html#assertion-context).

- Use `Option` when absence/simple failure is sufficient, `Result` when a recoverable failure needs context, and panics for bugs or violated invariants according to project policy. External I/O failures are normally recoverable errors. Google's exceptions allow assertions in tests and non-fatal-error panics in developer-facing binaries; some projects require even invariant failures to return errors.
- Prefer pattern matching to a check followed by `unwrap()`. When a necessary invariant panic cannot be expressed through types or matching, prefer `expect()` with a reason. Changing `unwrap` to `expect` does not make user-triggered recoverable failures safe.
- When matching a non-exhaustive enum, Google prefers explicitly accounting for known variants and retaining a fallback for future ones. Group known ignored variants with that fallback. For a few interesting variants, use `if let` or `let ... else`; `match` is still allowed when clearer.
- Assertion context should explain the invariant, useful values, or whether failure means caller misuse or an implementation bug. Put useful diagnostic context in the assertion message rather than only in a nearby comment; avoid merely repeating the expression.
- Google's mutex rule forbids accessing poisoned state. Under this policy, propagate failure or follow the project's fail-fast behavior rather than using `PoisonError::into_inner` to continue with potentially broken invariants. A repository with a deliberate recovery contract is a documented project deviation, not something to rewrite silently.
- Google prohibits first-party `catch_unwind` except defense in depth at critical entry points where code already avoids panics, can run with unwinding, and relies on catching for no correctness property. Inspect the actual panic strategy and boundary contract. It cannot recover aborting panics. Do not introduce it as ordinary error handling or remove an established boundary merely for stylistic conformity.

### Unsafe, macros, and initialization

Sources: [unsafe](https://google.github.io/styleguide/rustguide.html#unsafe), [unstable features](https://google.github.io/styleguide/rustguide.html#unstable-features), [macros](https://google.github.io/styleguide/rustguide.html#macros), [initialization](https://google.github.io/styleguide/rustguide.html#global-initialization).

- Prefer a safe implementation. Where unsafe is necessary, isolate it behind a sound abstraction away from business logic, ideally with few dependencies. A `SAFETY:` comment explains why the operation satisfies its safety requirements; a separate technical justification explains why safe code is insufficient. A performance justification needs benchmark evidence.
- Use stable language features unless the project's explicitly accepted requirements permit otherwise. Google's platform exceptions are in [google-platforms.md](google-platforms.md). Do not treat the stable-only preference as authorization to remove required embedded or platform support.
- Prefer ordinary Rust facilities, then declarative macros, then other code generation, and finally procedural macros. Evaluate tooling, readability, and maintenance costs against the concrete benefit. This design preference does not imply removing existing framework macros or contradict using suitable derives.
- Google disallows execution before `main()`, including constructor-style initialization. Prefer initialization whose ordering and error handling are visible in the application's startup path.

### Readability and documentation

Sources: [inference](https://google.github.io/styleguide/rustguide.html#type-inference), [iteration](https://google.github.io/styleguide/rustguide.html#combinator-chains), [strings](https://google.github.io/styleguide/rustguide.html#prefer-format-or-write), [documentation](https://google.github.io/styleguide/rustguide.html#writing-doc).

- Add explicit types where conversions, parsing, or complex chains leave the reader guessing. Prefer annotations on bindings; a required turbofish can use inference placeholders.
- Keep short, expressive combinators such as `any()`. Use ordinary loops when a long chain hides branching or state changes. Google discourages `for_each` without a reason and prefers assigning a combinator chain to a named variable before using it in a `for` header.
- Prefer `format!` or `write!` for joining more than two strings or substituting values into literal templates. Choose based on the existing buffer and allocation needs; do not claim a performance improvement without evidence.
- Document public APIs with useful contracts and representative examples, rather than mechanically narrating names. Document malformed-input panic cases and unsafe function/trait invariants. Self-explanatory items or enum variants can omit redundant documentation.
- Use Markdown `///` comments for items, `//!` at the top for modules/crates, and ordinary `//` for implementation notes. Use readable sentences and punctuation, avoid language tutorials, and keep documentation directly readable instead of generating it through macros.
- Use the repository's actual testing framework and build entrypoints. Google-specific testing choices are scoped in [platform guidance](google-platforms.md); ordinary Rust tests remain appropriate elsewhere.

The compatibility checks, project-precedence policy, truthful performance reporting, and scoped workflow in this adaptation are additional application safeguards; they are not presented as verbatim Google requirements.
