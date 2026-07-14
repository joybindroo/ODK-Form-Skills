# ODK Form Skills for Claude Code

Custom [Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) that expose the ODK Form Skills project as Claude Code commands. Each skill is a spec-compliant directory containing a `SKILL.md` with YAML frontmatter (`name`, `description`, and where relevant `allowed-tools`).

## Available Skills

| Skill | Directory | Purpose |
|---|---|---|
| `/odk` | `odk/SKILL.md` | Master skill — full workflow orchestration (Design → Validate → Deploy → Analyze) |
| `/odk-generate` | `odk-generate/SKILL.md` | Create XLSForm from survey specifications |
| `/odk-validate` | `odk-validate/SKILL.md` | Validate forms (xls2xform + PyXComparer) |
| `/odk-reference` | `odk-reference/SKILL.md` | Access standards, naming conventions, reusable modules |

## Structure

```
.claude/skills/
  odk/SKILL.md            # master workflow skill
  odk-generate/SKILL.md   # form generation
  odk-validate/SKILL.md   # two-stage validation
  odk-reference/SKILL.md  # standards & module lookup
```

Skills reference the repo-root knowledge base (`skills.md`, `references/`, `src/`, `templates/`, `skills_archive/`) by relative path — clone the whole repo to get everything.

## How to Use

In Claude Code, invoke a skill by typing the command:

```
/odk-generate
```

Then provide your survey specification (fields, logic, choices).

Or use the master skill:

```
/odk
```

And follow the workflow step-by-step. Skills are also auto-discovered by their `description` frontmatter, so Claude may activate the relevant one when your request matches.

## Installation

These skills are part of the ODK Form Skills project. They're automatically available when Claude Code is working in this repository (indicated by CLAUDE.md).

To activate:
1. Open this repository in Claude Code
2. Type `/odk` or `/odk-generate` in the command input
3. Follow the prompts

## Documentation

Each skill file contains:
- **Usage** — how to invoke the skill
- **What It Does** — step-by-step process
- **Standards Applied** — naming conventions, validation rules
- **Examples** — sample input/output
- **Reference** — links to detailed documentation

For complete documentation, read:
- `skills.md` — Operational manual (naming, validation, modules)
- `AGENTS.md` — Agent instructions and documentation requirements
- `references/technical_reference.md` — Technical syntax and patterns

## Persona

When using these skills, adopt the **"Master ODK Programmer"** persona:
- Expert in XLSForm syntax and ODK Center practices
- Fluent in standardized naming conventions and special values
- Skilled at cascading selects, XPath logic, and constraint patterns
- Focused on analysis-ready forms for Python/Pandas and SAS integration

## Key Standards

**Naming:** `snake_case` with module prefix (`demog_*`, `hh_*`, `agri_*`)
**Special Values:** `-88` (don't know), `-89` (refused), `-90` (not applicable)
**Choices:** Integer values only, cascading via filter columns
**Validation:** xls2xform CLI (not pyxform package) + PyXComparer for regression

## Requirements

- Python 3.6+
- Dependencies: `pip install -r requirements.txt`
  - openpyxl, pandas, pyxform, pyodk
- Optional tools:
  - [PyXComparer](https://github.com/joybindroo/PyXComparer) — for regression testing
  - pyODKmcp — for ODK Central integration
  - pyMCP — for database querying

## Workflow Example

```
1. I need a household survey with cascading locations
   └─ /odk-generate
      (describe survey structure)

2. System generates my_household_survey.xlsx

3. I validate it
   └─ /odk-validate my_household_survey.xlsx

4. Validation passes, I'm ready to deploy

5. I push to ODK Central
   └─ (using pyODKmcp)

6. Later, I analyze submissions
   └─ (using pyODKmcp + SQL)
```

## Troubleshooting

**"Command not found"**: Skills are available when Claude Code is in this repository
**"xls2xform not found"**: Install with `pip install pyxform`
**"PyXComparer not found"**: Install from [source](https://github.com/joybindroo/PyXComparer)
**"Formula stripped"**: Use XML patching (raw text replacement in `xl/worksheets/sheet1.xml`)

## Learn More

- `skills.md` — Complete operational manual
- `references/technical_reference.md` — Technical details and patterns
- `AGENTS.md` — Project-specific instructions
- `CLAUDE.md` — This project overview
