# Implementation patterns

Translate the design decisions into the existing frontend. The patterns below are framework-independent guidance; reuse project conventions rather than imposing a new architecture.

## Inspect before choosing a mechanism

Find the token definitions, component primitives, theme boundary, local overrides, style encapsulation, supported browser/platform versions, and existing test commands. Identify whether the defect is a missing role, a wrong role assignment, or a wrong value. These require different fixes: a correct global token should not change to compensate for one component using it incorrectly.

Read related consumers before editing a global token. Check theme providers and portals: a popup rendered outside a themed subtree can lose the intended values. Keep changes to business logic separate unless necessary to support the requested interaction state.

## A small semantic contract

Map existing names to these roles; do not rename a functioning system solely to match this vocabulary.

| Category | Useful roles | Question answered |
| --- | --- | --- |
| Surface | Canvas, content, raised, recessed, overlay | What layer or group does this belong to? |
| Foreground | Main, supporting, on-action, on-selection | What is readable on this surface? |
| Boundary | Essential control, decorative divider, focus | Is this a necessary edge, quiet grouping cue, or keyboard location? |
| Action | Primary, hover, pressed, disabled | What can the user do and what state is it in? |
| Feedback | Error, warning, success, information | What changed and what should the user understand? |
| Geometry | Spacing roles, radii, type roles, elevation levels | Which repeated relationships should remain consistent? |

Define component-specific aliases when shared roles cannot express a real local requirement. Avoid one-off values simply because a new screen looks different. Separate a primitive color ramp from its semantic assignments if the project already has that architecture; introducing both layers is unnecessary for a tiny isolated page.

## Adapt to the stack

| Environment | Suitable implementation |
| --- | --- |
| Plain CSS, CSS Modules, Sass | Reuse custom properties or existing variables; keep component rules scoped; change theme values at the established boundary |
| Utility-first CSS | Use the project's configured semantic utilities and supported version conventions; avoid scattering arbitrary values across every component |
| React, Vue, Svelte, server-rendered templates | Preserve existing components and data flow; express visual variants through their current props/classes; retain markup semantics |
| Component library | Prefer its theme API, documented tokens, variants, and slots; inspect overrides before fighting internals |
| React Native, SwiftUI, Compose, other native UI | Map roles to platform themes, text scaling, elevation/material, focus, and accessibility APIs; do not transplant browser CSS |
| Canvas/custom renderer | Preserve accessible equivalents and hit regions; treat pixel appearance and semantic access as separate requirements |
| Design-only artifact | Specify roles, states, layout behavior, and measurable constraints; label unimplemented behavior |

Do not add a design-system dependency to perform a border adjustment. Use native capabilities where possible. When an unfamiliar stack appears, inspect its existing implementation and primary documentation before writing version-specific code.

## Apply theme and state together

Keep semantic roles stable while assigning appropriate values independently in each supported theme. Evaluate all supported combinations that the change touches. A changed primary background may need a new on-primary foreground; selection can need both new fill and new text color.

Use the [optional token starter](../assets/token-starter.css) as an illustration, not an import mandate. It contains original example values and opt-in example component classes. It neither selects/persists a theme nor creates a complete design system. Implement system-theme preference, explicit user selection, and persistence using the host project's existing mechanism when that functionality is requested.

Do not assume a generated palette passes contrast. Inspect the final computed/composited color pairs. Use color functions only when the project's targets support them; preserve a suitable fallback when needed. Treat a decorative divider separately from a boundary required to identify a control.

## Keep the change maintainable

Make an intentional relationship reusable when it recurs: a group gap, field height, surface treatment, or focus style. Keep optical exceptions local. Avoid globally styling every `div`, `button`, or heading to fix one screen. Respect component ownership and established imports.

Validate the smallest representative consumer set that addresses the actual risk. A shared theme adjustment needs several consumers; a local label-spacing change does not require an unrelated end-to-end suite. Do not create tests that merely assert your chosen spacing constant. Test observable behavior, contrast contracts, or packaging guarantees where a regression would matter.

Explain the design decision at the appropriate level: a meaningful token name in code, a short comment for a non-obvious optical exception, and a user-facing explanation of the resulting behavior. Avoid leaving large design essays in production components.
