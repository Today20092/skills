# Consistency across pages

## Baseline and shared contract

Select the authoritative source for each pattern: current project decision, semantic token, shared component/template, then approved page or reference. Scope references by page family and state. If guidance conflicts or lacks an exemplar, record a provisional choice and uncertainty.

Compare roles rather than raw values: tokens for equivalent roles, component variants and overrides, shell/navigation/footer, responsive behavior, vocabulary, interaction states, focus and recovery. Different compositions may serve different tasks. Repeated defects remain defects.

WCAG [3.2.3](https://www.w3.org/WAI/WCAG22/Understanding/consistent-navigation.html) concerns relative order of repeated navigation within a set of pages; [3.2.4](https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification.html) concerns consistent identification of the same functionality; [3.2.6](https://www.w3.org/WAI/WCAG22/Understanding/consistent-help.html) concerns relative order of repeated help mechanisms. These do not mandate identical layouts or adding help everywhere.

## Repeated sections

For section selection, content contracts, CTA variants and page-family recipes, use [sections and layouts](sections-layouts.md). Compare equivalent section purposes and action roles, including their shared implementation, rather than requiring every page to use the same sequence or density. A legitimate variant has a task/content reason and preserves the shared contract.

## Audit evidence

Inventory requested page families, routes and relevant states. For each difference record: page/state, expected pattern and source, observed behavior, reproduction or screenshot/DOM evidence, user effect, classification (defect, intentional variant, uncertain) and narrow responsible-layer fix. Mark uninspected or unavailable surfaces. An audit produces findings; changes follow the user's requested scope.

## Visual comparisons and regression

Compare under equivalent viewport, zoom, theme, data, fonts and interaction state. Stabilize time-dependent content and animation when appropriate. Inspect screenshots and rendered behavior alongside DOM/accessibility evidence. Raw literals, token bypasses, copied components, unsupported overrides and pixel differences are investigation candidates, not automatic defects.

Fix shared rules at their source and local misuse locally. Shared tokens/shells/components need checks across affected families, variants, breakpoints and states; a local copy edit needs narrower checks. Record the sampled consumers and why they cover the change. Sampling supports bounded conclusions, not whole-site consistency.

Preserve meaningful baselines; investigate unexpected differences before replacing snapshots. Report actual checks, unresolved issues and coverage limits. This workflow is engineering synthesis; only the linked criteria establish WCAG obligations.
