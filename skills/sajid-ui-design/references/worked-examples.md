# Worked examples

These hypothetical exercises illustrate this skill's original implementation guidance. They are not Sajid's case studies or measured usability results. See [sources and provenance](sources.md) for the evidence. Adapt decisions to the repository and task; these are not visual presets.

## 1. Dense enterprise dashboard with an established dark theme

**Observation.** An operations dashboard uses an approved brand palette and compact table library. In dark mode, a floating filter menu blends into the table, selected rows resemble hovered rows, and a decorative summary panel attracts more attention than actionable exceptions. Preserve brand and density.

**Diagnosis.** Surface relationships and information priority are unclear. Making every panel brighter, larger, or more spacious would not address the specific ambiguity and could reduce useful comparison space.

**Decisions.** Retain compact rows, table semantics, brand colors, and existing type roles. Give the menu the project's floating-surface treatment, inspecting its boundary against both nearby surfaces. Separate selection from hover with a persistent indicator and appropriate semantics. Reduce the summary panel's competing emphasis; reinforce exceptions with text or icons as well as color. Preserve deliberate horizontal table scrolling where column comparison requires it.

**Exceptions.** A brand token that fails required contrast needs an explicit accessible treatment, not silent acceptance. Change shared tokens only if all consumers should receive the change. A lighter surface does not determine stacking order or justify raising every panel.

**Verification.** Inspect both themes, open menus, selection, hover, and focus. Measure relevant contrast pairs and exercise table navigation. Confirm long values remain available and the same operational tasks remain possible at narrower widths.

Read [color and theme](color-and-theme.md), [depth and shadows](depth-and-shadows.md), and [typography and hierarchy](typography-and-hierarchy.md).

## 2. Flat documentation interface that feels difficult to read

**Observation.** A documentation page is described as plain. It has wide centered paragraphs, weak section grouping, and a navigation area that competes with article headings. Its flat visual language is intentional.

**Diagnosis.** Reading geometry and hierarchy need attention. Adding a card and shadow around each section would create more boundaries without necessarily improving navigation or comprehension.

**Decisions.** Preserve the flat style. Start-align prose according to writing direction, constrain its measure, and associate headings more clearly with their sections. Reuse established heading and body roles. Reduce unnecessary navigation emphasis while retaining a clear current location. Give code and callouts appropriate typography and grouping; make long code examples independently scrollable when required.

**Exceptions.** A diagram or comparison table can legitimately need more width than prose. Do not shrink code until it fits or truncate information necessary to follow an example. A marketing introduction may use a different treatment from the reading area if its purpose warrants it.

**Verification.** Inspect the document outline, long paragraphs, nested lists, code, and supported languages. Check text enlargement, anchor navigation, visible focus, and narrow layouts. Ensure the page remains understandable without added elevation.

Read [typography and hierarchy](typography-and-hierarchy.md) and [layout and spacing](layout-and-spacing.md).

## 3. New marketing page for a real product

**Observation.** An early page contains a generic promise, centered text, interchangeable feature cards, and a large decorative gradient. It does not show what the product does. No established design system exists yet.

**Diagnosis.** The main weakness is an unclear product proposition and insufficient evidence. More effects would amplify an undifferentiated message.

**Decisions.** Clarify the audience, specific benefit, and next action using supplied facts. Show a real product screen, honest example, or feasible demonstration. Establish readable body typography and a deliberate display role that fits the product's character. Use a restrained palette with clear action and supporting roles. Choose a layout around the actual product evidence; introduce variation only where it improves the story. Build a small reusable token set for the page.

**Exceptions.** A marketing page can use expressive typography, imagery, and motion that would be distracting in the product's daily workflow. This does not require a bento grid, animated hero, or multiple typefaces. Never fabricate customer logos, testimonials, metrics, or working demo functionality to complete the composition.

**Verification.** Check that mobile visitors can understand the product and reach the intended action. Verify factual copy, working links, focus, contrast, text wrapping, and any reduced-motion behavior. Report design rationale without claiming higher conversion before measurement.

Read [decision framework](decision-framework.md), [typography and hierarchy](typography-and-hierarchy.md), and [components and states](components-and-states.md).

## 4. Small mobile form in React Native, including offline errors

**Observation.** A native settings form clips translated labels at larger text sizes. The keyboard covers its save action. A failed network request clears edited values and leaves an unexplained disabled button.

**Diagnosis.** The form has layout and recovery failures. Visual polish cannot compensate for lost input or ambiguous save status.

**Decisions.** Use existing native components and theme roles. Allow labels and messages to grow, group fields by task, and use platform-appropriate keyboard avoidance and safe-area handling. Retain entered values after failure. Identify invalid fields with understandable text, maintain persistent labels, and provide suitable accessibility announcements. Make the offline state explicit and offer an honest recovery path. Represent pending, successful, and failed saves distinctly.

**Exceptions.** Do not invent offline persistence or queued synchronization when the application has no such capability. If queuing exists, distinguish “saved locally” from server confirmation. Follow platform accessibility and text-scaling APIs; translating CSS values mechanically is unnecessary. Avoid automatic retries that could duplicate consequential submissions.

**Verification.** Test enlarged text, long translations, keyboard visibility, assistive navigation, offline submission, and recovery. Confirm values survive failure and completion feedback matches the actual persistence state. Check both themes; messages must not depend on color alone.

Read [layout and spacing](layout-and-spacing.md), [components and states](components-and-states.md), and [implementation patterns](implementation-patterns.md).

## 5. A local shadow refinement in an existing application

**Observation.** The user asks for a softer shadow on one popover. It already has an established surface role and functioning interactions. Its current shadow feels heavy against a light canvas.

**Diagnosis.** This is a limited elevation adjustment. Keep the intervention within the requested popover and necessary dependencies.

**Decisions.** Inspect the component's existing token and consumers. Choose an appropriate existing elevation level or introduce the smallest justified local variant. Balance contact definition and diffuse shadow without obscuring nearby content. Preserve the surface boundary, focus indication, placement, and interaction behavior. Check the dark-theme counterpart independently instead of applying a mechanical inversion.

**Exceptions.** A shared token is the right change only when its other consumers should also soften. If clipping or a stacking context causes the visible defect, fix that cause rather than increasing blur or opacity. A border may provide clearer separation on dark surfaces.

**Verification.** Compare the popover before and after against actual surrounding surfaces, including viewport edges and scrolling containers. Exercise open, close, and keyboard focus behavior. Inspect supported themes and run the relevant existing checks; avoid expanding a local refinement into an unrelated redesign.

Read [depth and shadows](depth-and-shadows.md) and [accessibility and validation](accessibility-and-validation.md).
