<p align="center">
  <img src="banner/openstacks_banner.png" alt="OpenStacks for Change" width="700">
</p>

<h1 align="center">OpenStacks for Change</h1>

<p align="center">
  <strong>An index of open-source work on development research, data, and policy.</strong><br>
  Built in India. Shared for impact.
</p>

<p align="center">
  <a href="https://openstacks.dev"><img src="https://img.shields.io/badge/Website-openstacks.dev-0984e3?style=flat-square" alt="Website"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-00b894?style=flat-square" alt="License: MIT"></a>
  <a href="MAINTENANCE.md"><img src="https://img.shields.io/badge/Maintenance-policy-6b7280?style=flat-square" alt="Maintenance policy"></a>
</p>

---

## What this is

This repository is an **index**, not a product. It hosts [openstacks.dev](https://openstacks.dev) and points to the open-source repositories behind my work in development economics, evaluation, and public-interest data.

It began in 2025 as the hub for a family of eight interlocking "stacks." Some of those are still genuinely useful and still here. Others were scaffolding for an ecosystem that never needed to exist, and they have been retired. The sections below say plainly which is which.

If you are looking for the polished, reader-facing version of this work, start with the platforms — not this repo.

## Start here

| | | |
|---|---|---|
| **[Impact Mojo](https://www.impactmojo.in)** | Teaching and practice platform for development economics and social research. | [repo](https://github.com/ImpactMojo/ImpactMojo) |
| **[JanVayu](https://www.janvayu.in)** | जनवायु — a citizen-led national archive of India's air quality crisis. | [repo](https://github.com/JanVayu/JanVayu) |
| **[openstacks.dev](https://openstacks.dev)** | This index — the code behind the above, plus the research toolkits. | you are here |

---

## Projects

### Data and policy

| Project | What it is |
|---|---|
| **[PolicyDhara](https://policydhara.impactmojo.in)** | [Source](https://github.com/Varnasr/PolicyDhara) · Auto-updating tracker of Indian government policy across development sectors. A complement to Impact Mojo. |
| **[How India Lives](https://howindialives.impactmojo.in)** | 259 state-level choropleth maps and 10 visual stories on India's diversity across demography, health, gender, economy, education, and environment, with an interactive map of 106 indicators. [Source](https://github.com/Varnasr/how-india-lives). |
| **[Some Perspective](https://someperspective.info)** | Unfunded empirical study of India's political economy, 2004–2026. Three constructed indices, full dataset, replication code, and a working paper. |
| **[Hyderabad Electoral Analysis](https://varnasr.github.io/Hyderabad-Electoral-Analysis/)** | Five old-city seats, one winner since 1999 — and still the poorest part of Hyderabad. Ward-level census analysis showing the gap is in work and income, not services or slums. [Source](https://github.com/Varnasr/Hyderabad-Electoral-Analysis). |
| **[Bihar Parichay](https://bihar-parichayproject.netlify.app)** | [Source](https://github.com/Varnasr/BiharParichay-Project) · Interactive bilingual resource on Bihar — society, economy, caste, migration, climate, culture. Single offline-capable HTML file. |
| **[Off the Roll](https://offtheroll.in)** | [Source](https://github.com/Varnasr/INDIA-DATA) · Who was struck off India's electoral rolls in the 2025-26 Special Intensive Revision: across India, in Bihar, in five Old City constituencies of Hyderabad, and in Tamil Nadu, Karnataka, West Bengal and Kerala. |
| **[SDG Progress Tracker](https://sdgtracker.impactmojo.in)** | [Source](https://github.com/Varnasr/sdg-progress-tracker) · India's progress on all 17 UN Sustainable Development Goals — scores, trends, radar charts, and category breakdowns. |
| **[India Development Indicators](https://devindicators.impactmojo.in)** | [Source](https://github.com/Varnasr/india-development-indicators) · Interactive dashboard across economic, health, education, infrastructure, and environmental indicators, pulling live from the World Bank Open Data API. |
| **[Climate TRACE India](https://climatetrace.impactmojo.in)** | [Source](https://github.com/Varnasr/climate-trace-india) · Satellite-verified, facility-level greenhouse-gas emissions for India — power, manufacturing, transport, fossil fuels, agriculture, and waste, including the top-emitting coal and steel plants. |
| **[Industry Conglomerates Tracker](https://industrygroups.impactmojo.in)** | [Source](https://github.com/Varnasr/industry-conglomerates-database) · Open geographic database of 386 major Adani and Ambani infrastructure projects, 1998–2026 — searchable and filterable, with government-support classification. |
| **[WhoGaveTheOrder.in](https://www.whogavetheorder.in/)** | Citizen-led accountability archive asking who authorised the use of state power against citizens. A six-state evidence grammar, a page for each incident, an evidence library, a calendar of court hearings and committee sittings, letters asking offices to preserve their records, and a log of what has been asked of public offices. [Source](https://github.com/Varnasr/whogavetheorder). |

### Teaching and practice

| Project | What it is |
|---|---|
| **[Dev Case Studies](https://varnasr.github.io/dev-case-studies/)** | [Source](https://github.com/Varnasr/dev-case-studies) · 208 real development case studies from 117 countries — searchable, filterable, fully cited. |
| **[Development Discourses](https://devdiscourses.impactmojo.in/)** | Curated library of 687 research papers, books, and grey literature for practitioners in South Asia, open access first. [Source](https://github.com/Varnasr/development-discourses). |
| **[DevData Practice](https://github.com/Varnasr/devdata-practice)** | Realistic practice datasets — 36 generators, 840,000+ rows. |
| **[DevEconomics Toolkit](https://github.com/Varnasr/deveconomics-toolkit)** | 11 interactive Shiny apps, six in Python and five in R, for impact evaluation, poverty analysis, and program design. |
| **[ImpactLex](https://www.impactmojo.in/impactlex/)** | Development-sector glossary and companion to Impact Mojo — 494 terms, with 5 case studies, 10 worked formulae, and cross-references to where each term is taught. Offline-capable PWA. |

### Research toolkits — the OpenStacks

Reusable scripts, notebooks, and templates for people doing MEL and applied research. These are **stable**: usable today, maintained on a low-touch basis, not under active development. See [MAINTENANCE.md](MAINTENANCE.md).

| Stack | What it is | Languages |
|---|---|---|
| **[InsightStack](https://varnasr.github.io/InsightStack/)** ([source](https://github.com/Varnasr/InsightStack)) | The largest of the set. MEL calculators that run in the browser, loaders that open DHS and PLFS microdata as the files actually arrive, a tested econometrics module, data validation and labelling from one dictionary, annotated research briefs, and templates for logframes, indicators and MEL frameworks. | Stata, Python, R, SPSS |
| **[FieldStack](https://varnasr.github.io/FieldStack/)** ([source](https://github.com/Varnasr/FieldStack)) | Field operations while a survey is being collected: high-frequency checks, enumerator monitoring, back checks, GPS checks, an ODK reader, and the evening report that runs them. Then the analysis after: sample size, weights, design-based estimates. | R |
| **[EquityStack](https://varnasr.github.io/EquityStack/)** ([source](https://github.com/Varnasr/EquityStack)) | Equity from a development economics perspective. Who is carrying the bad outcome and how steeply: the Gini and Theil family, the concentration index with its corrections, within/between decomposition, Blinder-Oaxaca, benefit incidence, and design-based standard errors for clustered surveys. | Python |
| **[SignalStack](https://varnasr.github.io/SignalStack/)** ([source](https://github.com/Varnasr/SignalStack)) | Companion archive for the [Research Rundown](https://varna.substack.com) newsletter: every post in full, its recurring sections (praxis, glossary, researchers, reading) compiled into reference pages, and four tested scripts implementing its methods notes. Beside the stacks rather than one of them. | Markdown, Python |

InsightStack has a DOI: [10.5281/zenodo.15245182](https://doi.org/10.5281/zenodo.15245182).

### Writing

| Project | What it is |
|---|---|
| **[The Measurement Trap](https://github.com/Varnasr/the-measurement-trap)** | Companion site for *The Measurement Trap: India's Quest for Social Progress Through Eight Decades* (Routledge, March 2027; ISBN 9781041436744). Live at [whatcounts.in](https://whatcounts.in/). |
| **[The Very Last Superhero](https://postheroic.world)** | Illustrated speculative fiction set in a climate-collapsed India. |

### Utilities

| Project | What it is |
|---|---|
| **[CandidateDossier](https://github.com/Varnasr/CandidateDossier)** | CSV → PDF generator for uniform candidate dossiers with phone numbers and emails masked. It runs in the browser, and the PDF comes from the browser's print dialogue. [Live](https://varnasr.github.io/CandidateDossier/). |
| **[Experiments](https://idealogworks.foo/)** | The sandbox, at idealogworks.foo. Small browser tools are built and indexed there and are not listed here; anything that lasts moves to a repository of its own and appears above. |
| **[.github](https://github.com/Varnasr/.github)** | Shared community health files — contributing guide, code of conduct, issue templates — inherited by every repo above. |

---

## Retired

These are archived and read-only. The code stays public and browsable; nothing has been deleted. Three were built as a database, API and dashboard pipeline for an ecosystem that the toolkits above never needed. PolicyStack was replaced by PolicyDhara.

| Repo | Was |
|---|---|
| **[RootStack](https://github.com/Varnasr/RootStack)** | SQLite/PostgreSQL schemas and seed data for the shared data layer |
| **[BridgeStack](https://github.com/Varnasr/BridgeStack)** | FastAPI backend serving RootStack to frontends |
| **[ViewStack](https://github.com/Varnasr/ViewStack)** | React dashboard for exploring the data |
| **[PolicyStack](https://github.com/Varnasr/PolicyStack)** | South Asia policy tracker: 15 flagship schemes and four years of budget data as static CSVs. Replaced by [PolicyDhara](https://github.com/Varnasr/PolicyDhara), which updates itself |
**Not retired — graduated.** [ImpactLex](https://www.impactmojo.in/impactlex/) moved into Impact Mojo rather than winding down, and is listed under Teaching and practice above. Its [old repository](https://github.com/Varnasr/ImpactLex) is archived for citation continuity only; the living version is at [impactmojo.in/impactlex](https://www.impactmojo.in/impactlex/).

Four further stacks — ClimateStack, EduStack, SocialStack, InfraStack — were on a published roadmap and were never started. That roadmap has been withdrawn rather than left standing as a promise. The needs behind them are better served by [How India Lives](https://github.com/Varnasr/how-india-lives), [PolicyDhara](https://github.com/Varnasr/PolicyDhara), and [JanVayu](https://www.janvayu.in).

---

## Status vocabulary

Every repo listed here uses one of three labels, and they mean specific things:

| Label | Meaning |
|---|---|
| **Active** | Under current development. Issues and pull requests get responses. |
| **Stable** | Usable and correct, not under development. Bug reports are welcome; new features are unlikely. |
| **Retired** | Archived, read-only. Kept public for reference and citation. |

The full policy — what gets updated, how often, and what to expect if you open an issue — is in [MAINTENANCE.md](MAINTENANCE.md).

## Using this work

Everything here is MIT-licensed code unless a repo says otherwise (some carry Creative Commons terms for written content — check the individual LICENSE). You can clone, adapt, and redistribute. Attribution is appreciated, not required.

Each toolkit is self-contained: clone the one you need, read its README, run it. There is no ecosystem to install and no shared dependency to satisfy.

## Contributing

Issues and pull requests are welcome on any repo marked Active or Stable. Shared guidelines live in the [.github repo](https://github.com/Varnasr/.github):

- [Contributing guidelines](https://github.com/Varnasr/.github/blob/main/CONTRIBUTING.md)
- [Code of Conduct](https://github.com/Varnasr/.github/blob/main/CODE_OF_CONDUCT.md)

Please be aware that response times on Stable repos are measured in weeks, not days.

## Citation

If you use this work, please cite it. Machine-readable metadata is in [CITATION.cff](CITATION.cff).

## About

**Dr. Varna Sri Raman** — Development economist and social researcher with 20+ years of experience across public health, education, gender equity, and climate resilience in India and South Asia. Has led programme design, MEL strategies, and research with Oxfam, UNICEF, Gates Foundation, PLAN India, and BBC Media Action.

[GitHub](https://github.com/Varnasr) · [Twitter](https://x.com/varna) · [Web](https://idealog.works)

## Support

If this work is useful to you, you can support it via UPI: `varna@icici` — see [support.html](https://openstacks.dev/support.html) for a QR code.

## License

MIT — free to use, modify, and share. See [LICENSE](LICENSE).

---

<sub>AI tools have been used for documentation, code generation, and editing support. All decisions, designs, datasets, and content curation are entirely the creator's.</sub>
