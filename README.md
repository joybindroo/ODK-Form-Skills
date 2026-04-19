# ODK Design System & AI Framework

This repository provides a professional framework for the end-to-end lifecycle of ODK (Open Data Kit) survey instruments. It is designed to bridge the gap between natural language survey requirements, production-ready XLSForms, and AI-powered data analysis.

## 🎯 Purpose
The goal of this project is to ensure that ODK forms are:
1. **Standardized**: Following strict naming and logic conventions.
2. **Analysis-Ready**: Optimized for seamless data cleaning and analysis in **Python (Pandas)** and **SAS**.
3. **AI-Agentic**: Structured so that AI assistants can program, validate, deploy, and analyze surveys with minimal human intervention.

## 🛠️ The End-to-End Workflow
This framework implements a complete loop from design to insight:

### 1. Design $\rightarrow$ `ODK-Form-Skills`
- **Master Programmer**: Use the AI implementation guide in `skills.md` to generate forms.
- **Conventions**: Adhere to `conventions/conventions.md` for `snake_case` naming and standardized special values (`-88`, `-89`, `-90`).
- **Modules**: Leverage `modules/modules.md` for reusable blocks like Informed Consent and Household Rosters.

### 2. Validate $\rightarrow$ `PyXComparer`
- **QA Gate**: Use [PyXComparer](https://github.com/joybindroo/PyXComparer) to detect breaking changes between form versions.
- **Audit**: Ensure variable names haven't shifted, preventing breaks in downstream analysis scripts.

### 3. Deploy $\rightarrow$ `ODK Central`
- **Automation**: Use `pyODKmcp` or the ODK Central API to programmatically push validated forms to the server.

### 4. Analyze $\rightarrow$ `pyODKmcp` + `pyMCP`
- **Ingestion**: Use the `pyODKmcp` MCP server to fetch submission data and store it in a local SQLite database.
- **Insight**: Use a Database MCP server (like `pyMCP`) to perform natural language SQL queries on the collected data.

## 📂 Repository Structure
- `/conventions`: House style and naming standards.
- `/modules`: Reusable XLSForm building blocks.
- `/references`: Technical ODK syntax and logic patterns.
- `/tooling`: Documentation for the software ecosystem (`PyXComparer`, `pyODKmcp`).
- `skills.md`: System prompts and workflows for AI agents.

## 🚀 Getting Started for AI Agents
To turn an AI into a Master ODK Programmer, initialize it with the persona and workflow defined in [`skills.md`](./skills.md).
