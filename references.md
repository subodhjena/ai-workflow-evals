# Sources and claim boundaries

Read on 17 October 2026. Links are primary papers, specifications, official documentation, or firsthand engineering accounts. Living documentation is not an archived snapshot. No claim is made that the example ran on the website archive date.

## Anthropic agent evals

- Source: [Anthropic agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).
- Version/date: 2026-01-09.
- Read: Grader types, capability/regression, nondeterminism, dataset creation, isolated environments and grader design.
- Use and limits: Outcome grading permits valid alternative paths; required authorization ordering is still a legitimate constraint. Judge calibration matters.

## tau-bench v1

- Source: [tau-bench v1](https://arxiv.org/html/2406.12045v1).
- Version/date: 2024-06-17.
- Read: Section 3 reward and pass^k definitions; construction methods and limitations.
- Use and limits: Final-state/output reward may miss required confirmation. Our both-trials count is descriptive, not a pass^k estimator from independent model samples.

## MT-Bench judge study v4

- Source: [MT-Bench judge study v4](https://arxiv.org/html/2306.05685v4).
- Version/date: 2023-12-24.
- Read: Sections 3.1 to 3.5, agreement evaluation and position-bias discussion.
- Use and limits: Position and verbosity bias observed for studied models/tasks. No current local judge accuracy follows from historical agreement percentages.

## Hamel Husain field guide

- Source: [Hamel Husain field guide](https://hamel.dev/blog/posts/field-guide/).
- Version/date: 2025-03-24.
- Read: Error analysis, bottom-up categories, data viewer, synthetic data and evaluation trust.
- Use and limits: Firsthand practitioner guidance on inspecting failures. Its client results are not ours and are not repeated as general causal evidence.

