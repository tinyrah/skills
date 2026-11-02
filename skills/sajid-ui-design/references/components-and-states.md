# Components and states

Use this production extension when visual work affects behavior. Sajid's demos inform visual techniques; the state model below is original implementation guidance supported by [sources](sources.md).

## Define the state contract

List states the component actually supports. A static card needs no fake hover state. A control needs feedback for its supported keyboard, touch, and pointer input.

| State | Design decision | Verify |
| --- | --- | --- |
| Default | Identify purpose and availability | Label is understood without hover |
| Hover | Optional pointer feedback without layout changes | Content remains usable on touch |
| Focus-visible | Make keyboard location unmistakable | Indicator survives surrounding colors and clipping |
| Pressed/active | Show activation feedback | No layout jump or false completion |
| Selected/checked/expanded | Distinguish persistent state from hover | Semantic state and a non-color cue agree |
| Disabled | Explain unavailability when needed | Prevent action; do not merely fade a live handler |
| Loading/pending | Preserve context and indicate work | Prevent accidental duplicates where appropriate |
| Error | Identify the problem and recovery | Associate guidance with the control; retain valid input |
| Success | Confirm the intended outcome | No reliance on a disappearing color change |
| Empty | Explain the absence and next step | Distinguish first use, no results, and unavailable data |

Do not add every state to every component. Trace each to a real interaction or data condition. Visual style, programmatic state, and business behavior must agree.

## Choose the right primitive

On the web, use buttons for actions and links for navigation. Preserve meaningful visible labels and accessible names. Use native controls or established accessible components before inventing keyboard models. On native platforms, use equivalent platform controls, semantics, and focus APIs.

Keep a clear primary action within a local decision group. Independent regions can each have a primary action. Give secondary actions quieter treatment. Destructive actions need explicit wording and appropriate recovery or confirmation based on existing product behavior; do not add dialogs to harmless actions merely because they are emphasized.

Reserve interactive appearance for elements that act. Avoid raising a static card on hover if that suggests clickability. When a card contains nested actions, preserve their targets and semantics instead of wrapping everything in a competing click handler.

## Forms and feedback

Keep labels visible after entry. Put instructions before the decision and errors near their inputs. Combine error text with a visual cue; red alone is insufficient. On the web, preserve label associations and error relationships, such as `aria-invalid` and `aria-describedby`, where appropriate to the component.

During a request, keep the action's meaning readable and avoid moving surrounding content when a spinner appears. Announce relevant asynchronous changes through platform status mechanisms without announcing decorative changes. Preserve valid input after recoverable errors. Distinguish no matching results from not-yet-loaded data and network failure.

## Overlays and navigation

Reuse the project's dialog/menu primitives and their documented keyboard behavior. A modal needs a name, appropriate initial focus, contained keyboard focus while open, dismissal when appropriate, and sensible focus restoration. Test these behaviors; a shadow and high `z-index` do not implement them. Consult the [WAI-ARIA modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) for web behavior.

Keep navigation selection distinct from hover and focus. When a sidebar collapses, preserve orientation and access to destinations. Do not hide frequent actions solely to create whitespace. Treat stacking order, clipping, and visual elevation as related but separate concerns.

## Purposeful motion

Sajid's [motion guide](https://www.iamsajid.com/motion-design/) explains transforms, timing, and easing through examples. Apply that vocabulary to input feedback, continuity, spatial relationships, or deliberate identity. The production decisions here are our additions.

Use short, local feedback for frequent actions. Do not make usable controls wait for animation. Inspect performance rather than assuming every transform is free. Honor reduced-motion preferences and provide the same outcome without movement. Keep critical information available without waiting for transitions.

Verify rapid repeated input, interruption, keyboard use, and loading/error transitions. A polished default state is only one part of the component.
