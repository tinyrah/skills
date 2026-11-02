# Depth and shadows

## Purpose

Use this reference when surfaces blend together, controls lack emphasis, overlays are unclear, or an interface feels unnecessarily heavy. Depth should explain structure or interaction; it is not a required aesthetic.

**Design premise:** A tight contact shadow plus a broader soft ambient shadow can suggest elevation. Surface levels, edges, borders, and restrained highlights can communicate depth even when shadows are inappropriate. Judge the effect on the actual background.

## Mental model: separate structure from decoration

**Functional separation** explains grouping, overlap, selection, or an actionable surface. **Ornamental treatment** adds material character through a highlight, gradient, inset, or shadow. Establish functional separation first; retain ornament only if it strengthens the intended reading.

Start with content order, spacing, alignment, and surface contrast. Add borders or elevation if separation remains unclear. Flat tables, unboxed articles, and bordered forms can be appropriate. Importance and elevation are distinct: a modal must appear above its background, while a primary action can remain flat.

## Choose the smallest useful treatment

| Condition | Decision | Exception or constraint |
| --- | --- | --- |
| Related content is hard to group | Improve spacing or give the group a distinct surface | Avoid boxing every paragraph or row |
| A control cannot be identified | Strengthen its surface or necessary boundary | A decorative shadow cannot replace accessible identification |
| An overlay blends into underlying content | Establish a surface boundary and appropriate elevation/backdrop | Preserve the component library's stacking and focus behavior |
| Dark shadows disappear on a dark canvas | Distinguish surface lightness and edges | Do not make every surface luminous |
| All cards look equally important | Lower emphasis on supporting groups | Increasing every shadow preserves the problem |
| A surface should feel recessed | Consider a restrained inset treatment | Keep text and controls legible; do not imply disabled state |
| The product uses flat or dense styling | Prefer spacing, boundaries, and contrast | Add elevation only for a specific unresolved relationship |

## Application procedure

1. **Name the relationship.** Identify canvas, groups, controls, overlays, and the task's focal element. Without a functional or brand reason for depth, keep the current treatment.
2. **Try structural separation.** Compare improved spacing, a surface step, and a boundary. Choose the simplest treatment that clarifies grouping and interaction. Avoid adding shadows to every nested container.
3. **Define a small vocabulary.** Reuse existing elevation tokens. Otherwise begin with flat, modestly raised, and floating roles only as needed. Choose a consistent lighting direction for any material effects; do not mix contradictory highlights and cast shadows accidentally.
4. **Calibrate layers together.** For a raised surface, use a tighter contact shadow plus a softer ambient shadow. Tune offset, blur, spread, and opacity on the actual background. Larger blur does not automatically mean greater importance, and component size does not dictate elevation. Keep any highlight subordinate to content.
5. **Handle themes and interaction deliberately.** Dark mode may rely more on surface values and edges. Light mode may reveal subtle shadows more clearly. Add hover lift only to actual interactive elements; selected, pressed, focused, and disabled states need their own semantics. Keep keyboard focus identifiable independently of a hover effect.
6. **Inspect integration.** Check clipping by overflow, sticky regions, scroll containers, border radii, and overlays. `box-shadow` does not control stacking order; use the existing layering system. A visual change must not alter hit areas, reading order, or overlay behavior unexpectedly.

## Anti-patterns

- Solving weak typography or ambiguous actions by adding heavier shadows.
- Giving every card a gradient, glow, border, and large shadow simultaneously.
- Making a noninteractive panel lift on hover and imply a click action.
- Using `z-index` increases to compensate for shadow appearance.
- Removing focus outlines to preserve a polished surface.
- Animating expensive blur everywhere or making essential feedback depend on motion.

## Verification and stopping rule

Review the whole screen, then key controls and overlays. Confirm relationships remain clear in supported themes. Test focus, selection, hover where available, pressed states, and reduced motion if movement was added. In forced-colors modes, retain a usable boundary/focus fallback when decorative shadows disappear.

Verify no shadow is clipped unexpectedly, no overlay becomes unreadable, and no decorative treatment is the sole indicator of a required state. Compare with the simpler version. Keep the effect only when it improves grouping, priority, interaction clarity, or an explicit brand objective; stop when those aims are met.
