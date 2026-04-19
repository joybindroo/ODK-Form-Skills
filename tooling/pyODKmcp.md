# pyODKmcp: ODK Central Management & Automation

pyODKmcp is a Python-based tool designed to programmatically interact with ODK Central, automating the lifecycle of form deployment and data management.

## 🚀 Core Capabilities
- **Automated Deployment**: Programmatically upload and update XLSForms to ODK Central.
- **Form Management**: Manage form versions, draft/published statuses, and project settings via API.
- **Lifecycle Automation**: Bridges the gap between the design phase (XLSForm) and the production phase (ODK Central).

## 🛠️ Integration in the ODK Workflow
pyODKmcp serves as the **Deployment Layer**, removing the need for manual uploads via the ODK Central web interface.

### 1. Continuous Integration (CI)
Integrate pyODKmcp into a pipeline where a validated XLSForm (checked by PyXComparer) is automatically pushed to a test project in ODK Central.

### 2. Rapid Iteration
When an AI agent generates a new version of a form based on updated requirements, pyODKmcp can be used to instantly deploy that version for field testing.

### 3. Version Synchronization
Ensure that the version number in the `settings` sheet of the XLSForm is synchronized with the version tracked on the ODK Central server.

## 💻 Workflow Integration
The typical deployment sequence is:
`Design (ODK-Form-Skills)` $\rightarrow$ `Validate (PyXComparer)` $\rightarrow$ `Deploy (pyODKmcp)` $\rightarrow$ `Collect Data`.
