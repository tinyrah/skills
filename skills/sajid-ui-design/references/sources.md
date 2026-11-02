# Sources and provenance

Research date: **2026-11-02**.

This is an independent, original adaptation of selected public teaching materials by [Sajid / @whosajid](https://www.youtube.com/@whosajid), combined with accessibility standards and engineering judgment. It is not affiliated with or endorsed by Sajid. It does not claim to cover his entire channel or to reproduce a course.

## How to interpret the evidence

Creator-authored pages and demo source code provide the strongest inspected evidence for detailed visual techniques. Some video entries were available only as titles, metadata, or creator-authored descriptions. Those entries support only the narrow topic or statement identified below. Full video transcripts and frame-by-frame demonstrations were not verified; no exact narration or timestamps are asserted. Third-party transcript text is not included or used as the authority for detailed rules.

The skill's diagnosis workflow, decision tables, exceptions, token names and values, scripts, framework guidance, review checklist, and production verification procedures are original implementation synthesis. They are not Sajid quotations or universal numerical prescriptions. External demos illustrate techniques; their presence here does not certify their complete accessibility or production behavior. This repository's examples are independently written, not copies of those applications.

## Sajid source register

| ID and source | Evidence actually inspected | Used for |
| --- | --- | --- |
| **S1 — [UI Colors](https://www.iamsajid.com/ui-colors/)** | Creator's tool page, role labels, explanatory text, and links to source | Semantic palette roles; contrast, surface, and depth vocabulary |
| **S2 — UI Colors: [script.js](https://github.com/whosajid/UI-Colors/blob/cb8f1d0cd05e3ff27a5d603d837cf534654bef5e/script.js) and [style.css](https://github.com/whosajid/UI-Colors/blob/cb8f1d0cd05e3ff27a5d603d837cf534654bef5e/style.css)** | Source at immutable commit `cb8f1d0cd05e3ff27a5d603d837cf534654bef5e` | Related surfaces, independent themes, foreground roles, layered shadows, edge highlights, and optional gradients |
| **S3 — [CSS Tricks](https://www.iamsajid.com/css-tricks/) / [Better Shadows](https://codepen.io/whosajid/pen/QWReYqV)** | Creator's index and linked demo markup/styles | Tight contact and larger soft shadow layers |
| **S4 — [The Easy Way to Pick UI Colors](https://www.youtube.com/watch?v=vvPklRN0Tco)** | Official video metadata and description | Further learning; detailed color guidance is supported by S1–S2 |
| **S5 — [The Easy Way to Fix Boring UIs](https://www.youtube.com/watch?v=wcZ6jSlZqDc)** | Video page and expanded creator description; full transcript unavailable | Further learning on depth; detailed techniques are supported by S2–S3 |
| **S6 — [The 80% of UI Design - Typography](https://www.youtube.com/watch?v=9-oefwZ6Z74)** | Creator-authored video description | Size, weight, and color as typographic choices; functional UI versus broader landing-page needs |
| **S7 — [The Easy Way to Pick Perfect Spacing](https://www.youtube.com/watch?v=-O1ds-kPUZg)** | Creator-authored video description | Spacing for grouping, balance, and readability |
| **S8 — [The Golden Rule of UI Design](https://www.youtube.com/watch?v=9zt__YPULm8)** | Creator-authored video description | Reducing the effort required to use an interface |
| **S9 — [The Easy Way to Build Responsive Websites](https://www.youtube.com/watch?v=l04dDYW-QaI)** | Creator-authored video description | Considering a broad device range |
| **S10 — [Dynamic Sizes](https://codepen.io/whosajid/pen/jOoyqBW)** | Creator's demo source | Bounded fluid sizing, constrained containers, and proportional layout |
| **S11 — [Motion Design](https://www.iamsajid.com/motion-design/)** | Creator's guide text and code examples | Transform, timing, and easing vocabulary |
| **S12 — [Better Lists](https://codepen.io/whosajid/pen/XWwpdoE)** | Creator's demo markup/styles | Supporting examples of structured list presentation |
| **S13 — [Color Generator](https://www.iamsajid.com/colors/)** | Creator's page and displayed color variables | Background reading on restrained palettes; not an exact four-color requirement |

S4–S9 are linked for traceability and further learning, with their evidence limits preserved. They are not substitutes for inspecting the source when extending attribution. Numeric values in demonstrations are contextual examples. Retest any values selected for a real product.

## Accessibility and implementation authorities

These support the skill's engineering additions. Accessibility requirements are not attributed to Sajid. The W3C Understanding pages explain individual criteria; the [WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/) is the normative standard.

| Authority | Used for |
| --- | --- |
| [W3C: Contrast (Minimum), 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | Text contrast thresholds, exceptions, and large-text criteria |
| [W3C: Non-text Contrast, 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) | Necessary control/state indicators and meaningful graphics |
| [W3C: Use of Color, 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) | Information that must not depend on hue alone |
| [W3C: Focus Visible, 2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html) | Visible keyboard focus |
| [W3C: Focus Not Obscured (Minimum), 2.4.11](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html) | Focused components and author-created obscuring content |
| [W3C: Target Size (Minimum), 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) | Pointer target sizing, spacing alternatives, and exceptions |
| [W3C: Reflow, 1.4.10](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) | Responsive reading and task preservation under constrained width |
| [WAI-ARIA APG: Modal Dialog Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) | Dialog naming, keyboard interaction, and focus management |
| [MDN: prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) | Adapting movement to a user's motion preference |

The contrast helper checks declared color pairs within its documented input limits. It does not certify a page, inspect all rendered states, or replace keyboard and visual verification. CSS examples and platform adapters must be checked against the target project's supported environments.

## Skill format and packaging sources

| Source | Used for |
| --- | --- |
| [Agent Skills specification](https://agentskills.io/specification) | Frontmatter, directory conventions, progressive loading, and relative reference paths |
| [GitHub: Adding agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) | Copilot skill discovery, supporting resources, and project installation guidance |
| [VS Code: Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills) | Editor-specific discovery and relative resource references |
| [GitHub CLI: gh skill install](https://cli.github.com/manual/gh_skill_install) | Skill package discovery and installation commands |
| [Feature-Sliced Design example skill](https://github.com/feature-sliced/skills/tree/master/feature-sliced-design) | User-provided structural reference: concise entry point and linked supporting files; no UI-design authority or copied instructional content |

Discovery depends on the installed agent and its version. Listing every reference directly in `SKILL.md` makes resources discoverable; it does not mean every file is loaded into context automatically. Follow the entry point's read conditions and preserve the complete skill directory when installing.

## Maintaining this register

When extending the skill, record the actual evidence inspected and distinguish a source's teaching from new implementation advice. Prefer creator-authored material and stable source permalinks. Update the research date and relevant entries when evidence changes. Do not upgrade a title-only or description-only entry into a transcript-backed claim without verifying the additional material.
