# Stack Guide

Which repository should you use? Find your use case below.

All five toolkits are **Stable** — usable and correct, not under active development. See [MAINTENANCE.md](../MAINTENANCE.md) for what that means.

---

## By task

### I need to analyse survey data
**[FieldStack](https://varnasr.github.io/FieldStack/)** ([source](https://github.com/Varnasr/FieldStack)): R for the checks a survey team runs while data is being collected, and for sample size, weights and design-based estimates after. Reads ODK, KoBo and SurveyCTO exports.

### I need to clean and transform development data
**[EquityStack](https://varnasr.github.io/EquityStack/)** ([source](https://github.com/Varnasr/EquityStack)): inequality measurement and design-based survey estimation in Python, plus cleaning, modelling and visualisation modules.

### I need MEL tools, frameworks, or calculators
**[InsightStack](https://varnasr.github.io/InsightStack/)** ([source](https://github.com/Varnasr/InsightStack)): MEL calculators, loaders for DHS and PLFS microdata, validation and labelling tools, and templates for evaluation documents.

### I need to run an impact evaluation
**[InsightStack](https://varnasr.github.io/InsightStack/)** for the econometrics module (DiD, PSM, IV/2SLS, RDD, sensitivity analysis) in Python and R. **[EquityStack](https://varnasr.github.io/EquityStack/)** has a Python-only version (DiD, PSM, RDD) and the survey estimation the intervals depend on.

### I need to track government policies and schemes
**[PolicyDhara](https://github.com/Varnasr/PolicyDhara)**, which updates itself. PolicyStack, the earlier static dataset, is retired.

### I need practice data to teach or learn with
**[DevData Practice](https://github.com/Varnasr/devdata-practice)** — 10 generators, 350k+ rows of realistic development data.

### I need teaching material or case studies
**[Dev Case Studies](https://github.com/Varnasr/dev-case-studies)** (200 cases, 117 countries) and **[Development Discourses](https://github.com/Varnasr/development-discourses)** (500+ curated open-access sources).

### I need Indian state-level data or maps
**[How India Lives](https://github.com/Varnasr/how-india-lives)** — 205 state-level choropleth maps across demography, health, gender, economy, education, and environment.

### I need to publish or archive research content
**[SignalStack](https://varnasr.github.io/SignalStack/)** ([source](https://github.com/Varnasr/SignalStack)): the Research Rundown newsletter archived in full, its recurring sections compiled, and four scripts from its methods notes.

---

## By language

| Language | Repositories |
|----------|--------------|
| **R** | FieldStack, InsightStack, [DevEconomics Toolkit](https://github.com/Varnasr/deveconomics-toolkit) |
| **Python** | EquityStack, InsightStack, [DevData Practice](https://github.com/Varnasr/devdata-practice) |
| **Stata** | InsightStack, FieldStack |
| **Jupyter** | EquityStack |
| **Quarto** | FieldStack |
| **Observable** | InsightStack |
| **Markdown** | SignalStack |

---

## By domain

| Domain | Start with | Also useful |
|--------|-----------|-------------|
| **Public health** | EquityStack | FieldStack, InsightStack |
| **Education** | EquityStack | InsightStack, Dev Case Studies |
| **Gender equity** | EquityStack | InsightStack |
| **Climate / resilience** | EquityStack | [JanVayu](https://www.janvayu.in) for air quality |
| **Governance / policy** | [PolicyDhara](https://github.com/Varnasr/PolicyDhara) | InsightStack |
| **General MEL** | InsightStack | FieldStack |
| **Fieldwork / surveys** | FieldStack | InsightStack |

---

## Quick decision tree

```
What do you need?
│
├── To analyse something
│   ├── Survey / fieldwork data ──→ FieldStack (R)
│   ├── Cleaning / modelling ─────→ EquityStack (Python)
│   ├── Impact evaluation ────────→ InsightStack (Python, R)
│   └── MEL frameworks ───────────→ InsightStack (multi-language)
│
├── Data to work with
│   ├── Practice datasets ────────→ DevData Practice
│   ├── Indian state indicators ──→ How India Lives
│   └── Schemes and budgets ──────→ PolicyDhara
│
└── To read or teach
    ├── Case studies ─────────────→ Dev Case Studies
    ├── Literature ───────────────→ Development Discourses
    └── Newsletter archive ───────→ SignalStack
```

---

## Retired

**RootStack** (database schemas), **BridgeStack** (FastAPI backend), **ViewStack** (React dashboard) and **PolicyStack** (replaced by PolicyDhara) are archived and read-only. They formed a data → API → dashboard pipeline that the toolkits above never depended on. If you were looking for a database of Indian development indicators, [How India Lives](https://github.com/Varnasr/how-india-lives) and [PolicyDhara](https://github.com/Varnasr/PolicyDhara) are the maintained alternatives.
