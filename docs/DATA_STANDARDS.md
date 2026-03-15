# Data Standards

Conventions for sample data across all OpenStacks repositories.

---

## Directory Structure

Every stack that includes data should use:

```
StackName/
└── sample_data/
    ├── dataset_name.csv
    ├── dataset_name_dictionary.csv
    └── README.md              ← Describes each dataset briefly
```

- Use `sample_data/` as the directory name. Not `data/`, not `datasets/`.
- Keep the directory at the repository root.
- Include a short `README.md` inside `sample_data/` listing each file and its purpose.

## File Formats

**CSV is the default.** Use comma-separated values for all tabular data unless there's a strong reason not to.

| Format | When to use |
|--------|-------------|
| CSV | Default for all tabular data |
| JSON | API responses, nested structures, config files |
| GeoJSON | Geospatial data |
| Parquet | Large datasets (>100MB) where CSV is impractical |
| SQLite | Database seeds and schema exports (RootStack) |
| Markdown | Documentation, narrative content |

### CSV Conventions

- UTF-8 encoding.
- Header row required.
- Use `snake_case` for column names (e.g., `district_name`, `enrollment_rate`).
- No trailing commas.
- Quote fields that contain commas or newlines.
- Use ISO 8601 for dates: `YYYY-MM-DD`.
- Use empty fields (not `NA`, `N/A`, or `null`) for missing values — let the analysis tool handle missing data conventions.

## Data Dictionaries

Every dataset should have a companion data dictionary. Name it `<dataset_name>_dictionary.csv` and place it alongside the dataset.

The dictionary should include:

| Column | Description |
|--------|-------------|
| `variable_name` | Column name as it appears in the dataset |
| `label` | Human-readable description |
| `type` | Data type: `string`, `integer`, `float`, `date`, `boolean`, `categorical` |
| `unit` | Unit of measurement where applicable (e.g., `INR`, `km`, `percent`) |
| `values` | Allowed values or range (e.g., `1-5`, `male/female/other`) |
| `notes` | Any additional context |

Example:

```csv
variable_name,label,type,unit,values,notes
district_id,Unique district identifier,string,,,Based on Census 2011 codes
enrollment_rate,Gross enrollment ratio,float,percent,0-200,Can exceed 100 due to over-age enrollment
year,Academic year start,integer,,2010-2024,
```

## Anonymisation

All sample data must be anonymised. No real individual-level data should appear in any repository.

### Requirements

- **No personally identifiable information (PII).** No names, phone numbers, email addresses, Aadhaar numbers, GPS coordinates that identify households, or any other direct identifiers.
- **Aggregate or synthesise.** Use district-level or block-level aggregates where possible. Where individual-level data is needed for demonstration, synthesise it.
- **Clearly label synthetic data.** If a dataset is generated or synthesised, say so in the data dictionary and the `sample_data/README.md`.
- **Real structure, fake values.** Sample data should have realistic structure, column names, and distributions — but not contain real observations from real people.

### What's acceptable

| Acceptable | Not acceptable |
|-----------|---------------|
| District-level health indicators from public sources | Individual patient records |
| Synthesised household survey responses | Real survey microdata |
| Anonymised, aggregated programme data | Named beneficiary lists |
| Published government statistics | Unpublished administrative data |

## Naming Conventions

### Files
- Use `snake_case`: `district_health_indicators.csv`, not `District Health Indicators.csv`.
- Be descriptive: `maternal_health_block_level_2023.csv` is better than `data1.csv`.
- Include geographic scope and year where relevant.

### Variables
- Use `snake_case` for all column names.
- Prefix with domain where helpful: `edu_enrollment_rate`, `health_imr`.
- Avoid abbreviations unless they're standard in the field (e.g., `imr` for infant mortality rate, `gdp`).

## Size Guidelines

Sample data should be small enough to include in a Git repository without issues.

| Guideline | Limit |
|-----------|-------|
| Individual CSV file | Under 5 MB |
| Total `sample_data/` directory | Under 25 MB |
| Rows per sample dataset | Enough to demonstrate the tool (typically 50-500 rows) |

If a workflow requires larger data, provide a small sample in the repo and document how to obtain the full dataset.

## Attribution

If sample data is derived from a public source, include attribution:

- Note the source in the data dictionary's `notes` column.
- Add a line to the `sample_data/README.md` with the source, URL, and access date.
- Respect the source's license terms.

Common sources for development data in India and South Asia:
- Census of India
- NFHS (National Family Health Survey)
- UDISE (education data)
- HMIS (health management information system)
- Open Government Data Platform India (data.gov.in)
