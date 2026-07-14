---
name: odk-generate
description: Generate a production-ready, analysis-ready ODK XLSForm (.xlsx) from survey specifications. Use when the user describes a survey (fields, question types, choice lists, cascading logic, settings) and wants it turned into a valid XLSForm, or when they invoke /odk-generate. Applies snake_case naming conventions, integer choice values, standardized special values, and cascading choice filters via src/xlsform_generator.py.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---

# odk-generate

Generate a production-ready XLSForm from survey specifications.

## Usage

Invoke the skill, then provide:
- Survey structure (fields, types, logic)
- Choice lists (with cascading filters if hierarchical)
- Form settings (title, ID, version)

## What This Does

1. **Validates input** against naming conventions (snake_case, module prefixes)
2. **Generates `.xlsx`** using `src/xlsform_generator.py`
3. **Preserves formulas** using XML patching (prevents openpyxl from stripping `${variable}` syntax)
4. **Supports cascading selects** via filter columns and `choice_filter` expressions
5. **Outputs** analysis-ready form (integer choice values, ISO date formats, standard special values)

## Standards Applied

- Variable naming: `snake_case` with module prefix (`demog_*`, `hh_*`, `agri_*`)
- Special values: `-88` (don't know), `-89` (refused), `-90` (not applicable)
- Choice lists: integers only, cascading via filter columns
- Constraints: auto-applied for special values (`. >= 0 or . = -88 or . = -89 or . = -90`)

## Example

```
Survey:
  - name: state
    type: select_one state
    label: Select State
    required: yes
  - name: city
    type: select_one city
    label: Select City
    choice_filter: state = ${state}

Choices:
  state:
    - name: 1, label: State 1
    - name: 2, label: State 2
  city:
    - name: 101, label: City 1, state: 1
    - name: 102, label: City 2, state: 1
    - name: 201, label: City 3, state: 2

Settings:
  form_title: City Selection Survey
  form_id: city_survey_v1
  version: 1
```

## Reference

- `skills.md` — naming conventions, special values, reusable module templates
- `references/technical_reference.md` — XPath expressions, advanced patterns
- `templates/schema.json` — field type schema
- `src/xlsform_generator.py` — generator source code
- `odk-docs` MCP server — look up ODK syntax/behavior not covered in the references above
