# Stack Guide

Which repository should you use? Find your use case below.

All five toolkits are **Stable** — usable and correct, not under active development. See [MAINTENANCE.md](../MAINTENANCE.md) for what that means.

---

## By task

### I need to analyse survey data
**[FieldStack](https://github.com/Varnasr/FieldStack)** — R notebooks for sampling, sample size, sampling weights, complex survey analysis, regression, cost-effectiveness, and qualitative coding. Works with KoboToolbox and ODK exports.

### I need to clean and transform development data
**[EquityStack](https://github.com/Varnasr/EquityStack)** — Python/Jupyter templates for cleaning, modelling, and visualisation across health, gender, education, and climate datasets. Includes a data-cleaning pipeline with automatic logging.

### I need MEL tools, frameworks, or calculators
**[InsightStack](https://github.com/Varnasr/InsightStack)** — Monitoring, evaluation, and learning toolkits: visual frameworks, calculators, Observable notebooks, and research documentation templates.

### I need to run an impact evaluation
**[InsightStack](https://github.com/Varnasr/InsightStack)** for the full econometrics module (DiD, PSM, IV/2SLS, RDD, sensitivity analysis) in Python and R. **[EquityStack](https://github.com/Varnasr/EquityStack)** has a lighter Python-only version (DiD, PSM, RDD).

### I need to track government policies and schemes
**[PolicyDhara](https://github.com/Varnasr/PolicyDhara)** for current work — it auto-updates and is actively developed. **[PolicyStack](https://github.com/Varnasr/PolicyStack)** holds the original static dataset: 15 flagship schemes with four years of budget data.

### I need practice data to teach or learn with
**[DevData Practice](https://github.com/Varnasr/devdata-practice)** — 10 generators, 350k+ rows of realistic development data.

### I need teaching material or case studies
**[Dev Case Studies](https://github.com/Varnasr/dev-case-studies)** (200 cases, 117 countries) and **[Development Discourses](https://github.com/Varnasr/development-discourses)** (500+ curated open-access sources).

### I need Indian state-level data or maps
**[How India Lives](https://github.com/Varnasr/how-india-lives)** — 205 state-level choropleth maps across demography, health, gender, economy, education, and environment.

### I need to publish or archive research content
**[SignalStack](https://github.com/Varnasr/SignalStack)** — Markdown archive for the Research Rundown newsletter: method spotlights, curated resources, tool reviews.

---

## By language

| Language | Repositories |
|----------|--------------|
| **R** | FieldStack, InsightStack, [DevEconomics Toolkit](https://github.com/Varnasr/deveconomics-toolkit) |
| **Python** | EquityStack, InsightStack, PolicyStack, [DevData Practice](https://github.com/Varnasr/devdata-practice) |
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
| **Governance / policy** | [PolicyDhara](https://github.com/Varnasr/PolicyDhara) | PolicyStack, InsightStack |
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

**RootStack** (database schemas), **BridgeStack** (FastAPI backend), and **ViewStack** (React dashboard) are archived and read-only. They formed a data → API → dashboard pipeline that the toolkits above never depended on. If you were looking for a database of Indian development indicators, [How India Lives](https://github.com/Varnasr/how-india-lives) and [PolicyDhara](https://github.com/Varnasr/PolicyDhara) are the maintained alternatives.
