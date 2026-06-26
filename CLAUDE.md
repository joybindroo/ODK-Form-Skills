# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A specialized knowledge base and operational framework for AI agents to act as professional ODK (Open Data Kit) XLSForm programmers. It provides tools, standards, and templates for creating analysis-ready survey forms that work seamlessly with Python (Pandas) and SAS.

## Core Workflow

**Design** → (Python generation) **Validate** → (xls2xform + PyXComparer) **Deploy** → (ODK Central) **Analyze** → (SQL on submissions)

Key files:
- `skills.md` — operational manual (naming conventions, special values, validation pipeline, reusable modules)
- `references/technical_reference.md` — technical ODK syntax, XPath, implementation patterns
- `src/xlsform_generator.py` — main XLSForm generation engine
- `templates/` — schemas, field types, base template

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

## Get Started

Use Claude Code skills in this repo:
- `/odk-generate` — Create XLSForm from specifications
- `/odk-validate` — Validate form (xls2xform + PyXComparer)
- `/odk-reference` — Access standards, naming conventions, reusable modules
- `/odk` — Master skill for full pipeline

Or read `skills.md` for the complete operational manual.
