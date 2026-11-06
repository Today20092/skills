# Accessibility checks

Apply to the changed scope and affected states. This is a focused implementation reference, not a complete conformance checklist. Consult [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for other applicable requirements, especially forms, authentication, media, time limits and complex interactions.

| Area | Requirement and verification |
| --- | --- |
| Text contrast | [1.4.3 AA](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html): 4.5:1 ordinary text; 3:1 large text (24 CSS px regular or about 18.67 CSS px bold). Measure actual pairs including links, muted text and states; retain full precision when judging thresholds. |
| Graphics and controls | [1.4.11 AA](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html): required graphical parts and control/state cues need 3:1 against adjacent colors. Assess meaningful charts, custom controls and selected states; decorative separators have different requirements. |
| Color | [1.4.1 A](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html): convey meaning through labels, shapes or text alongside color. |
| Reflow | [1.4.10 AA](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html): vertical content works at 320 CSS px without information/function loss or two-dimensional scrolling, except genuinely two-dimensional content. Test 1280px at 400% browser zoom as well as a narrow viewport. Contain essential wide tables locally. |
| Resize | [1.4.4 AA](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html): text grows to 200% without loss. Preserve zoom and flexible containers. |
| Spacing | [1.4.12 AA](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html): tolerate simultaneous line-height 1.5×, paragraph spacing 2×, letter-spacing 0.12× and word-spacing 0.16× font size. These are override tolerances, not required defaults. |
| Targets | [2.5.8 AA](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html): 24×24 CSS px, subject to spacing, equivalent-control, inline, user-agent and essential exceptions. Prefer generous 44×44 standalone controls with separation as a usability practice. |
| Keyboard and focus | All functionality through keyboard ([2.1.1](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html)); no traps; logical order, visible focus ([2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)), and focused controls not entirely obscured by author content ([2.4.11](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)). Test overlays and sticky shells. |
| Semantics | Programmatic relationships, meaningful headings, page title and correct language. Match visual and DOM reading order; use table headers/captions and landmarks. Name controls and expose role/value/state. Accessible names include visible labels. |
| Forms | Visible associated labels, instructions and input purpose; identify errors in text with useful correction, preserve entries and announce relevant status. Check applicable error prevention, redundant entry and accessible authentication requirements in WCAG 2.2. |
| Disclosure | Prefer details/summary; custom disclosure uses a button, expanded state, associated panel and keyboard activation. [WAI pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/). |
| Hover/focus content | [1.4.13 AA](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html): applicable additional content is dismissible, hoverable and persistent. Keep equivalent essential information available without hover. |
| Pointer input | Provide alternatives to multipoint/path gestures and dragging where required; support cancellation and activation safely. Test touch without hover. |
| Charts and images | Meaningful images have appropriate text alternatives; complex charts provide a takeaway and equivalent exact values with units/periods. Hide redundant visuals only when their complete meaning is accessible elsewhere. [WAI complex images](https://www.w3.org/WAI/tutorials/images/complex/). |
| Media and motion | Check applicable caption/audio-description requirements. Auto-starting motion over five seconds alongside other content requires pause/stop/hide unless essential; auto-updating content has related controls ([2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)). Honor reduced motion as a project practice; disabling nonessential interaction animation is AAA. |

## Link recognition

Choose link cues for their context:

- **Paragraph links:** an underline is a reliable default. Another visible treatment can be valid when it meets [Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html); [G183](https://www.w3.org/WAI/WCAG22/Techniques/general/G183) describes sufficient lightness contrast for inline links. Check text/background contrast separately.
- **Navigation bars, menus and tabs:** permanent underlines are optional when grouping, placement, labels and styling make the actions recognizable before hover. Show the current/selected item with a cue beyond hue alone, such as weight, shape, a background or an underline; retain visible keyboard focus and touch targets. Hover cannot be the only cue on a touch screen.
- **Scanner warnings:** inspect the rendered context and affected states. A missing-underline warning is evidence to review, not a requirement to underline every link. Record whether the issue is a defect, a justified navigation treatment or unresolved.

Done when links are recognizable at rest, current/selected state and keyboard focus are clear, and paragraph links remain distinguishable from surrounding text in the tested themes.

Check the accessibility tree and screen-reader behavior for names, states, status announcements and reading order. Test forced colors, reduced motion and supported real mobile/assistive-technology combinations where available. Report checks unavailable separately from passes. [WAI evaluation guidance](https://www.w3.org/WAI/test-evaluate/) explains why automated checks alone do not establish conformance.
