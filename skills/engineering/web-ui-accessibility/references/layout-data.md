# Layout and data presentation

Reuse the site's tokens, components and identity. When suitable tokens are absent, starting values include 16px mobile gutters, 16–20px card padding, 32px section gaps, 16–18px primary text and roughly 65–75 characters per prose line. Adjust to content and task; these are usability choices, not WCAG requirements. Use relative type sizes and flexible containers.

Keep primary content, useful actions and important uncertainty visible. Group labels, values and comparisons before decorating. Start with one column, introducing columns when actual content fits. Disclose secondary detail with specific labels and native semantics.

For data views:
- Choose charts for the actual question: zero-based bars for magnitude, dated time series for change over time, scatter plots for evidenced paired observations.
- Provide direct labels and equivalent exact values with units and periods.
- Convey platform/category distinctions and increase/decrease meanings through text alongside color.
- Keep missing values, rounding, different windows and material uncertainty explicit.
- Use semantic table headers and captions; align comparable numbers and contain essential horizontal scrolling locally.

Reference basis: [GOV.UK layout](https://design-system.service.gov.uk/styles/layout/), [spacing](https://design-system.service.gov.uk/styles/spacing/), [type](https://design-system.service.gov.uk/styles/type-scale/), [tables](https://design-system.service.gov.uk/components/table/), and [Government Analysis Function chart guidance](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/).

For interaction direction, [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/) and [Samsung One UI](https://developer.samsung.com/one-ui/index.html) inform grouping, recognizable actions, feedback and recovery. Apply their principles through HTML and WCAG; native measurements and OS patterns need web-specific judgment. Consult relevant current primary guidance when interpreting a new pattern.
