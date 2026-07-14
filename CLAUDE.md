# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A specialized knowledge base and operational framework for AI agents to act as professional ODK (Open Data Kit) XLSForm programmers. It provides tools, standards, and templates for creating analysis-ready survey forms that work seamlessly with Python (Pandas) and SAS. This is primarily a documentation/skills repo with one supporting Python module — there is no application build, lint, or test suite.

## Core Workflow

**Design** → (Python generation) **Validate** → (xls2xform + PyXComparer) **Deploy** → (ODK Central) **Analyze** → (SQL on submissions)

Key files:
- `skills.md` — operational manual (naming conventions, special values, validation pipeline, reusable modules)
- `references/technical_reference.md` — technical ODK syntax, XPath, implementation patterns
- `src/xlsform_generator.py` — main XLSForm generation engine
- `templates/` — schemas, field types, base template
- `AGENTS.md` — persona/process mandates (docs must be updated and changes committed/pushed after every significant edit)
- `skills_archive/` — original, pre-consolidation source docs (conventions, modules, tooling) that `skills.md` was consolidated from

## Commands

```bash
pip install -r requirements.txt        # openpyxl, pandas, pyxform, pyodk
python src/xlsform_generator.py        # runs the built-in example, writes enhanced_test.xlsx

xls2xform my_form.xlsx                 # structural validation → XForm (preferred over the pyxform package for validation)
```

There is no test suite. Validation of a generated form is done by running `xls2xform` against it, then diffing against a known-good baseline with PyXComparer (external tool, not vendored here).

## Architecture

`src/xlsform_generator.py` exposes two functions:
- `extract_template_metadata(template_path)` — reads column headers from `templates/odk_template.xlsx` (survey/choices/settings/entities sheets) so an agent can learn the exact schema before generating a form.
- `generate_xlsform(output_path, survey_data, choices_data, settings_data, template_path=None)` — builds a fresh `.xlsx` workbook via openpyxl. `choices_data` accepts either the "advanced" dict form (`{list_name: [{'name', 'label', ...filter_cols}, ...]}`, which auto-derives extra filter columns for cascading selects) or a legacy flat list of rows.

**Formula stripping caveat**: openpyxl/pandas can strip `${variable}` syntax out of formula-like cell values on save. When editing forms with Python (not just this generator), the required workaround is XML patching — unzip the `.xlsx`, raw-text-replace the broken formula back into `xl/worksheets/sheet1.xml`, rezip. This is documented in `references/technical_reference.md` §5A and must be followed rather than trusting openpyxl to preserve formulas.

`templates/schema.json` is the canonical column list per sheet (survey/choices/settings/entities) and `templates/field_types.json` presumably enumerates supported question types — treat `templates/odk_template.xlsx` as the source of truth for real-world column order since it's what `extract_template_metadata` reads from.

## ODK Docs MCP Server

An `odk-docs` MCP server (endpoint `https://odk-docs.mcp.kapa.ai`, HTTP transport, backed by kapa.ai indexing official ODK documentation and the ODK community forum) is registered for this project. It supports searching ODK docs, answering questions, troubleshooting, and form/workflow building — use it whenever authoring or debugging XLSForm logic that isn't already covered in `skills.md` / `references/technical_reference.md` (unfamiliar XPath functions, ODK Central-specific behavior, appearance/widget quirks, version-specific gotchas from the forum). Prefer it over guessing at ODK syntax or general web search, since it's scoped to authoritative ODK sources — but still validate anything it surfaces with `xls2xform` before trusting it in a generated form.

Reference: https://docs.getodk.org/docs-mcp/

**Claude Code** (already configured for this project):
```bash
claude mcp add --transport http odk-docs https://odk-docs.mcp.kapa.ai
```

**ChatGPT** (Pro/Plus/Team/Enterprise/Edu): Settings → Apps → Advanced settings → enable Developer Mode, then in ChatGPT Apps settings create a new app named `ODK Docs` with connection URL `https://odk-docs.mcp.kapa.ai`.

**OpenCode**: add to `opencode.json` in the project root:
```json
{
  "mcp": {
    "odk-docs": {
      "type": "remote",
      "url": "https://odk-docs.mcp.kapa.ai",
      "enabled": true
    }
  }
}
```

**Other MCP-compatible agents**: connect directly to the `https://odk-docs.mcp.kapa.ai` HTTP endpoint using whatever remote-MCP-server mechanism that agent provides.

## Claude Code Skills

Custom skills live in `.claude/skills/` and are the intended entry points for agent work in this repo:
- `/odk` — master skill, full Design → Validate → Deploy → Analyze pipeline
- `/odk-generate` — create an XLSForm from a survey spec
- `/odk-validate` — run xls2xform + PyXComparer against a form
- `/odk-reference` — look up standards/naming/reusable modules

Prefer these skills over re-deriving the workflow from scratch when the user's ask matches one of them.

## Critical Standards

**Variable Naming** (required for Python/SAS compatibility):
- `snake_case` with module prefix: `demog_age`, `hh_size`, `agri_plot_area`
- Groups: `grp_*`, Calculations: `calc_*`

**Special Values:**
- `-88` = Don't know, `-89` = Refused, `-90` = Not applicable, `99` = Other
- Constraint: `. >= 0 or . = -88 or . = -89 or . = -90`

**Choices:**
- Use **integers** as values (not strings)
- Cascading via filter columns + `choice_filter` expressions

Full detail (reusable header/consent/roster/geographic/asset/socio-economic modules, XPath function reference, audit-log configuration) is in `skills.md` and `references/technical_reference.md` — read those before generating a nontrivial form rather than relying on the summary above.
