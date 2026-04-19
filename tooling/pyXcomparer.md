# PyXComparer: XLSForm Version Control & QA

PyXComparer is a specialized tool for monitoring changes between different versions of ODK XLSForms, ensuring that survey modifications do not break data pipelines or analysis scripts.

## 🚀 Core Capabilities
- **Version Comparison**: Detects additions, deletions, and modifications between two XLSForm versions.
- **Change Categorization**: Specifically tracks changes in questions, choices, and settings.
- **Metadata Extraction**: Converts XLSForms into human-readable YAML/JSON data dictionaries.
- **Multi-Interface Support**: Available via CLI (for automation), Web (for non-technical review), and GUI.

## 🛠️ Integration in the ODK Workflow
PyXComparer acts as the **Quality Assurance (QA)** gate between design and deployment.

### 1. Validating Naming Conventions
Use PyXComparer to ensure that variable names follow the `conventions.md` (snake_case, module prefixes). If a variable name is changed, it will be flagged as a "modification," alerting the analyst that Python/SAS scripts may need updating.

### 2. Auditing Logic Changes
Before deploying a new version, generate an HTML report to review changes in `relevant` and `constraint` columns to ensure no regressions in survey logic.

### 3. Generating Data Dictionaries
Export the current form version to YAML/JSON to provide a machine-readable map of the survey for the data analysis team.

## 💻 Quick Usage (CLI)
```bash
# Compare two versions and generate a report
pyxcomparer compare survey_v1.xlsx survey_v2.xlsx -o report.html
```
