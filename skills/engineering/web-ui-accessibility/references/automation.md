# Automated checks and setup

Use this reference when setting up project accessibility checks or verifying a UI revision. The skill's accessibility and usability checklist remains the review contract; tools supply evidence for parts of it.

## Choose the layers

| Tool | Run it for | Evidence and limit |
| --- | --- | --- |
| Playwright + `@axe-core/playwright` | Rendered pages, states and browser interactions; local completion and CI | Axe reports rule violations and incomplete checks. Playwright verifies tasks, keyboard behavior, focus, error recovery, themes and reflow. Explicitly assert control-boundary and interaction-state contrast; axe alone does not cover every pair. |
| SquirrelScan, when installed | Local site-quality baseline and follow-up scores | Broad HTTP/SEO, link, image and performance hints; static scores and warnings require contextual review and do not replace rendered accessibility checks. See [local workflow](#local-squirrelscan). |
| Astro Audit toolbar | Immediate feedback while developing an Astro page | Built into Astro development; inspect its findings after editing. A quiet toolbar is not a CI pass. |
| `eslint-plugin-astro` with JSX accessibility rules | Fast source checks on `.astro` and React JSX/TSX | Associated labels, alt text, semantic and ARIA mistakes. Enable the matching JSX rules on React islands too. Static linting cannot measure rendered colors or prove custom-component behavior. |
| Accessibility Insights for Web | Guided manual review and keyboard tab stops | Free open-source Chrome/Edge extension. FastPass combines automated checks with tab-stop review; its documented guided assessment targets WCAG 2.1 AA, so supplement with the skill's WCAG 2.2 checks. Human judgement is still required. |

Prefer these complementary layers over several competing accessibility scanners. Installing a package, browser extension, or toolbar does not demonstrate a successful check.

## Set up a project

1. Inspect package scripts, lint configuration, test runner, supported Node version, routes and CI. Resolve current docs through Context7 or official sources. Select dependency versions with compatible peer ranges and preserve the lockfile. Use the existing runner and components where possible.
2. Add cached accessibility linting with failing exit status. Teach the linter the actual semantics of house controls, with narrow component mappings or documented local exceptions. A source check must not silently omit Astro or React surfaces.
3. Add browser tests against an isolated local **production build**. Use local pinned axe code, a fixed browser version from the lockfile, one server startup, two or fewer workers on constrained machines, reduced motion and no arbitrary sleeps. Wait for hydration of interactive islands before exercising them. Bound external media dependencies without masking relevant content or controls.
4. Start with every public route in a narrow light view and a wide dark view. Add a focused interaction test for the changed task: real keyboard input, required/invalid fields, correct status, preserved entries, duplicate activation where asynchronous, and failure/recovery. Use actual hover and focus. Add a broader on-demand matrix covering opposite theme/width pairs, intermediate width, text resize/spacing, forced colors and relevant disclosures. CSS font resizing is not actual browser zoom; desktop Chromium emulation is not an Android device test.
5. Attach axe violations **and incomplete findings**, screenshots and traces on failure. Fail on unexplained violations; review incomplete checks explicitly. Keep exact, reasoned exceptions only when the pattern is verified. A new gate exposes existing defects: fix the responsible layer or report the exact blockers, rather than weakening rules or silently baselining them.
6. In CI, install lockfile dependencies, run lint, build once, install/cache the required browser, run the small default suite, and upload failure evidence. Never rebuild separately for each viewport. Keep browser packages and reports outside production assets.

Done when a clean checkout can run the documented commands, the intended CI step is wired, a real failing UI state is detected, and the repaired state passes. Report dependency/browser setup separately from steady-state runtime.

## Local SquirrelScan

For a site audit or site-quality fix:

1. **Discover:** check project audit scripts and an installed `squirrel` command or known local binary. Read its version and help before choosing flags. If unavailable, record SquirrelScan as not run and continue the other checks; installation is a separate choice.
2. **Serve locally:** use the current isolated local production build and project-approved test data. Verify readiness. For a dedicated audit-origin build, make generated canonicals and sitemap agree with the scanned origin without changing production configuration. Record any fixture gaps. Use the installed version's offline, passive/HTTP and no-publish options when supported; record unsupported options and scope limits. Keep results local.
3. **Measure:** save the current report as the audit baseline. During implementation, preserve that baseline and rerun after fixes with the same scanner version, scope, page limit, configuration and concurrency. Run browser/load tests separately to avoid local simulator contention. If environment or configuration changes, retain a comparison that separates those changes from source fixes.
4. **Review:** report overall score/grade, failures, warning counts, rule groups, scanned pages, version, command/configuration, coverage limits and artifact paths. Check individual recommendations against rendered behavior and the relevant standard. Preserve useful content, semantics and security. For an evidenced exception, document its reason and keep both unadjusted and contextual scores/reports; do not present an exception as an application fix. A score is supporting evidence, not accessibility conformance or production performance.

Done when the current local score and findings are recorded, implementation fixes have a comparable follow-up report, and remaining warnings, exceptions and unavailable checks are explained. The [SquirrelScan documentation](https://docs.squirrelscan.com/) and installed help are the CLI references; avoid fixed flags copied from another project's run.

## Use the fast path after UI work

- During editing: cached source lint and the specific changed interaction test. Rebuild only when production output is stale.
- Before completion: relevant source checks plus the default rendered gate against current output; inspect the task's manual checklist. Shared component/token changes require sibling consumers and applicable themes/states.
- Broader changes or newly found responsive/theme defects: run the extended matrix. Avoid repeating unchanged passing work without a new reason.
- Measure the local default suite once and record test count, elapsed time, browser and machine limitations in project docs. Use zero retries while stabilizing; arbitrary waits and retries can hide defects.

For contrast, resolve actual rendered CSS colors including alpha against the effective background. Text is at least 4.5:1, or 3:1 for qualifying large text. Meaningful control boundaries and states need 3:1. Include resting, hover, keyboard focus, selected and error states, and keep visible labels in accessible names. Gradients, images and forced colors may need manual inspection even when an automated rule passes.

Accessibility Insights is a manual companion: document its official installation link and the review steps rather than claiming it runs in CI. Use Astro's existing development toolbar instead of installing a redundant integration. Ask users to interpret the primary action and complete/recover from the task when representative users are available; automated assertions do not establish intuitiveness.

## Sources and update points

- Playwright accessibility testing: https://playwright.dev/docs/accessibility-testing
- Browser setup and CI: https://playwright.dev/docs/ci
- Axe Playwright integration: https://github.com/dequelabs/axe-core-npm/tree/develop/packages/playwright
- Astro Audit toolbar: https://docs.astro.build/en/guides/dev-toolbar/
- Astro lint setup and compatible JSX plugins: https://ota-meshi.github.io/eslint-plugin-astro/user-guide/
- Accessibility Insights setup and assessment: https://accessibilityinsights.io/docs/web/overview/

Verify setup APIs and peer requirements when installing or upgrading. Put project-specific commands, timings, exceptions and findings in the repository; keep this shared skill independent of any one project.
