# Registry starting points

Use when a project lacks a suitable component/section or the user requests premade blocks. Start with the task and the [section contract](sections-layouts.md), then choose a source compatible with the project's stack and identity. Existing project components remain the first place to look; shadcn is an option where it fits.

## Find a candidate

The [official shadcn registry directory](https://ui.shadcn.com/docs/directory) lists third-party publishers; [official blocks](https://ui.shadcn.com/blocks) provide a baseline. Registry membership establishes distribution, not accessibility, license approval or framework compatibility.

These leads come from the 2026-11-05 registry survey. Recheck the selected item's source, current terms and delivery before adoption; a public repository's license may cover only its free collection.

| Need | Starting point | Boundary |
| --- | --- | --- |
| Marketing sections, hero, content, CTA and footer | [Tailark OSS](https://github.com/tailark/blocks) | MIT repository; broader commercial offerings and OSS delivery endpoints need distinguishing. |
| Creator link hub, destination gallery, About sections | [Shadcn Space](https://shadcnspace.com/blocks) | Mixed Free/Pro catalog. Free Bio Link 01, Gallery 01 and About Us 01 were relevant examples; match the chosen source to its [public MIT repository](https://github.com/shadcnspace/shadcnspace). |
| Stories/reels, video and image viewing | [Kibo UI](https://www.kibo-ui.com/) | [MIT source](https://github.com/shadcnblocks/kibo); media pieces rather than a complete archive or page layout. |
| Base UI forms, filters and selection controls | [coss UI, formerly Origin UI](https://coss.com/ui) | [MIT source](https://github.com/cosscom/ui); controls rather than a marketing page kit. |
| Application lists, panels, stats and framing | [Official shadcn blocks](https://ui.shadcn.com/blocks), [Blocks.so](https://blocks.so) | Useful MIT sources; adapt dashboard-oriented compositions to the actual page task. |
| A specific motion or visual accent | [Magic UI](https://magicui.design), [Cult UI](https://www.cult-ui.com), [Kokonut UI](https://kokonutui.com) | Public MIT component collections are distinct from paid blocks/templates. Evaluate added motion and dependencies. |

These are discovery leads, not a required stack or a ranking for every project. Prefer one coherent section family where useful; additional libraries should solve a concrete gap.

## Adapt the selected item

1. **Provenance:** record the item URL, source revision, license and required notices beside the project's existing third-party records. Distinguish free end-product use, OSI open source and paid source access. Inspect the actual item's terms: the survey found extra restrictions in Animate UI, React Bits and Shadcn Studio, custom terms in Aceternity/Shadcnblocks, and per-item provenance needs on 21st.dev.
2. **Compatibility:** use Context7 or official docs for current registry/CLI behavior. Inspect the payload, files and dependencies before applying changes. Match framework, React/Tailwind versions and Base UI versus Radix APIs; preserve local primitive customizations. Use the publisher's actual namespace, item name and endpoint.
3. **Integration:** adapt composition to local tokens, primitives, content and states. Account for Next.js-specific routing, images or server features. In Astro, keep static sections static and hydrate only needed interactions. Choose added dependencies and motion for an evidenced task benefit.
4. **Verification:** run the skill's applicable accessibility and project checks on the integrated result. A demo's appearance, an accessible primitive or an upstream claim does not establish the adapted page's conformance.

Done when the selected source and license are recorded, required adaptations are explicit, and the integrated result passes the applicable checks or has clearly reported limits. A discovery-only request ends with candidates and unresolved questions; installation follows the implementation scope.

## Research provenance

The YaHala repository retains the detailed survey at `docs/research/shadcn-registry-survey.md` and full directory snapshot at `docs/research/shadcn-registry-inventory.json`. The survey screened all 539 directory entries and checked a relevant shortlist; it was not a license audit of every entry. Those project artifacts are optional background. This portable reference carries the reusable decisions and primary links so other projects can use it independently.
