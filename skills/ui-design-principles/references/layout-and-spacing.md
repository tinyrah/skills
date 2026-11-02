# Layout and spacing

## Purpose

Use layout to reveal relationships and keep the task usable as available space changes. Spacing creates grouping, balance, and readable rhythm; responsive design must support the task from narrow screens to wide ones.

Bounded fluid sizing, constrained reading widths, and proportional layout can help, but their numeric values are contextual. Choose changes based on the content and observed layout behavior.

## Model: relationships first, dimensions second

Describe the content as nested groups: parts of a control, parts of an item, related items, sections, and the page. Usually, stronger relationships need less separation than weaker ones. Equal gaps everywhere can erase these relationships even when every value comes from a spacing scale.

Use the current design system and density. Operational tools, touch interfaces, reading pages, and promotional pages need different space allocation. A spacing scale limits arbitrary choices; it does not choose relationships or density. Do not introduce cards when alignment and whitespace provide sufficient grouping.

## Diagnose the failure

| Observed condition | Decision | Exception or constraint |
| --- | --- | --- |
| A label appears attached to the wrong field | Reduce within-group separation and distinguish neighboring groups. | Preserve room for validation and help text. |
| A section looks cramped | Reconsider grouping, padding, and line wrapping together. | Dense workspaces must retain efficient comparison and navigation. |
| Equal spacing looks uneven | Inspect line boxes, icon silhouettes, and control heights; apply a small optical correction. | Do not abandon shared tokens for every component. |
| A narrow viewport causes overlap | Let content wrap, grow, or change arrangement at the observed failure point. | Some two-dimensional information needs controlled overflow. |
| A wide viewport produces unreadable lines | Constrain reading width and allocate extra space intentionally. | A comparison table may use more width than prose. |
| Mobile removes necessary actions | Preserve the task with a different arrangement or accessible disclosure. | Hide redundant presentation, not indispensable functionality. |
| Every section has a border and shadow | Test whether proximity and alignment already establish groups. | A floating or independently interactive surface may need a stronger boundary. |

## Practical workflow

1. **Inspect constraints.** Read existing components, tokens, breakpoints, platforms, and real content. Identify necessary information and actions, including state messages.
2. **Establish groups.** Identify what belongs together before choosing gaps. Keep headings near their own content and secondary actions associated with the item they affect. Check the whole screen as well as individual components.
3. **Map spacing roles.** Reuse tokens for control padding, internal gaps, group separation, and page gutters. For an unconstrained new composition, start with sufficient breathing room and reduce while inspecting; retain established density in existing products.
4. **Choose intrinsic behavior.** Use the stack's layout primitives to allow wrapping, flexible tracks, and content-driven height. Constrain long reading lines. Avoid fixed widths or heights that assume one language or one ideal content length.
5. **Find transitions empirically.** Resize until a group becomes crowded or wasteful, then choose a layout change. Preserve reading and focus order. Test intermediate widths instead of validating only named device sizes.

For web implementations, flex/grid, `minmax()`, wrapping, and `clamp()` can express these decisions. Let flexible children shrink where appropriate. For native frontends, use equivalent constraints and text-scaling behavior; CSS is not a required stack.

## Responsive and localization exceptions

Do not convert every table into cards. When column comparison is the task, use an accessible, discoverable scroll region or another appropriate presentation that preserves headers and relationships. Do not conceal accidental page overflow with a blanket clipping rule.

Support logical start/end alignment and spacing. Reconsider reading order and directional icons for RTL interfaces; do not mirror every symbol. Allow translated labels and user-generated text to grow. Truncation needs access to necessary full content.

## Verification

- Inspect narrow, intermediate, and wide layouts with long content and enlarged text; check page overflow, clipped messages, and inaccessible actions.
- Use realistic empty, loading, error, and populated states. Avoid validating only balanced placeholder content.
- Check group relationships, alignment, and optical balance at normal scale. Ensure spacing changes did not reduce usable interaction targets.
- Traverse the layout by keyboard where supported; visual rearrangement must not make focus order confusing.

Record the content constraint that justified each layout transition and any deliberate overflow. Report untested viewport or localization cases explicitly.
