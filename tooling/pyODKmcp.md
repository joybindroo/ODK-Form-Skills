# pyODKmcp: AI-Powered ODK Data Bridge (MCP Server)

pyODKmcp is a Model Context Protocol (MCP) Server that enables AI agents to interact directly with ODK Central. It transforms ODK Central from a static data repository into a live, queryable context for AI-powered analysis.

## 🚀 Core Capabilities
- **Project & Form Discovery**: Allows AI agents to list all projects and forms on an ODK Central instance to understand the data landscape.
- **Automated Data Ingestion**: Fetches submission data for specific forms and automatically persists it into a local SQLite database.
- **Agentic Data Bridge**: Acts as the "fetcher" in a dual-server workflow, providing the raw data that a Database MCP server (like `pyMCP`) can then query.

## 🛠️ Integration in the ODK Workflow
pyODKmcp represents the **Analysis & Monitoring** phase of the survey lifecycle.

### 1. The "Fetch $\rightarrow$ Store $\rightarrow$ Analyze" Loop
Instead of manual CSV exports, the workflow becomes:
1. **Discovery**: AI uses `list_projects()` and `list_forms()` to find the target data.
2. **Ingestion**: AI uses `get_data()` to pull submissions and save them to a local table.
3. **Analysis**: AI switches to a Database MCP server to run SQL queries (e.g., "What is the average age of respondents in Bihar?") using natural language.

### 2. Closing the Feedback Loop
By analyzing real-time data via pyODKmcp, the AI agent can identify patterns or errors in the collected data and suggest improvements to the XLSForm design (referencing `ODK-Form-Skills` and validating changes via `PyXComparer`).

## 💻 Toolset for the AI Agent
- `list_projects()`: Map the ODK Central environment.
- `list_forms(project_id)`: Identify specific instruments.
- `get_data(project_id, form_id)`: Sync ODK submissions to local SQLite.
