# Architecture

How the OpenStacks toolkits fit together — and, deliberately, how little they depend on each other.

---

## Overview

OpenStacks is **not** a platform. It is a set of independent repositories that share conventions and nothing else.

This is a correction. An earlier version of this document described a layered pipeline in which analysis repos fed a central database (RootStack), which was served by an API (BridgeStack), which was rendered by a frontend (ViewStack). That pipeline was built, and it was the most expensive part of the project to maintain and the least used. Those three repos have been [retired](../README.md#retired).

What remains is the part that always worked: five self-contained toolkits that a researcher can clone one at a time.

```
InsightStack   MEL tools, calculators, econometrics      Stata · Python · R
FieldStack     Survey design → analysis → reporting      R · Quarto
EquityStack    Data cleaning, modelling, impact eval     Python · Jupyter
PolicyStack    South Asia scheme and budget data         Python · CSV
SignalStack    Research Rundown newsletter archive       Markdown
```

No arrows. That is the architecture.

## Design principles

### Independence first
Every repo works on its own. You never need to set up more than one to use one. Clone it, read its README, run it. No repo imports from another.

### Shared conventions, not shared code
Alignment comes from convention — consistent directory structures, CSV as the default interchange format, sample data alongside every script — not from a dependency. Conventions can drift without breaking anything; dependencies cannot.

### Practitioner-facing
Built for evaluators, analysts, and programme designers, not platform engineers. Readable scripts over clever abstractions. Real sample data over fixtures. Sensible defaults over configuration.

### Reproducibility over currency
Scripts ship with sample data. Notebooks are self-contained. A repo cloned three years from now should still run — which is a reason to pin dependencies and leave them pinned, not to chase the newest version of everything.

### Boring is a feature
Stata do-files, R scripts, and Jupyter notebooks have almost no maintenance surface. They do not break when a transitive npm dependency publishes a new major version. The toolkits have survived untouched for a year precisely because they were built out of durable, unfashionable things.

## Directory conventions

Each toolkit follows roughly this structure:

```
StackName/
├── README.md
├── LICENSE
├── CITATION.cff
├── sample_data/        ← Real or realistic sample datasets
├── scripts/            ← Analysis scripts and notebooks
├── docs/               ← Repo-specific documentation
└── tests/              ← Where applicable
```

Conventions are aspirational, not enforced. Repos drift, and that is acceptable — cross-repo standardisation has been proposed more than once and finished exactly never. See [MAINTENANCE.md](../MAINTENANCE.md) for why that is now an explicit non-goal.

Details on data formats are in [DATA_STANDARDS.md](DATA_STANDARDS.md).

## Where new work goes

New projects are built as **single self-contained repositories with their own site**, not as additions to this ecosystem. [How India Lives](https://github.com/Varnasr/how-india-lives), [Dev Case Studies](https://github.com/Varnasr/dev-case-studies), and [PolicyDhara](https://github.com/Varnasr/PolicyDhara) all follow that pattern. Each reaches readers directly, carries its own deployment, and costs nothing to own when idle.

That pattern has outperformed the ecosystem model on every measure that matters: reach, maintenance cost, and the odds of the thing still working in a year.
