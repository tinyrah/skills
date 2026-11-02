# Decision framework

Turn a vague request into a bounded intervention. Prioritize the task, observable problems, existing constraints, and evidence over visual effects for their own sake.

## Establish a working contract

| Question | Evidence to inspect | Default when unspecified |
| --- | --- | --- |
| What must the user accomplish? | Requested flow, content, existing labels | State one plausible task and proceed |
| What defines the visual language? | Tokens, components, brand assets, neighboring screens | Reuse the existing system |
| Where must it work? | Framework, platforms, supported widths | Adapt to the current stack; cover narrow and wide layouts |
| How dense should it be? | Task frequency, information volume, input method | Preserve established density |
| How broad is the request? | Named component, screen, or system | Restrict changes to that boundary |
| What can be verified? | Running app, screenshots, tests, source access | Label unavailable evidence explicitly |

Do not create a questionnaire for a reversible adjustment. Ask when the answer would change direction, such as whether a screen is a public landing page or an operator's daily workspace. Inspect established conventions before asking the user to restate them.

## Diagnose before treating

| Observation | Cause to investigate | First intervention | Common false solution |
| --- | --- | --- | --- |
| Next action is hard to find | Competing actions or unclear labels | Clarify the action and reduce competing emphasis | Brighten every button |
| Everything feels equally important | Weak hierarchy across content roles | Rank information and adjust relative emphasis | Enlarge all headings |
| Label appears attached to the wrong field | Spacing fails to express relationships | Strengthen within-group versus between-group spacing | Add more cards |
| Panels merge into the background | Weak boundaries or missing surface roles | Adjust surface separation or a purposeful border | Shadow every panel |
| Dark surfaces look muddy | Weak lightness separation or excessive effects | Tune surfaces and quieter boundaries | Increase black shadow opacity |
| UI looks noisy | Competing colors, borders, or accents | Remove redundant emphasis | Change accent hue alone |
| Mobile feels cramped | Content has outgrown fixed geometry | Reflow at the actual failure point | Shrink all text |
| Polished button feels unclear | Missing state feedback or semantics | Repair labels, focus, loading, and errors | Add a hover animation |

Treat these as hypotheses, not diagnoses established by a screenshot alone. Inspect relevant code or interaction before changing behavior.

## Resolve tradeoffs

Prioritize task correctness and access, then organization, hierarchy and consistency, then ornament. This identifies the dominant problem; it does not require a global redesign before a local fix.

Preserve system constraints when they support the task. If an existing token makes necessary text illegible, report the conflict and propose the narrowest suitable repair. If flat surfaces already work, improve hierarchy within that language. If marketing needs stronger identity, consider display type, imagery, copy, and composition together rather than imposing application density.

Prefer one coherent change set. For a toolbar issue, adjust the toolbar and necessary tokens; do not redesign every table. For a theme-system defect, inspect shared consumers before changing a global value. A broad selector's reach is part of the design decision.

## Make decisions inspectable

Record these six items for substantial changes:

1. **Observation:** identify an element, state, or viewport.
2. **Consequence:** explain confusion, delay, or lost information.
3. **Hypothesis:** name the likely structural or visual cause.
4. **Intervention:** name the smallest useful change.
5. **Tradeoff:** identify what might become less effective.
6. **Verification:** specify a rendered, behavioral, or measured check.

Example: “In narrow checkout, the estimate has the same emphasis as the final total. Group the breakdown under the total and reduce the estimate's weight while retaining readable contrast. Verify the total and submit action remain easy to locate with a long currency string.” This is a testable hypothesis, not measured conversion improvement.

## Iterate and stop

Capture the relevant baseline, change the hypothesis under examination, inspect the result, and keep or revise it based on evidence. Stop when the requested task works, the defect is addressed, and no concrete regression remains within scope. Seek preference when viable directions differ materially in brand expression or workflow.

Do not invent beauty scores, claim user validation from self-inspection, or keep changing styles because another fashionable treatment exists. Separate uncertainty about taste from demonstrable defects.
