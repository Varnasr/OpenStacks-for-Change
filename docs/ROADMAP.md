# Roadmap

Where OpenStacks is now and where it's going.

---

## Active and Stable

These stacks are usable today. They have working code, sample data, documentation, and real-world testing.

| Stack | Status | What's there |
|-------|--------|-------------|
| **InsightStack** | Stable | MEL calculators, visual frameworks, Observable notebooks, Excalidraw diagrams, Miro templates, Flourish charts. Multi-language: Stata, Python, R. |
| **FieldStack** | Stable | Full lifecycle R notebooks — survey design, sampling, regression, cost-effectiveness, qualitative coding, automated reporting. KoboToolbox/ODK integration. |
| **EquityStack** | Stable | Python/Jupyter data workflows for health, gender, education, and climate equity. Data cleaning, modelling, and visualisation templates. |
| **SignalStack** | Stable | Research Rundown newsletter archive. Method spotlights, curated resources, research tool reviews. |

**Current priorities for active stacks:**
- Expand sample datasets with data dictionaries across all stacks
- Improve cross-stack consistency in documentation and directory structure
- Add automated testing where applicable (FieldStack, EquityStack)

---

## Being Built

These stacks have scaffolding, initial code, and clear direction. They're the best place for contributors to make an immediate impact.

| Stack | Status | What exists | What's needed |
|-------|--------|-------------|---------------|
| **RootStack** | Early-stage | PostgreSQL/SQLite schemas, seed data structure | More schema coverage, migration scripts, seed data for key indicators |
| **BridgeStack** | Early-stage | FastAPI project structure, initial endpoints | API routes for core data, authentication, documentation |
| **ViewStack** | Early-stage | Frontend scaffolding | Dashboard components, data visualisation views, responsive design |
| **PolicyStack** | Early-stage | Policy tracking structure, South Asia focus | Structured policy data, scheme metadata, budget parsing |

**Current priorities for early-stage stacks:**
- RootStack: Define schemas for health, education, and climate indicators
- BridgeStack: Build REST endpoints that serve RootStack data
- ViewStack: Choose frontend framework and build first dashboard prototype
- PolicyStack: Structure India government scheme data as a proof of concept

---

## Planned

These stacks are designed but not yet started. They're open for proposals and early contributions.

### ClimateStack
**Focus:** Composite risk scores, resilience modelling, geo-spatial mapping.

Intended scope:
- Climate vulnerability indices at district/block level
- Resilience scoring frameworks
- Integration with publicly available geo-spatial and weather data
- Visualisation templates for climate risk communication

### EduStack
**Focus:** Learning assessment pipelines, education outcome dashboards.

Intended scope:
- Assessment data analysis tools (NAS, ASER-style datasets)
- Enrollment, dropout, and transition rate calculators
- School-level indicator dashboards
- Integration with UDISE and similar public data sources

### SocialStack
**Focus:** Rapid ethnography, qualitative coding, NLP for field narratives.

Intended scope:
- Qualitative data analysis templates
- Thematic coding frameworks
- NLP pipelines for field notes and interview transcripts
- Mixed-methods integration tools

### InfraStack
**Focus:** Access scoring, infrastructure mapping, spatial planning tools.

Intended scope:
- Infrastructure access indices (health facilities, schools, water, roads)
- Distance and coverage analysis
- Spatial planning support tools
- Integration with OpenStreetMap and government facility data

---

## Contribution Priorities

Where help is most needed right now, roughly in order of impact.

### High impact
1. **RootStack schemas** — Define and populate database schemas for core development indicators
2. **BridgeStack API routes** — Build endpoints that connect data to frontends
3. **Sample data with dictionaries** — Add well-documented sample datasets to any active stack
4. **EquityStack notebooks** — New Python notebooks for common development data tasks

### Medium impact
5. **PolicyStack data structuring** — Convert policy documents into structured, queryable formats
6. **ViewStack prototyping** — Build initial dashboard components
7. **FieldStack testing** — Add test coverage to R notebooks and scripts
8. **Cross-stack documentation** — Improve consistency and fill gaps

### Open for proposals
9. **ClimateStack design** — Propose architecture and initial tools for climate risk analysis
10. **EduStack design** — Propose tools for education data pipelines
11. **SocialStack design** — Propose qualitative analysis frameworks
12. **InfraStack design** — Propose infrastructure mapping tools

If you're interested in contributing to any of these, see [CONTRIBUTING.md](../CONTRIBUTING.md) or open an issue.
