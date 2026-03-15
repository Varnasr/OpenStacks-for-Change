# Stack Guide

Which stack should you use? Find your use case below.

---

## By Task

### I need to analyse survey data
**FieldStack** — R notebooks for sampling, regression, cost-effectiveness, and qualitative coding. Works with KoboToolbox and ODK exports.

### I need to clean and transform development data
**EquityStack** — Python/Jupyter templates for data cleaning, modelling, and visualisation across health, gender, education, and climate datasets.

### I need MEL tools, frameworks, or calculators
**InsightStack** — Monitoring, evaluation, and learning toolkits. Includes visual frameworks, calculators, Observable notebooks, and research documentation templates.

### I need to track government policies and schemes
**PolicyStack** — South Asia policy tracker. Turns policy documents into structured, queryable data covering schemes, budgets, and implementation.

### I need to publish or archive research content
**SignalStack** — Markdown-based archive for the Research Rundown newsletter. Method spotlights, curated resources, and research tool reviews.

### I need a database for development indicators
**RootStack** — PostgreSQL and SQLite schemas, seed data, and queries. The shared data backbone for the ecosystem.

### I need an API to serve development data
**BridgeStack** — FastAPI backend that connects RootStack data to frontend applications via REST endpoints.

### I need a dashboard or data visualisation interface
**ViewStack** — Frontend UI for interactive dashboards and data exploration tools.

---

## By Language

| Language | Stacks |
|----------|--------|
| **R** | FieldStack, InsightStack |
| **Python** | EquityStack, InsightStack, BridgeStack |
| **Stata** | InsightStack, FieldStack |
| **Jupyter** | EquityStack |
| **SQL** | RootStack |
| **Markdown** | SignalStack |
| **Observable** | InsightStack |

---

## By Domain

| Domain | Start With | Also Useful |
|--------|-----------|-------------|
| **Public health** | EquityStack | FieldStack, InsightStack |
| **Education** | EquityStack | InsightStack |
| **Gender equity** | EquityStack | InsightStack, PolicyStack |
| **Climate / resilience** | EquityStack | PolicyStack |
| **Governance / policy** | PolicyStack | InsightStack |
| **General MEL** | InsightStack | FieldStack |
| **Fieldwork / surveys** | FieldStack | InsightStack |

---

## By Maturity

### Ready to use now
These stacks have real code, sample data, and documentation.

- **InsightStack** — Mature. Broad toolkit across MEL, Stata, Python, R, and Observable.
- **FieldStack** — Mature. Full lifecycle R notebooks for applied research.
- **EquityStack** — Mature. Python/Jupyter data workflows for development sectors.
- **SignalStack** — Mature. Newsletter archive and curated resources.

### Foundations in place — contributions welcome
Scaffolded with structure and initial code. Good entry points for contributors.

- **RootStack** — Database schemas and seed data.
- **BridgeStack** — FastAPI backend, early endpoints.
- **ViewStack** — Frontend scaffolding.
- **PolicyStack** — Policy tracking structure.

### On the roadmap
Planned but not yet started. If one of these matches your expertise, reach out.

- **ClimateStack** — Composite risk scores, resilience modelling, geo-spatial mapping.
- **EduStack** — Learning assessment pipelines, education outcome dashboards.
- **SocialStack** — Rapid ethnography, qualitative coding, NLP for field narratives.
- **InfraStack** — Access scoring, infrastructure mapping, spatial planning tools.

---

## Quick Decision Tree

```
What do you need?
│
├── Analysis or research?
│   ├── Survey / fieldwork data ──→ FieldStack (R)
│   ├── Data cleaning / modelling ──→ EquityStack (Python)
│   └── MEL frameworks / tools ──→ InsightStack (multi-language)
│
├── Content or knowledge?
│   ├── Policy tracking ──→ PolicyStack
│   └── Research curation ──→ SignalStack
│
└── Infrastructure?
    ├── Database ──→ RootStack
    ├── API ──→ BridgeStack
    └── Frontend ──→ ViewStack
```
