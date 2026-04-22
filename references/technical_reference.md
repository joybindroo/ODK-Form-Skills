# ODK Technical Reference

This library provides a quick-reference for ODK XLSForm syntax, operators, and logic patterns based on official ODK documentation.

## 1. Core Question Types
| Type | Description | Appearance/Notes |
| :--- | :--- | :--- |
| `text` | Open-ended text | `multiline` for long text |
| `integer` | Whole numbers | Use constraints for range validation |
| `decimal` | Floating point numbers | Use constraints for range validation |
| `select_one [list]` | Single choice | `horizontal`, `minimal` |
| `select_multiple [list]` | Multiple choice | `horizontal` |
| `geopoint` | GPS coordinates | Captures lat/long/alt |
| `calculate` | Hidden calculation | Used for logic and data transformation |
| `note` | Display text/info | Used for instructions or calculated results |
| `begin_repeat` / `end_repeat` | Roster/Loop | Use `repeat_count` for fixed-size loops |

## 2. Operators and Functions
### Math Operators
- `+`, `-`, `*` : Standard arithmetic.
- `div` : Division (e.g., `${a} div ${b}`).
- `mod` : Modulo (remainder).

### Logic Operators
- `and`, `or`, `not` : Boolean logic.
- `=` , `!=`, `<`, `>`, `<=`, `>=` : Comparison.

### Key Functions
- `coalesce(val1, val2, ...)` : Returns the first non-empty value.
- `if(condition, true_val, false_val)` : Conditional logic.
- `selected(list, choice)` : Checks if a specific choice is selected in a `select_multiple`.
- `count()` : Counts number of selections in a `select_multiple`.
- `indexed-repeat(name, index, repeat_group)` : Retrieves a value from a specific repeat instance. Use this to pull data from a previous roster iteration into a calculation or note.
- `pulldata('csvname', 'column', 'key')` : Pulls data from an external CSV file uploaded to the device. Essential for pre-loading beneficiary lists or site metadata.
- `once(expression)` : Evaluates the expression only once and stores the result.

## 3. Advanced ODK Features

### A. Automated Data Capture
- **Automatic GPS Capture**: Use `geopoint` with the `device` trigger, or set a `calculate` field with `once()` to capture location automatically upon form start.
- **Background Audio Recording**: Use the `audio` question type. For background recording, ensure the device settings allow the app to record while the screen is off or in the background.

### B. Cascading Selects (Choice Filtering)
- **Implementation**: Use the `choice_filter` column in the `survey` sheet.
- **Logic**: `choice_filter = "category_column = ${parent_question}"`.
- **Custom Columns**: You can add custom columns to the `choices` sheet (e.g., `category`, `region_id`, `status`). These columns are not displayed to the user but can be used in `choice_filter` expressions to dynamically filter the list of available options based on previous answers.

## 4. Logic Patterns
### Relevance (`relevant` column)
- **Simple**: `${age} > 18`
- **Choice-based**: `selected(${gender}, 'female')`
- **Complex**: `${age} > 18 and selected(${employment}, 'employed')`

### Constraints (`constraint` column)
- **Range**: `. >= 0 and . <= 120`
- **With Special Values**: `(. >= 0 and . <= 120) or . = -88 or . = -89 or . = -90`
- **Cross-field**: `. <= ${parent_age}`

### Calculations (`calculation` column)
- **Summing**: `${income1} + ${income2} + ${income3}`
- **Conditional**: `if(${age} <<  18, 'Minor', 'Adult')`
