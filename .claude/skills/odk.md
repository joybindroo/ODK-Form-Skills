# /odk

Master skill for the full ODK XLSForm workflow: Design → Validate → Deploy → Analyze

## Persona

Adopt the **"Master ODK Programmer"** persona when using this skill:
- Expert in XLSForm syntax and ODK Center best practices
- Fluent in snake_case naming conventions and standardized special values
- Skilled at cascading selects, complex XPath logic, and constraint patterns
- Focused on analysis-ready forms that work seamlessly with Python/Pandas and SAS

## Full Workflow

```
1. DESIGN (Python generation)
   └─ /odk-generate <spec>
      Creates .xlsx using src/xlsform_generator.py
      Applies naming conventions, special values, cascading filters

2. VALIDATE (Two-stage gate)
   └─ /odk-validate <form.xlsx> [--baseline <baseline.xlsx>]
      Stage 1: xls2xform CLI (structural validation)
      Stage 2: PyXComparer (regression testing vs. baseline)

3. DEPLOY (ODK Central)
   └─ Use pyODKmcp or ODK Central API
      Push validated form to server

4. ANALYZE (Data ingestion + SQL)
   └─ Use pyODKmcp to fetch submissions into SQLite
      Query with SQL (via pyMCP or similar)
      Feedback loop: use results to improve form
```

## Operational Mandates

**Standards:** Always follow naming conventions in `skills.md`
- Variables: `snake_case` with module prefix (`demog_*`, `hh_*`, `agri_*`)
- Groups: `grp_*`, Calculations: `calc_*`
- Special values: `-88`, `-89`, `-90`, `99`
- Choice values: integers only

**Tooling Chain:**
- **Design**: Use `templates/schema.json` and `references/technical_reference.md`
- **Generation**: Use `src/xlsform_generator.py` with `templates/odk_template.xlsx`
- **Validation**: xls2xform CLI (not pyxform package), then PyXComparer for regression
- **Deployment**: pyODKmcp or ODK Central API
- **Analysis**: pyODKmcp + database MCP (same SQLite database for both)

**Documentation:** After any significant change
- Update `README.md` to reflect current state
- Commit with descriptive messages: `docs: update reference` or `feat: add household module`
- Push immediately after validation to maintain audit trail

**Version Control:**
- Every form change is committed to Git
- Always validate before committing generated forms
- Baseline forms are maintained for regression testing

## Quick Start

1. Define your survey (fields, types, logic)
2. Run `/odk-generate` with your spec
3. Run `/odk-validate my_form.xlsx` (or with baseline)
4. If validation passes, commit and push
5. Deploy to ODK Central
6. Use pyODKmcp to fetch submissions and analyze

## Reference

- `skills.md` — Complete operational manual, module templates, validation pipeline
- `AGENTS.md` — Project-specific agent instructions and documentation requirements
- `references/technical_reference.md` — Technical ODK syntax, XPath patterns, pitfalls
- `/odk-generate` — Form generation skill
- `/odk-validate` — Validation skill
- `/odk-reference` — Standards and module reference

## Key Files

| File | Purpose |
|---|---|
| `src/xlsform_generator.py` | XLSForm generation engine (cascading choice support) |
| `templates/odk_template.xlsx` | Base Excel template |
| `templates/schema.json` | Field type schema |
| `skills.md` | Operational manual (naming, validation, modules) |
| `skills_archive/` | Archived documentation (conventions, modules, tooling) |

## Important Notes

⚠️ **Formula Preservation**: Use XML patching (raw text replacement in `xl/worksheets/sheet1.xml`) to preserve `${variable}` syntax when editing .xlsx files programmatically

⚠️ **Validation**: Always use `xls2xform` CLI (not the Python package) for validation

✓ **Cascading Selects**: Implemented via filter columns + `choice_filter` expressions (handled automatically by generator)

✓ **Analysis-Ready**: Integer choice values, ISO date formats, standardized special values for seamless Python/SAS integration
