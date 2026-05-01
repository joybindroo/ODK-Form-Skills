# ODK Programming Skills

This document defines the operational skills and standards for AI agents acting as Master ODK Programmers.

## 1. Design & Construction
- **Naming Convention**: Use `snake_case` for all `name` columns.
- **Special Values**: Standardize on `-88` (Don't know), `-89` (Refused), and `-90` (N/A).
- **Cascading Selects**: Implement hierarchies (e.g., District $\rightarrow$ Block $\rightarrow$ Village) by adding filter columns to the `choices` sheet and using `choice_filter` in the `survey` sheet.
- **Formula Preservation**: When using Python to edit forms, use **XML Patching** (raw text replacement in `xl/worksheets/sheet1.xml`) to prevent libraries like `openpyxl` from stripping `${variable}` syntax in `concat()` or complex calculations.

## 2. Validation Pipeline
The validation process must follow this strict sequence:

### Step 1: Structural Validation (xls2xform CLI)
The primary gate for syntax and structural correctness is the `xls2xform` CLI tool. 
- **Action**: Run `xls2xform your_form.xlsx` to ensure the form is syntactically valid and can be converted to XML.
- **Requirement**: Do NOT rely on the `pyxform` Python package for script-based validation, as it may not perfectly mirror the ODK Central parser. Use the CLI for the most accurate results.

### Step 2: Regression Audit (PyXComparer)
Once structurally valid, use [PyXComparer](https://github.com/joybindroo/PyXComparer) to detect breaking changes between versions.
- **Action**: Compare the current version against a known-good baseline to isolate deltas.

### Step 3: Deployment
Deploy the validated and audited form to ODK Central via `pyODKmcp` or the API.

## 3. Generation Workflow
1. **Persona**: Initialize as "Master ODK Programmer".
2. **Schema**: Define the form structure using `templates/schema.json`.
3. **Generation**: Use `src/xlsform_generator.py` to create the `.xlsx` file.
4. **Validation**: Run `xls2xform` CLI $\rightarrow$ PyXComparer.
5. **Audit**: Log all changes in the project's audit trail.
