# ODK Design Conventions (House Style)

This document defines the standards for ODK form development to ensure data consistency, ease of analysis in Python and SAS, and maintainability.

## 1. Naming Conventions
To ensure compatibility with Python (Pandas) and SAS, follow these rules:

- **Variable Names**: 
    - Use `snake_case` (lowercase with underscores).
    - Avoid starting names with numbers.
    - **Prefixing**: Use module-based prefixes to group variables.
        - Example: `demog_age`, `demog_gender`, `hh_size`, `agri_plot_area`.
    - **Length**: Keep names descriptive but concise (recommended $\le 64$ characters for SAS/Python compatibility).
- **Group Names**: 
    - Prefix with `grp_`. Example: `grp_household_info`.
- **Calculation Fields**: 
    - Prefix with `calc_`. Example: `calc_total_income`.

## 2. Special Value Conventions
Standardize "missing" or "non-applicable" values to simplify data cleaning in Python/SAS.

| Value | Meaning | Usage |
| :--- | :--- | :--- |
| `-88` | Don't know | Numeric fields where the respondent is unsure. |
| `-89` | Refused | Numeric fields where the respondent declines to answer. |
| `-90` | Not applicable | Numeric fields that are logically N/A. |
| `99` | Other (specify) | Used as a choice value for "Other" options. |

**Constraint Pattern**: 
For any numeric field that should be positive but allow special values:
`. >= 0 or . = -88 or . = -89 or . = -90`

## 3. Data Analysis Alignment
- **Choice Values**: Always use integers for `value` in the `choices` sheet. Avoid using the label as the value.
- **Date/Time**: Use standard ISO formats.
- **Boolean**: Use `1` for Yes and `0` for No.
