# XLSForm-Validation-Skills: Syntax & Structural Validation

XLSForm-Validation-Skills is an external toolkit used to ensure that XLSForms are syntactically correct and compatible with the ODK ecosystem before they are uploaded to ODK Central.

## 🚀 Core Capabilities
- **Syntax Checking**: Validates the XLSForm structure against the official ODK specification.
- **XML Conversion**: Tests the conversion of the `.xlsx` file into the `.xml` format used by ODK Collect.
- **Error Identification**: Pinpoints the exact row and column causing a validation failure.

## 🛠️ Integration in the ODK Workflow
This tool is the **first gate** in the validation pipeline. It must be run *before* PyXComparer.

### The Validation Flow:
1. **Syntax Validation (XLSForm-Validation-Skills)**: 
   - Run `check_xlsform.py` to ensure the form is structurally sound.
   - If errors are found, refer to `references/xlsform_syntax.md` in the repo to fix them.
2. **Regression Audit (PyXComparer)**: 
   - Once the form is syntactically valid, use PyXComparer to ensure changes haven't broken existing data paths.
3. **Deployment**: 
   - Upload the validated and audited form to ODK Central.

## 💻 Installation & Usage
Since this is an external repository, do not maintain local copies of the scripts. Install it directly from the source:

```bash
# Clone the repository
git clone https://github.com/joybindroo/XLSForm-Validation-Skills.git

# Run the validation script
python3 XLSForm-Validation-Skills/scripts/check_xlsform.py your_form.xlsx
```
