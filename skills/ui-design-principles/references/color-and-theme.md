# Color and theme

## Purpose

Use this reference when choosing, repairing, or extending a palette, changing themes, or diagnosing weak visual hierarchy. Preserve the project's brand and existing token contracts.

**Design premise:** Treat color as a set of semantic relationships among canvases, surfaces, text, borders, actions, and feedback—not a collection of isolated swatches. The roles, procedures, and examples below are adaptable choices, not universal palette values.

## Mental model: assign a job before choosing a color

Color establishes readability, communicates relationships, and expresses identity. One value can serve compatible roles, but actions, errors, and decoration must remain distinguishable. Name tokens by purpose, such as `surface-raised`, `text-secondary`, or `action-background`; adapt these names to the repository instead of introducing a parallel system.

Keep structural hierarchy understandable without hue. A quieter secondary label still needs to be readable. A brand color is a starting constraint, not an automatic choice for every button background, chart series, or status message.

## Decide from the observed problem

| Condition | Decision | Exception or constraint |
| --- | --- | --- |
| Everything competes for attention | Reduce secondary emphasis and saturated surface area; reserve strongest emphasis for the current task | Multiple urgent statuses may need simultaneous prominence |
| Panels blend into the canvas | Adjust related surface values or add a boundary | An editorial layout may need only spacing |
| A brand color makes small text hard to read | Choose an accessible role-specific variant or pair it with a suitable foreground | Do not silently replace mandated brand assets |
| Dark mode feels muddy | Separate surface levels and foregrounds independently | Existing platform/theme conventions take precedence |
| State is conveyed only by hue | Add text, a check, icon, underline, or shape with appropriate semantics | Decorative color need not carry a redundant message |
| A chart needs many categories | Use a dedicated data palette plus labels/patterns | Do not force every category into the interface accent |

## Application procedure

1. **Inventory what exists.** Find theme providers, CSS variables, component variants, chart colors, and current contrast failures. Reuse working semantic roles; change the smallest coherent set of values.
2. **Map the roles.** Identify canvas, ordinary surface, raised surface if needed, primary/secondary text, necessary boundaries, focus, actions, and applicable statuses. Define foreground/background pairs, not isolated swatches. Separate destructive actions from general brand emphasis.
3. **Establish reading hierarchy.** Give primary content sufficient contrast first. Make supporting content quieter through weight, size, placement, or color while retaining legibility. Muted does not mean disabled; placeholders and helper text are still readable content.
4. **Choose controlled variation.** Use the project's color space. If creating a new ramp, a perceptual space can help organize changes, but inspect the result and measure actual contrast. HSL lightness and OKLCH lightness are not WCAG contrast ratios. Avoid copying a demonstration's numeric ramp as a universal recipe.
5. **Resolve each supported theme.** Retain role meanings while choosing mode-specific values. Do not apply literal numeric inversion. Test raised surfaces, selected controls, links, alerts, charts, and foregrounds separately. Follow the existing theme preference and persistence mechanism; do not add another toggle unnecessarily.
6. **Validate actual compositions.** Check the rendered foreground against its actual adjacent background, including transparency, imagery, gradients, disabled styling, and interaction states. Review the least favorable background behind text. Honor the project's supported browsers and color fallback policy.

## Anti-patterns

- Adding a new hex value for every local mismatch instead of repairing a shared role.
- Lowering opacity across a whole component, unintentionally weakening text and controls.
- Treating an arbitrary percentage split or fixed palette size as a requirement.
- Assuming changing only the canvas produces a complete dark theme.
- Using low-contrast gray to make required information appear “premium.”
- Reusing one saturated token indiscriminately for brand, warning, selection, and focus.

## Verification and stopping rule

Check representative content in every supported theme and relevant state. Under WCAG AA, ordinary text requires 4.5:1 and qualifying large text 3:1; [W3C defines the exceptions and large-text criteria](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). Necessary control/state indicators have [non-text contrast requirements](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html); decorative separators are a different case.

Confirm selected state, focus, error, and success remain understandable without hue alone. Record the actual pairs and checks performed; do not report measured compliance from visual inspection. Stop when reading order and semantic distinctions are clear, the tested pairs meet the project's requirements, and further palette changes would be preference rather than a demonstrated improvement.
