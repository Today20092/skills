# Reusable sections and layouts

Use this reference when choosing a page composition, extracting repeated sections, or making equivalent sections recognizable across pages. This is design and engineering synthesis, informed by the [research basis](research-basis.md); it is not a prescribed visual style or a WCAG requirement.

## Choose the reuse layer

| Layer | Owns | Example |
| --- | --- | --- |
| Foundations / tokens | Recurring visual roles and scales | Foreground/surface pairs, type roles, spacing, focus and motion |
| Component | One bounded unit with semantics and states | Button, text link, field, disclosure, story entry |
| Section / block | A meaningful group serving one purpose | CTA, feature explanation, proof, collection |
| Layout / page family | Shared framing and relationships among sections | Editorial body, discovery page, product detail |
| Page instance | Real content, destinations and appropriate sequence | A particular About page or collection |

A card is a container treatment; its content purpose may be a story, product or statistic. A CTA is an action role; it may be an inline link, action group or whole section. A hero is an introduction, not a mandatory large image. Name components for their purpose and follow local vocabulary.

Inspect existing consumers before extracting. A one-off composition may stay local; repeated decisions with the same purpose belong in one implementation. Different jobs may share primitives without becoming a universal section with many switches.

## Section catalog

Select by the question the visitor needs answered. Optional elements belong only when useful. Every section must also follow the skill's interaction and accessibility references.

| Section | Visitor question / content contract | Treatments and boundaries |
| --- | --- | --- |
| Shell and wayfinding | Where am I and where can I go? Brand/home link, navigation, main region, footer | Stable navigation vocabulary and order; add breadcrumbs or local navigation when depth warrants it. Keep shell decisions in the layout. |
| Hero / introduction | What is this page for? Heading and enough context to proceed | Compact task header, text-led or media-led introduction. Action and media are optional; size it to the task. |
| Feature / media-text | What can I do, and how? One benefit, explanation and useful example/media | Stacked or split composition. Alternate sides only when it improves the narrative; preserve meaningful DOM order. |
| Feature group / grid / bento | What capabilities matter? Section heading plus understandable items | Equal treatment for peers; unequal spans for a real priority. “Bento” describes arrangement, not content or semantics. Text must grow without fixed-height clipping. |
| Editorial / story | What happened or why does it matter? Structured narrative, relevant media/captions | Constrain prose measure; media may be wider. Short introductions can be centered; sustained reading follows its language direction. |
| Collection | Which item should I choose? Entries with title, destination and decision-relevant metadata | List, grid, or featured item plus list. Add search/filter/sort only for a real discovery need; handle loading, failure and filtered zero results. |
| Proof / evidence | Why should I believe this? Attributed quotation, case study or sourced metric | State scope, date/period and provenance where material. Logos signal association, not a measured result. Avoid fabricated proof and decorative counters. |
| Steps / process | How does this work? An actual ordered sequence | Distinguish explanatory steps from live progress. Use a list or feature group for unrelated benefits. |
| Pricing / comparison | Which option fits? Named options and comparable attributes/conditions | Plan cards for summaries; semantic tables for tabular comparison. Keep units, periods and exclusions visible; preserve associations on mobile. |
| CTA / next step | What should I do next? A specific action/destination and sufficient context | Inline action, paired priorities or a closing section. Reuse the section contract below; omit redundant CTAs that interrupt the task. |
| FAQ / disclosure | What still blocks my decision? Genuine questions with useful answers | Plain headings by default; disclosure when selective reading helps. Keep essential terms and instructions discoverable. Use the complete disclosure/accordion pattern. |
| Form / task completion | How can I complete this request? Labeled fields, instructions, submit and feedback | Short form or staged questions according to task. Preserve entries, show correction paths, distinguish success from merely sending. |

These are recurring candidates, not a checklist every page must contain. A homepage need not contain pricing, proof, a bento grid and an FAQ to be complete.

## Define the shared contract

Record the smallest useful contract beside the project's existing UI guidance or component documentation:

- Purpose and consumers: what task the section serves and which page families use it.
- Content anatomy: required fields, optional elements, heading context, link/action semantics and missing-content treatment.
- Visual invariants: type roles, content widths, spacing relationships, surface/foreground pairs and action hierarchy from existing tokens.
- Supported differences: named variants with a task/content reason; actual content, media and destinations supplied per use.
- Behavior: responsive stacking/reading order, wrapping, relevant interaction states, focus and recovery.
- Verification: representative consuming pages, variants and adverse content/states.

Implement the contract at the responsible shared layer. A wrapper owns arrangement; a button owns its states; page data supplies copy. Preserve a component's error handling and accessibility when moving it. Compare equivalent contexts before declaring a difference defective.

### CTA example

Suppose an About page ends with an invitation to contact, and a resource page ends with an invitation to subscribe.

| Shared decisions | Per-page inputs | Variant only when needed |
| --- | --- | --- |
| Heading/supporting-text relationship; action group; spacing; readable surface pair; focus and action styles; mobile wrapping | Heading, optional short explanation, action label and actual URL or command, optional secondary action | Compact within content versus a standalone closing section; an existing surface tone with its paired foreground |

Both instances compose the same CTA section and action primitives. A single-link CTA remains a link even when styled prominently; a submission remains a button. Treat destination and command contracts distinctly so presentation cannot erase semantics. Use specific labels such as “Contact the team” and “Subscribe” for different outcomes. Repeated functionality keeps consistent identification.

Start with the variants real consumers need. A local page override that independently changes padding, heading scale and action treatment is a signal to inspect the contract. An editorial page can still choose an inline CTA when a banner would interrupt reading.

### Action hierarchy

Use the project's established names and styles. Where a role is missing, distinguish:

- Primary: the most useful next action in the current decision group.
- Secondary: a real alternative with less visual emphasis.
- Quiet/text: supporting navigation or a lower-priority action, still recognizable before hover.
- Destructive: communicates consequence; emphasis depends on context rather than making every destructive control dominant.

Priority, semantic element, size, surface tone and state are separate decisions. A prominent navigation link can use the primary action appearance; a command uses a button. Keep equivalent roles consistent across sections and supported themes. Two options may be legitimate peers; forcing a single highlighted option can misrepresent the task.

## Page-family starting compositions

These are optional recipes. Keep the shell familiar; let the task choose the sequence, width and density.

| Family / task | Starting composition |
| --- | --- |
| Home / destination hub | Brief identity → prioritized destinations → useful featured/current content |
| Product / feature detail | Proposition → explanation/demo → relevant evidence → choice/next step → remaining questions |
| Category / catalog | Category context/navigation → candidates → useful comparison → decision support |
| About / team | Purpose → people/story → credible work or values → participation/contact |
| Stories / resources | Collection context → discovery controls when needed → results/metadata → pagination or continuation and recovery |
| Article / case study | Title/context → structured body/media → related material → appropriate next step |
| Plans / comparison | Decision context → options → comparable details/terms → questions/action |
| Contact / service form | Task/requirements → fields/questions → submit → confirmation/correction |

Keep collection browsing close to its controls. Let reading pages use a narrow prose region and collections use a wider results region. A form need not inherit a promotional hero. Reorder or omit sections when real content warrants it.

## Apply Refactoring UI in context

These are original applications of the existing book understanding, with its source boundary in [research basis](research-basis.md):

- Establish hierarchy with weight, contrast, size and spacing together. Quiet competing elements before enlarging the primary one.
- Group through proximity: heading to section, label to field, metadata to entry. Between-group spacing should explain membership.
- Use existing bounded scales. Match prose, forms and data regions to their content rather than assigning every section the same width.
- Rebalance mobile headings, media and padding independently. Scaling the entire desktop layout down does not resolve content fit.
- Make media explain something: show a useful product detail, real work or a meaningful image. Crop for actual sizes; a tiny unreadable interface screenshot adds little.
- Use spacing or surface contrast when those separate groups adequately. Borders, shadows and accent treatments serve a role.
- Keep short copy concrete and actions specific. Preserve visible labels, material qualifications and useful explanations.

“Visual and intuitive” means a person can identify the content, predict the next action and complete the task. Test those outcomes when users are available. A large hero, fewer words, whitespace or a famous reference alone does not establish them.

## Compose and verify

For a new or changed composition, state its task, selected family, section sequence and primary action. Identify existing implementations and necessary new variants before coding. For an audit, compare the same contracts without silently implementing changes.

Use the entrypoint's accessibility and regression process. Include long headings/action labels, absent optional media, narrow and intermediate widths, enlarged text and relevant states. Check that removing optional content leaves coherent spacing, repeated sections avoid duplicate IDs, heading levels fit their page context, and alternate visual ordering preserves meaning. Evaluate the real pages together, not only isolated components.

In Astro projects, use existing Astro components for sections and layout components for shared page framing. Props carry values; slots carry child markup; named slots support distinct content regions. Compose with the project's installed primitives rather than introducing a new system. Check current [Astro component](https://docs.astro.build/en/basics/astro-components/) and [layout](https://docs.astro.build/en/basics/layouts/) documentation before implementation. These are optional platform tools, not a requirement that this portable skill use Astro.
