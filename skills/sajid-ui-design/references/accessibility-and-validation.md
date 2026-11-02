# Accessibility and validation

Use these production checks alongside visual judgment. They are standards-based additions, not claims about Sajid's demos. The [source ledger](sources.md) links the standards. Scope checks to the changed components and their actual dependencies; do not claim whole-product conformance from this checklist.

## Measure the right thing

| Concern | Baseline | Important distinction |
| --- | --- | --- |
| Normal text | WCAG 2.2 AA contrast of at least 4.5:1 | Supporting labels and placeholder text are still text |
| Large text | At least 3:1; large means 18 pt regular or 14 pt bold, approximately 24 or 18.67 CSS px | Do not infer this exception from a token name like `heading` |
| Essential component/state boundaries and meaningful graphics | At least 3:1 against adjacent colors | Pure decoration and inactive controls have exceptions; every decorative divider need not pass |
| Meaningful state | A cue beyond color alone | Add text, icon shape, pattern, position, or another appropriate cue |
| Keyboard focus | Visible focus; not entirely hidden by authored content | Aim for full visibility; the AA obscuration criterion itself says not entirely hidden |
| Pointer targets | At least 24 × 24 CSS px, or an applicable WCAG 2.5.8 exception | Spacing, equivalent controls, inline text, user-agent controls, and essential presentation have defined exceptions |
| Reflow | Ordinary vertically scrolling content works at 320 CSS px without loss or two-dimensional scrolling | Content requiring two-dimensional layout, such as some tables, has an exception |

For touch-heavy interfaces, a larger target such as 44 × 44 CSS px can be a useful design goal; do not mislabel it as the universal AA minimum. Check the actual clickable area, not the icon alone. Do not invoke an exception without establishing that it applies.

## Check contrast in context

Collect the resolved foreground and its actual adjacent background for each relevant theme and state. Check body text, supporting text, action labels, selected content, error text, focus cues, and meaningful icons. Hover or selected backgrounds can invalidate an otherwise good foreground.

Use the bundled [contrast checker](../scripts/check_contrast.py) for opaque sRGB hex pairs. Its numerical pass is only about the supplied pair and threshold. For alpha colors, gradients, images, blending, filters, or other color spaces, inspect the rendered/composited colors with appropriate tooling; do not feed unresolved token strings to the script or assume one sample covers the whole element. HSL or OKLCH lightness differences are not WCAG contrast ratios. Compare unrounded ratios with the requirement.

## Exercise behavior

Use keyboard navigation through the affected flow. Check visible focus, logical order, operation, dismissal, and return focus. Inspect sticky headers, footers, overflow containers, and dialogs for obscured focus. Confirm visual selection matches semantic selection. Retain names, labels, instructions, and status announcements.

Check long content, enlarged text, and relevant language/reading direction. On web layouts, inspect narrow reflow and an appropriate zoom test; test 200% text enlargement and 400% zoom where applicable, not just a single mobile screenshot. A large font cap or fixed-height container can clip content even when the default viewport looks correct.

Honor reduced-motion preferences for motion you add. Confirm the same task outcome without movement. In forced-colors/high-contrast modes, verify essential boundaries and focus remain perceivable when shadows or background fills disappear. Use platform equivalents for native applications.

## A proportional verification plan

| Change | Minimum meaningful evidence |
| --- | --- |
| Text or color adjustment | Actual computed pairs, affected states/themes, rendered readability |
| Spacing or typography adjustment | Narrow and wide layouts, long labels, enlargement, task grouping |
| Shared surface/shadow token | Representative consumers, nested layers, both supported themes, clipped/floating surfaces |
| Interactive component | Relevant state matrix, keyboard operation, semantics, touch behavior where supported |
| New screen | Main task flow, empty/loading/error/success as relevant, responsive layout, project build checks |

Choose widths around observed layout transitions as well as a narrow and wide example. Do not build a huge matrix unrelated to the change. Reuse the project's test and screenshot facilities before adding tools. Automated accessibility checks can find some defects; manual visual and keyboard checks remain necessary for the behaviors above.

## Report evidence honestly

Separate these categories:

- **Passed:** name the check, scope, and observed result; include ratio or viewport/state where useful.
- **Failed:** identify the concrete defect and whether it was corrected and rechecked.
- **Not checked:** explain unavailable rendering, browser, device, data, or interaction access.

Source inspection can verify that a focus rule exists, not that the focus is visible in every rendered state. A screenshot can show clipping, not prove a dialog traps focus correctly. A successful build proves neither visual quality nor accessible interaction. If no browser is available, deliver the implementation and a concise list of remaining visual/behavioral checks instead of fabricating a pass.
