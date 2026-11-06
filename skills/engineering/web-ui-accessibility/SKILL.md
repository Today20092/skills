---
name: web-ui-accessibility
description: >-
  Design, improve, or audit reusable website sections, page layouts, cross-page
  consistency, usability, and WCAG 2.2 AA accessibility.
disable-model-invocation: true
---
# Web UI and accessibility

Design, change, or audit websites and web apps for clear tasks, consistent behavior, mobile usability, and WCAG 2.2 AA accessibility. Use the current project's identity and design system. Project-specific evidence, publishing permissions, and delivery rules stay with the project.

## 1. Establish scope and reference

Choose **implement/change** or **audit/find** from the request. Identify the user's task, primary content and next action; inventory affected routes, page families, components, callers and states. Inspect existing tokens, components and project guidance before choosing replacements.

Use current project decisions, authoritative tokens/components/templates, then an approved reference for the pattern. Record the reference and its scope. Where none exists, identify a provisional reference and explain the choice. A repeated accessibility defect remains a defect.

For new pages, section reuse, CTA variants or page-family layout decisions, read [sections and layouts](references/sections-layouts.md). For the evidence behind those patterns or a brand-reference request, read [research basis](references/research-basis.md). For cross-page work, read [consistency](references/consistency.md). For layout or data presentation, read [layout and data](references/layout-data.md). For every interface change or accessibility audit, read [accessibility](references/accessibility.md) and identify applicable checks. These references are a starting set, not an exhaustive WCAG evaluation. For patterns beyond them, consult applicable W3C/WAI criteria and patterns. Fetch current library documentation through Context7 when available, or official documentation, before changing library behavior.

When a needed component or section has no suitable project implementation, or the user requests premade starting points, read [registry starting points](references/registry-starting-points.md) before choosing external code.

An audit inspects every requested page/state or marks it unavailable. Findings state expected pattern/reference, observed difference, reproducible evidence, user effect and narrow fix; distinguish defects, justified variants and uncertainty. An audit alone produces findings; implement within the requested scope.

Done when mode, task, affected surfaces, reference and applicable checks are explicit. Preserve data meanings and supported interactions.

## 2. Resolve hierarchy and layout

Choose a page family from its task, then select only sections with real content. Distinguish foundations (tokens), components (bounded units), sections (groups serving a purpose), layouts (relationships and framing), and page instances (actual content). Reuse the responsible layer; a shared button alone does not make two CTA sections consistent.

Before creating or changing a shared section, state its purpose, required and optional content, supported variants, responsive reading order and relevant states. Map equivalent uses to that contract. Extract repeated decisions into one implementation; let page content and destinations remain inputs. Add a variant for an evidenced task/content need, keeping semantics and interaction predictable.

Map changed elements to shared rules:
- Reuse semantic tokens for equivalent text, surfaces, actions, statuses, spacing, type and motion.
- Reuse existing components and supported variants; inspect local props and CSS overrides.
- Follow the page family's shell, navigation, footer, gutters and responsive conventions.
- Equivalent actions share labels, triggers, states, focus, feedback and recovery; different outcomes have distinct names.

Explain the task or accessibility gap before adding a variant. Record shared decisions beside existing project guidance. Fix shared defects at their responsible layer and local misuse locally; check affected consumers proportionately. Consistency means a shared visual and behavioral language, with task-specific compositions where useful.

Lead with the task's primary content and useful action. Keep related labels, values, units and comparisons together. Give groups more space than elements within them. Start with a single-column mobile flow, adding columns when content fits; align DOM and visual reading order. Keep essential instructions, conclusions and material uncertainty visible; disclose secondary detail under specific labels. Preserve readable secondary text and flexible containers.

Done when the chosen page family serves the task, repeated sections use shared contracts or explained exceptions, primary content is clear at phone width, visualizations answer evidenced questions, and supporting information remains accessible.

## 3. Make interactions predictable

Classify each changed surface by its outcome before styling:

| Outcome | Treatment |
| --- | --- |
| Read a metric, badge, status or legend | Informational content with ordinary reading behavior; action cues belong to real controls. |
| Reach a page, section, source or file | Descriptive link with a real destination and normal browser behavior. |
| Execute a command or change state | Labeled button; native selection control for choosing values. |
| Reveal supporting content | Native details/summary or complete WAI disclosure pattern. |
| Inspect chart data | Optional touch/keyboard inspection with equivalent values available without hover; navigation is a separate explicit action. |

Make actions recognizable before hover. For paragraph-link or navigation-link styling, apply [link recognition](references/accessibility.md#link-recognition) before acting on scanner underline warnings. Use specific labels and consistent terms. Pair unfamiliar icons with visible text; name icon-only controls by purpose. Expose current, selected and expanded states visually and programmatically.

A card with one destination can use a title link or appropriate enclosing link. Several actions need separate controls, with interactive elements outside enclosing links. Preserve browser Back. Use tabs, command menus or dialogs when warranted, implementing their complete keyboard, focus and dismissal patterns. Ordinary navigation links retain link semantics.

Define applicable resting, hover, focus, pressed, selected/expanded, disabled, loading, empty, error and success states. Delayed commands need visible progress, duplicate-activation handling and accurate outcomes. Preserve entered data, filters and focus through errors; keep recovery in context. Prefer undo for reversible work and proportionate confirmation for significant irreversible actions.

Keep essential work available without hover, long press or dragging alone. For popups, check touch/keyboard access, persistence, dismissal and viewport edges; a popup containing controls needs an interactive pattern. Read the relevant [WAI APG pattern](https://www.w3.org/WAI/ARIA/apg/patterns/) before custom interaction work. APG tooltip advice lacks task-force consensus; validate implementation against WCAG and actual browser/assistive-technology behavior.

Apple HIG and Samsung One UI may inform grouping, reachability, feedback and recovery; HTML semantics and WCAG govern web adaptation. Preserve browser conventions and site identity. Native pt/dp measurements and component rules are not CSS requirements.

Done when every apparent action has a useful predictable result, matching semantics and feedback; informational surfaces have ordinary reading cues.

## 4. Implement and verify accessibility

Apply the relevant [accessibility checklist](references/accessibility.md), including contrast measured from actual rendered pairs and states. Target WCAG 2.2 AA including level A. Treat 44×44 CSS px standalone controls and reduced motion as recommended practices beyond AA minimums, with inline prose links assessed in context.

Discover the project's checks and their prerequisites; reuse existing accessibility, responsive, chart and interaction tests. Extend checks for meaningful gaps introduced by the change. Compare shared patterns against their reference and sibling consumers under equivalent viewport, theme, data and interaction states. Follow the consistency reference's proportional regression guidance.

For site audits and site-quality fixes, run SquirrelScan locally when installed, following the [local scan workflow](references/automation.md#local-squirrelscan). When adding accessibility tooling or verifying a UI change, read [automated checks and setup](references/automation.md). It assigns Playwright/axe, Astro Audit, accessibility linting, and Accessibility Insights to their automated or manual roles, with a fast default gate and explicit completion evidence. Reuse the project's installed commands before introducing another runner.

Inspect 320 CSS px, a common phone width, intermediate width and desktop with supporting details expanded. Check 200% text, actual 400% browser zoom when available, simultaneous text-spacing overrides, long content and relevant empty/error/selected states. Inspect clipping and reading order as well as overflow. Exercise keyboard navigation, visible and unobscured focus, disclosures, reduced motion and forced colors; check screen-reader announcements and real mobile behavior when available.

For interactions, check cues before hover, touch without hover, delayed/repeated activation, failure/recovery, Back and focus on popup open/close. When representative users are available, ask them to identify an action and predict its result, complete the task and recover from an applicable error. Record confusion as evidence for revision. Automated checks and visual cleanliness alone do not establish intuitiveness.

Use prior validation to locate checks and known limitations, never as evidence for a new revision. For downloadable/offline interfaces, verify the actual delivery artifact and its supported JavaScript/network conditions under project rules.

Done for implementation when shared rules or explained exceptions hold, observed regressions are fixed, relevant checks pass, and actual results and unavailable checks are recorded beside the work. Done for audit when requested scope is accounted for and findings distinguish defects from intentional differences. Sampling cannot establish whole-site consistency. Instructions guide the agent; only executed checks provide test evidence. Claim WCAG AA as a target unless a complete evaluation supports conformance.
