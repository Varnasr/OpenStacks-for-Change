# Contributing to OpenStacks

Thank you for your interest in contributing to [OpenStacks for Change](https://openstacks.dev). This guide applies to all repositories in the ecosystem.

## Who Can Contribute

OpenStacks welcomes contributions from:

- **Development practitioners** — Share tools, templates, and workflows from your own work (anonymised)
- **Researchers and evaluators** — Contribute analysis scripts, methodologies, and replication files
- **Data analysts and engineers** — Improve code quality, add tests, fix bugs
- **Writers and editors** — Improve documentation, add use case guides, fix errors
- **Students** — Practice with real-world development data and contribute improvements

## How to Contribute

### Reporting Issues

- Use the repository's **Issues** tab to report bugs, suggest features, or ask questions
- Check existing issues first to avoid duplicates
- Use issue templates where available

### Submitting Changes

1. **Fork** the repository
2. **Create a branch** for your change (`git checkout -b feature/your-feature-name`)
3. **Make your changes** with clear, descriptive commit messages
4. **Test your changes** — ensure scripts run and notebooks execute without errors
5. **Submit a pull request** with a clear description of what you changed and why

### What Makes a Good Contribution

- **Self-contained** — Scripts should work independently with sample data
- **Documented** — Include comments, a header description, and usage instructions
- **Anonymised** — Never include real participant data, names, or identifying information
- **Reproducible** — Include sample data or clear instructions for obtaining test data
- **Tested** — Verify that your code runs without errors

## Contribution Ideas by Stack

| Stack | Good Contributions |
|-------|-------------------|
| **InsightStack** | MEL calculators, Stata/SPSS scripts, research templates |
| **FieldStack** | R notebooks, survey tools, evaluation frameworks |
| **EquityStack** | Python scripts, Jupyter notebooks, data workflows |
| **SignalStack** | Research tool recommendations, method spotlights |
| **RootStack** | Database schemas, seed data, SQL queries |
| **BridgeStack** | FastAPI endpoints, data models, API tests |
| **ViewStack** | Frontend components, chart templates, dashboard designs |
| **PolicyStack** | Policy data, budget analysis scripts, government data scrapers |

## Code Style

- **Python:** Follow PEP 8. Use descriptive variable names.
- **R:** Follow the tidyverse style guide. Use snake_case.
- **Stata:** Use clear variable labels and value labels.
- **Markdown:** Use ATX-style headers (`#`). Keep lines under 120 characters.

## Data Standards

- Use **CSV** for tabular data (UTF-8 encoding)
- Include a **data dictionary** or codebook for any new datasets
- **Never commit** real participant data, credentials, or API keys
- Use **sample_data/** directories for test datasets

## Questions?

Open an issue in the relevant repository or email varna.sr@gmail.com.

## Code of Conduct

All contributors are expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md).
