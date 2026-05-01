# ODK Form Skills for AI Agents

This repository is a specialized knowledge base and operational framework designed to empower AI agents—such as **Claude Code, Open Claw, Nanobot, and Open Code**—to act as professional ODK (Open Data Kit) XLSForm Programmers and Data Analysts.

## 🎯 Purpose
The goal of this project is to provide AI agents with the "cognitive tools" to ensure ODK forms are:
1. **Standardized**: Following strict naming and logic conventions that prevent data corruption.
2. **Analysis-Ready**: Optimized for seamless data cleaning and analysis in **Python (Pandas)** and **SAS**.
3. **Fully Agentic**: Structured so that AI assistants can program, validate, deploy, and analyze surveys with minimal human intervention.

## 🛠️ The End-to-End AI Workflow
This framework implements a complete loop from design to insight:

### 1. Design $\rightarrow$ `ODK-Form-Skills`
- **Persona**: AI agents should initialize using the **Master ODK Programmer** persona defined in `skills.md`.
- **Standards**: Adhere to `snake_case` naming and standardized special values (`-88`, `-89`, `-90`).
- **Generation**: Use `src/xlsform_generator.py` to produce `.xlsx` files.
- **Advanced Logic**: Implement cascading selects and complex calculations using the patterns in `references/technical_reference.md`.
- **Formula Preservation**: Use **XML Patching** (raw text replacement in `xl/worksheets/sheet1.xml`) to prevent Python libraries from stripping `${variable}` syntax in formulas.

### 2. Validate $\rightarrow$ `xls2xform` & `PyXComparer`
- **Structural Validation**: Use the `xls2xform` CLI tool for the most accurate syntax and structural validation. **Avoid using the `pyxform` Python package for script-based validation.**
- **Regression Audit**: Use [PyXComparer](https://github.com/joybindroo/PyXComparer) to detect breaking changes between form versions and isolate deltas.
- **QA Gate**: Review changes in `relevant` and `constraint` columns to ensure no regressions in survey logic.

### 3. Deploy $\rightarrow$ `ODK Central`
- **Programmatic Push**: Use `pyODKmcp` or the ODK Central API to deploy validated forms.

### 4. Analyze $\rightarrow$ `pyODKmcp` + `pyMCP`
- **Data Ingestion**: Use `pyODKmcp` to fetch submission data into a local SQLite database.
- **Natural Language Querying**: Use `pyMCP` to query the database.
- **Feedback Loop**: Use analysis results to identify patterns or errors and suggest improvements back to the XLSForm design.

## 📂 Repository Structure
- `skills.md`: The core operational manual, validation pipeline, and standards (consolidated from archive).
- `references/technical_reference.md`: Technical ODK syntax, logic patterns, and implementation pitfalls.
- `src/`: Python scripts for automated XLSForm generation.
- `templates/`: Standardized ODK Excel templates and schemas.
- `skills_archive/`: Historical conventions, modules, and tooling documentation.
- `AGENTS.md`: Project-specific agent behavior and mandates.

## 🚀 Getting Started for AI Agents
To activate these skills, an AI agent should:
1. Read `skills.md` to adopt the **Master ODK Programmer** persona and understand the validation pipeline.
2. Reference `references/technical_reference.md` for technical syntax and "pitfalls" (like formula stripping).
3. Use `src/xlsform_generator.py` to output the final form.
4. Validate the output using the `xls2xform` CLI, followed by `PyXComparer`.
