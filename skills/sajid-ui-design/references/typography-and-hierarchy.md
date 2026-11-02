# Typography and hierarchy

## Purpose and evidence

Make the information needed for the current task easy to find and read. Sajid's [typography lesson (S6)](https://www.youtube.com/watch?v=9-oefwZ6Z74) identifies font size, weight, and color as important UI choices, and distinguishes functional interfaces from landing pages that also depend on imagery, copy, and motion. His [simplicity lesson (S8)](https://www.youtube.com/watch?v=9zt__YPULm8) emphasizes reducing user effort.

These statements were verified in creator-authored video descriptions, not complete transcripts. The procedures, examples, and starting values below are this skill's implementation guidance. See the [source register](sources.md) for attribution boundaries. The video's “80%” title is not a measured design-quality formula.

## Model: task importance becomes visual emphasis

Identify what a person needs to **notice, understand, and do** in the current state. Rank actual content before styling tags. A dashboard's exception, a search result's distinguishing attribute, and a checkout's total can deserve more emphasis than the page title. Independent work areas may each have a local focal point.

Keep document semantics and visual roles separate. Choose heading levels for the content outline; choose appearance through existing classes or tokens. Never change heading levels merely to obtain browser-default sizing. Use the project's typography, brand fonts, component library, and established density unless the task calls for changing them.

## Diagnose before changing values

| Observed condition | Decision | Exception or constraint |
| --- | --- | --- |
| Everything attracts equal attention | Rank content; quiet competing decoration and metadata before enlarging the main item. | Essential supporting text must remain readable and meet contrast requirements. |
| The page title dominates operational information | Emphasize the value, status, or result that supports the task. | An editorial headline may legitimately be the main content. |
| Many almost-identical sizes appear | Map them to a small set of existing roles and remove accidental variants. | Data labels, code, and display text can need distinct treatment. |
| Text looks crowded despite ample padding | Inspect line height, wrapping, and font metrics before adding outer space. | Compact controls need different treatment from reading paragraphs. |
| The interface feels generic | Give the product's content and typography clearer roles before adding fonts. | A brand-directed landing page may warrant a display face. |
| Text fits only with a smaller font | Reflow the layout or reconsider content presentation. | Concise secondary metadata can use a smaller role when still readable. |

## Apply the smallest coherent change

1. **Read real content.** Find the task, key labels, values, instructions, and next action. Include loading, empty, validation, and error states when relevant. Do not infer importance solely from current styling.
2. **Map roles.** Usually distinguish reading text, controls/labels, supporting text, section headings, and optional display or numeric text. Reuse project tokens; add a role only for a recurring need.
3. **Choose emphasis.** Adjust position, grouping, weight, and foreground contrast. Change size when those are insufficient. Keep equivalent roles consistent across related screens.
4. **Tune reading conditions.** Set line height and text width for the actual language and content length. Start-align extended reading content according to writing direction. Inspect font loading and fallback behavior; a different font can change wrapping and control dimensions.
5. **Inspect at normal scale.** Compare the intended reading order with what actually stands out. Zoomed-in component work can hide an unbalanced page. Change one cause at a time and preserve the surrounding system.

For a new web project without tokens, a body size around `1rem` with a unitless line height around `1.5` is a starting experiment, not a requirement or Sajid quotation. `rem` follows the root font size; `em` can follow local sizing. Avoid overriding user text preferences to preserve a screenshot.

## Verify the result

- Read the key content and identify the next action without scanning every label.
- Test long names, large values, multiline errors, translated labels, and supported writing directions. Keep text selectable and complete where the task requires it.
- Increase text size and zoom: controls, headings, and messages must reflow without clipping, overlap, or loss of necessary actions.
- Check primary and supporting text against their actual backgrounds in every supported theme; visual de-emphasis does not justify unreadable contrast.
- Verify heading structure and accessible names alongside appearance. A convincing screenshot alone does not establish usable typography.

Report which information became easier to find, which roles changed, and what you verified. If rendered inspection was unavailable, state that limitation rather than claiming visual validation.
