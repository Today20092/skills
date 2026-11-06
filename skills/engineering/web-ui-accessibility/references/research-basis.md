# Research basis for reusable sections

Research date: 2026-11-05. The original research artifact is `docs/research/reusable-web-layouts.md` in the YaHala repository. This portable digest retains the sources and decision basis so the skill can work outside that repository.

## Evidence and limits

The sample consists of Apple, Notion, Cloudflare, Samsung, Astro's showcase and two destinations reached from it. “Common” means recurring within this selected sample; there is no web-wide popularity ranking. Page-text extraction identified content groups, headings, links and approximate document order. It did not verify visible geometry, responsive behavior, interactions, accessibility or task success. Marketing claims were not independently verified. Duplicate extraction can represent hidden content or clones.

The section taxonomy, contracts, CTA example and page-family recipes are design/engineering synthesis, not patterns that the brands themselves named or published. Split columns and bento grids are candidate treatments, not visual findings from extracted text. Fetching a showcase entry does not verify its present framework or performance. Revisit live references and inspect rendered pages when current appearance matters.

## Brand and showcase evidence

Each linked public page was accessed on the research date. These are concise observations, not copied templates:

| Source | Observed content groups | Reusable lesson (synthesis) |
| --- | --- | --- |
| [Apple iPhone](https://www.apple.com/iphone/) | Category navigation, featured promotions with learn/buy links, lineup/comparison destinations, shopping support | Separate discovery, comparison and purchase reassurance; keep product-entry anatomy consistent. |
| [Notion product](https://www.notion.com/product) | Proposition, start/demo actions, customer logos, capability groups, workflow examples, quotations | Capabilities explain what; use cases explain where; evidence has a distinct role. |
| [Cloudflare](https://www.cloudflare.com/) | Platform proposition, network explanation, customer evidence, plan alternatives and product selectors | Distinguish explanation from choice support. Repetitive extraction limits arrangement conclusions. |
| [Samsung smartphones](https://www.samsung.com/us/smartphones/) | Family navigation, promotions, products, comparisons, trade-in, trial, switching/support | Repeated product structures can carry different positioning. Some image-led headings were unavailable. |
| [Astro showcase](https://astro.build/showcase/) | Linked site entries and submission action | A discovery collection provides references, not one universal page template. |
| [Unilever](https://www.unilever.com/) — followed from Astro showcase | Grouped navigation, investor/quick links, news with dates/types/images | Audience shortcuts and editorial collections have different jobs even when both use links. |
| [Guardian Engineering](https://theguardian.engineering/) — followed from Astro showcase | Mission, recruitment, values, team imagery, posts with authors/dates, RSS | About/team content can connect identity to current work and participation without a sales-page sequence. |

## Design guidance and book understanding

[USWDS templates](https://designsystem.digital.gov/templates/) describe adaptable component combinations. [Carbon patterns](https://www.carbondesignsystem.com/building-blocks/core/patterns/overview) distinguish components from broader combinations and decisions that meet user needs. [GOV.UK patterns](https://design-system.service.gov.uk/patterns/) organize guidance around tasks and page types. These support composition with stable parts rather than identical page stacks.

[USWDS process lists](https://designsystem.digital.gov/components/process-list/) distinguish sequential explanation from progress and unrelated content. [GOV.UK question pages](https://design-system.service.gov.uk/patterns/question-pages/) provide a service-context example of focused question flows; that context does not impose one question per page on every contact form.

The [official Refactoring UI public page](https://refactoringui.com/) demonstrates a proposition, testimonials, explanatory material, package choices and FAQs. Its public design example discusses alternatives to borders. It supports context-sensitive treatment, not a guarantee of usability.

Existing book understanding came from the local `refactoring-ui/references/book-principles.md`, an original summary of the 2018 book by Adam Wathan and Steve Schoger. This task read that summary, not the full book or a newly supplied PDF. The applied lessons are task-first design, coordinated hierarchy, bounded scales, proximity, appropriate content width, responsive proportions and useful imagery. The section reference carries concise applications so using this skill does not require another skill or a local PDF.

## Web semantics and accessibility sources

Read the skill's [accessibility checklist](accessibility.md) for actual checks. The following explain how section design meets web requirements; the brands' implementations are not conformance references.

| Source | Use |
| --- | --- |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Normative requirements; evaluate the completed page, not a pattern name. |
| [WAI page structure](https://www.w3.org/WAI/tutorials/page-structure/) | Regions, headings and relationships within reusable compositions. |
| [Understanding reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) | Flexible content under narrow width/zoom and defined exceptions. |
| [Understanding contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | Actual text/background pairs and large-text definitions. |
| [APG accordion](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/) | Complete semantics and keyboard behavior for a custom FAQ accordion. |
| [WAI carousel animations](https://www.w3.org/WAI/tutorials/carousels/animations/) | Automatic motion control. A carousel is optional, not the default proof treatment. |
| [WAI tables](https://www.w3.org/WAI/tutorials/tables/one-header/) | Comparison header/data associations. |
| [WAI form labels](https://www.w3.org/WAI/tutorials/forms/labels/) and [notifications](https://www.w3.org/WAI/tutorials/forms/notifications/) | Labels, correction and completion feedback in reusable forms. |

Tutorials and APG explain implementation; they do not replace WCAG or prove a site's compliance.

## Astro implementation references

Current official Astro documentation was queried through Context7 (`/withastro/docs`) on 2026-11-05:

- [Astro components](https://docs.astro.build/en/basics/astro-components/): props supply values, slots place child markup, named slots identify separate regions.
- [Astro layouts](https://docs.astro.build/en/basics/layouts/): layout components wrap page content with shared framing.

This supports the optional Astro composition note. It does not prescribe component APIs, hydration or a dependency change for other stacks.

## How to extend this evidence

For a new design question, choose sources for that task rather than collecting more famous homepages. Record the source, access date, actual observation and what is inferred. If the claim concerns visual rhythm, crop, breakpoints, motion or intuitiveness, add rendered or user evidence appropriate to that claim. Update the relevant contract when evidence changes a decision.
