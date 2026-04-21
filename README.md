# ODK Form Skills for AI Agents

This repository is a specialized knowledge base and operational framework designed to empower AI agents—such as **Claude Code, Open Claw, Nanobot, and Open Code**—to act as professional ODK (Open Data Kit) XLSForm Programmers and Data Analysts.

It transforms the complex process of survey design, validation, and deployment into a set of machine-readable skills, allowing AI agents to bridge the gap between natural language requirements and production-ready, analysis-optimized survey instruments.

## 🎯 Purpose
The goal of this project is to provide AI agents with the "cognitive tools" to ensure ODK forms are:
1. **Standardized**: Following strict naming and logic conventions that prevent data corruption.
2. **Analysis-Ready**: Optimized for seamless data cleaning and analysis in **Python (Pandas)** and **SAS**.
3. **Fully Agentic**: Structured so that AI assistants can program, validate, deploy, and analyze surveys with minimal human intervention.

## 🛠️ How to Use These Skills in AI Agents

Depending on the agent you are using, here is how to activate this framework:

### 🤖 For Nanobot
Nanobot can ingest this repository as a **Custom Skill**. 
- **Setup**: Add the repository path to Nanobot's workspace or use the `skill-creator` to package it.
- **Execution**: Once the workspace is indexed, Nanobot will automatically reference `skills.md` and `conventions.md` when tasked with ODK form design.

### 💻 For Claude Code
Claude Code can use this repository as a **Contextual Knowledge Base**.
- **Setup**: Clone this repository into your project directory.
- **Execution**: Start your session by telling Claude: *"Read the ODK-Form-Skills repository and adopt the Master ODK Programmer persona defined in skills.md."* Claude will then use the local files to guide its code generation.

### 🦅 For Open Claw
Open Claw can utilize this as a **System Prompt Extension**.
- **Setup**: Feed the content of `skills.md` and `conventions.md` into the agent's system instructions or a dedicated "Skill" slot.
- **Execution**: The agent will apply the modular design patterns and naming conventions automatically during the form-building process.

---

## 🛠️ The End-to-End AI Workflow
This framework implements a complete loop from design to insight, specifically tailored for agentic execution:

### 1. Design $\rightarrow$ `ODK-Form-Skills`
- **Agent Persona**: AI agents should initialize using the "Master Programmer" persona in `skills.md`.
- **Conventions**: Agents must adhere to `conventions/conventions.md` for `snake_case` naming and standardized special values (`-88`, `-89`, `-90`).
- **Modules**: Agents can inject production-ready blocks from `modules/modules.md` (e.g., Informed Consent, Household Rosters).
- **File Generation**: Agents use `src/xlsform_generator.py` and `templates/odk_template.xlsx` to produce valid `.xlsx` files.
- **Validation**: Agents must use the `pyxform` library to validate the `.xlsx` structure and ensure successful XML conversion.

### 2. Validate $\rightarrow$ `PyXComparer`
- **Automated QA**: Agents use [PyXComparer](https://github.com/joybindroo/PyXComparer) to detect breaking changes between form versions.
- **Regression Testing**: Use `PyXComparer` to isolate the exact delta when a previously working form fails `pyxform` validation.

### 3. Deploy $\rightarrow$ `ODK Central`
- **Programmatic Push**: Agents use `pyODKmcp` or the ODK Central API to deploy validated forms without manual uploads.

### 4. Analyze $\rightarrow$ `pyODKmcp` + `pyMCP`
- **Data Ingestion**: Agents use the `pyODKmcp` MCP server to fetch submission data into a local SQLite database.
- **Natural Language Querying**: Agents transition to a Database MCP server (`pyMCP`), ensuring it is connected to the **exact same SQLite database** populated by `pyODKmcp`.

## 📂 Repository Structure
- `/conventions`: House style and naming standards for AI consistency.
- `/modules`: Reusable XLSForm building blocks for rapid agent generation.
- `/references`: Technical ODK syntax and logic patterns for AI reference.
- `/src`: Python scripts for automated XLSForm generation.
- `/templates`: Standardized ODK Excel templates.
- `/tooling`: Documentation for the software ecosystem (`PyXComparer`, `pyODKmcp`).
- `skills.md`: The core system prompts, environment setup, and operational workflows.
- `AGENTS.md`: Project-specific agent behavior and mandates.

## 🚀 Getting Started for AI Agents
To activate these skills, an AI agent should:
1. Read `skills.md` to adopt the **Master ODK Programmer** persona.
2. Set up the virtual environment and install dependencies via `requirements.txt`.
3. Reference `conventions/conventions.md` and `references/technical_reference.md` during the construction phase.
4. Use `src/xlsform_generator.py` to output the final form.
5. Validate the output using `pyxform`.
6. Follow the **Workflow for Form Generation** to ensure a production-ready output.
