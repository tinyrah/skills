# Skills

Reusable Agent Skills for frontend work.

## Sajid UI Design

**A portable Agent Skill for making reasoned frontend design decisions.**

Inspired by [Sajid's public UI design teaching](https://www.youtube.com/@whosajid), this skill helps an assistant diagnose and improve hierarchy, color, depth, shadows, typography, spacing, and interaction states. It adapts to the project's users, task, platform, brand, and existing design system.

Start with the [skill instructions](skills/sajid-ui-design/SKILL.md) or inspect the [sources and provenance](skills/sajid-ui-design/references/sources.md).

## How it thinks

The workflow is a diagnostic loop:

1. **Inspect** the task, implementation, existing tokens, and rendered interface when available.
2. **Diagnose** an observed problem and its consequence for the user.
3. **Choose** an intervention that addresses the cause within the requested scope.
4. **Implement** a coherent change using the project's components and conventions.
5. **Verify** the relevant layouts, themes, states, contrast pairs, and interactions.
6. **Report** the evidence, tradeoffs, and anything still unverified.

For example, weak card hierarchy might call for clearer grouping, a surface-color adjustment, or a border. A shadow is appropriate when elevation communicates something useful. The skill asks the assistant to make that choice deliberately.

Build, refinement, audit, and shared-system work have different boundaries. An audit stays read-only unless implementation is requested; a component polish request stays focused. Existing brand and density constraints matter throughout.

## Install for GitHub Copilot

With a GitHub CLI version that supports `gh skill` (currently 2.90.0 or later), preview and install for your user account:

```bash
gh skill preview tinyrah/skills sajid-ui-design
gh skill install tinyrah/skills sajid-ui-design --agent github-copilot --scope user
```

For an explicit project installation, clone or download this repository, then copy the **entire** `skills/sajid-ui-design/` folder into your frontend project at:

```text
.github/skills/sajid-ui-design/SKILL.md
```

Keep `references/`, `scripts/`, `assets/`, and `agents/` alongside that file. Install into a supported skill location for the scope you want; a separate clone is only the source package.

See GitHub's [installation guidance](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) and [CLI reference](https://cli.github.com/manual/gh_skill_install) for supported hosts and locations.

Copilot selects skills using their description and the task. When activated, `SKILL.md` directs it to the relevant supporting files. Every reference is linked directly in the reference map; supporting documents are read progressively, rather than all being automatically injected.

## Example requests

> Use the sajid-ui-design skill to audit this dashboard. Identify the three most consequential hierarchy, color, or spacing problems. Explain the user impact and how to verify each recommendation. Keep the audit read-only.

> Use sajid-ui-design to improve this settings form. Preserve our component library, brand, and compact density. Implement the changes and check keyboard focus, errors, narrow layouts, and both themes.

> Apply sajid-ui-design to this new mobile checkout screen. Establish the information priority and action hierarchy, then cover loading, validation, and success states. Explain the design decisions and what you verified.

## Package architecture

All paths below are inside `skills/sajid-ui-design/` unless stated otherwise.

| File or group | Purpose |
| --- | --- |
| `SKILL.md` | Core workflow, scope rules, and direct routing to all ten references |
| `references/decision-framework.md` | Diagnosis, prioritization, and competing constraints |
| `references/color-and-theme.md`, `depth-and-shadows.md` | Semantic color, surfaces, themes, and purposeful elevation |
| `references/typography-and-hierarchy.md`, `layout-and-spacing.md` | Reading order, type roles, grouping, density, and reflow |
| `references/components-and-states.md` | Controls, feedback, forms, overlays, and motion |
| `references/accessibility-and-validation.md` | Evidence-based verification and accessibility checks |
| `references/implementation-patterns.md`, `worked-examples.md` | Adaptation to project conventions and practical tradeoffs |
| `references/sources.md` | Attribution, source quality, and adaptation boundaries |
| `scripts/check_contrast.py` | Dependency-free color-pair contrast calculation |
| `assets/token-starter.css`, `assets/review-template.md` | Optional original examples for tokens and review records |
| `agents/openai.yaml` | Optional metadata for compatible agent interfaces |
| Repository `.github/scripts/` and `tests/` | Structural checks and numerical/failure-case tests |

## Validation and tools

From the repository root, with Python 3:

```bash
python .github/scripts/validate_skill.py
python -m unittest discover -s tests -v
python skills/sajid-ui-design/scripts/check_contrast.py '#526071' '#FFFFFF' --minimum 4.5 --json
```

The validator checks frontmatter, direct reference routing, portable local links, heading anchors, and bundled-resource discovery. The tests exercise contrast boundaries and broken-package detection. The included GitHub Actions workflow runs both.

[Behavioral scenarios](evals/scenarios.json) cover dashboards, editorial content, dark themes, native forms, local shadow changes, and marketing pages. Run these independently with task-local evidence when revising the skill; they are manual evaluation cases, not automated proof of design quality.

The contrast checker accepts **opaque sRGB `#RGB` or `#RRGGBB` pairs**. It compares the unrounded ratio and returns `0` for a pass, `1` below the threshold, or `2` for invalid input. It does not resolve CSS variables, alpha compositing, gradients, or whole-page accessibility. Use actual rendered colors and complete the relevant interaction checks.

## Provenance, portability, and license

This is an independent adaptation, with documented first-party demos/code and available video descriptions informing the design guidance. It is not an official Sajid release, a transcript collection, or an exhaustive account of his channel. The source ledger separates that evidence from the engineering and accessibility additions.

The principles apply across frontend stacks, including native interfaces. The CSS starter demonstrates a web implementation; adapt its roles to the platform and preserve established tokens where appropriate.

Original repository text and code are available under the [MIT license](LICENSE). Linked videos, demos, and other external material retain their respective ownership and licensing; this repository does not relicense them.
