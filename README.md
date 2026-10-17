# What I would measure before shipping an AI workflow

Grade synthetic recorded support runs against explicit outcome and authority contracts. Show a better average hiding a critical violation.

This is the runnable companion to [the article](https://subodhjena.com/blog/what-i-would-measure-before-shipping-an-ai-workflow). Website MDX is the canonical article; [article.md](article.md) is a deliberate GitHub-readable snapshot. Code and fixtures are canonical here. Research and examples updated on 17 October 2026.

## Reproduce

Python 3.11 or later, standard library only. No API keys, packages, or network access. Verified locally on Python 3.14.5.

```bash
python3 -m unittest -v
python3 evaluate.py
```

Compare stdout with [sample-output.txt](sample-output.txt). The tests exercise failure paths as well as the expected result. All fixtures are synthetic.

## Scope and limits

Six handcrafted tasks, two synthetic records per variant per task, no model executions or human-user sample. Completion-claim labels are manual fixture annotations. Events stand in for trusted harness records, not assistant assertions. Resource-level approvals are simplified to one operation inside an isolated trial. Costs and latency are invented; p95 over 12 values is the maximum. Passing the illustrative gate is not a deployment recommendation.

## Supporting material

- [Source notes](references.md), with versions and claim boundaries.
- [Recorded output](sample-output.txt).
- [Article snapshot](article.md).

The tests validate this demonstration, not production readiness. Source papers and documentation remain under their original licenses. Original example code and article text in this repository use the [MIT license](LICENSE).
