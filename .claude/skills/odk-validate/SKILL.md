---
name: odk-validate
description: Validate an ODK XLSForm with a two-stage pipeline — structural validation via the xls2xform CLI, then optional regression testing against a baseline with PyXComparer. Use when the user has a generated or edited .xlsx form and wants to confirm it is syntactically valid, spec-compliant, and free of unintended logic changes, or when they invoke /odk-validate.
allowed-tools: Bash, Read, Glob, Grep
---

# odk-validate

Validate a generated XLSForm using a two-stage pipeline.

## Usage

Provide the path to a form: `<path-to-form.xlsx> [--baseline <baseline-form.xlsx>]`

## Two-Stage Validation

**Stage 1: Structural Validation**
- Runs `xls2xform` CLI to check syntax and XLSForm spec compliance
- Converts `.xlsx` to `.xml` to verify structural integrity
- Catches: missing sheets, invalid field types, broken XPath expressions, duplicate variable names
- `xls2xform` is required: `pip install pyxform`

**Stage 2: Regression Testing** (optional, requires baseline)
- Uses [PyXComparer](https://github.com/joybindroo/PyXComparer) to compare against a known-good baseline
- Isolates deltas in `relevant` and `constraint` columns (where breaking changes hide)
- Ensures no unintended logic changes between versions
- PyXComparer: `pip install PyXComparer` from source

## Important Notes

⚠️ **Do NOT use** the `pyxform` Python package for script-based validation (it's for conversion only)
- Always use the `xls2xform` **CLI tool** (same package, different interface)

✓ **Always run** structural validation before deployment
- Catches 90% of issues that would fail in the field

✓ **Recommended** to run regression testing when iterating
- Prevents logic bugs from silently accumulating across versions

## Example

```bash
# Basic validation
xls2xform my_form.xlsx

# With baseline comparison (PyXComparer)
# compares my_form_v2.xlsx against my_form_v1.xlsx
```

## Reference

- `skills.md` — validation pipeline details, QA gates
- `references/technical_reference.md` — common pitfalls (formula stripping, XPath errors)
- `skills_archive/tooling/xlsform_validation.md` — validation tooling details
- `skills_archive/tooling/pyXcomparer.md` — regression testing guide
- `odk-docs` MCP server — troubleshoot xls2xform errors against official ODK docs/forum
