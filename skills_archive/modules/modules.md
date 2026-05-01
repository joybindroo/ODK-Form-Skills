# ODK Reusable Modules

This library contains standardized XLSForm blocks for common survey sections. Use these as templates to ensure consistency across instruments.

## 1. Form Header & Metadata
Standard fields for every form to ensure traceability and quality control.

| type | name | label | appearance | calculation/constraint |
| :--- | :--- | :--- | :--- | :--- |
| `start` | `start` | | | |
| `end` | `end` | | | |
| `deviceid` | `deviceid` | | | |
| `phonenumber` | `phonenumber` | | | |
| `username` | `username` | | | |
| `calculate` | `calc_duration` | | | `string-length(now())` (or custom duration logic) |

## 2. Informed Consent
A standard gate to ensure ethical compliance.

| type | name | label | appearance | relevant |
| :--- | :--- | :--- | :--- | :--- |
| `note` | `consent_note` | [Insert Consent Script Here] | | |
| `select_one yesno` | `consent_given` | Do you agree to participate in this survey? | `horizontal` | |
| `note` | `consent_fail` | Thank you for your time. We cannot proceed without consent. | | `${consent_given} = 0` |

## 3. Household Roster (Basic)
A repeat group to capture household members.

| type | name | label | appearance | constraint |
| :--- | :--- | :--- | :--- | :--- |
| `integer` | `hh_size` | Total number of members in the household | | `. >= 1` |
| `begin_repeat` | `grp_hh_roster` | Household Member Details | `repeat_count=${hh_size}` | |
| `text` | `mem_name` | Name of member | | |
| `select_one gender` | `mem_gender` | Gender | `horizontal` | |
| `integer` | `mem_age` | Age in years | | `(. >= 0 and . <= 120) or . = -88 or . = -89` |
| `select_one relation` | `mem_relation` | Relationship to head | | |
| `end_repeat` | | | | |

## 4. Geographic Identification
Cascading selects for location tracking.

| type | name | label | appearance | choice_filter |
| :--- | :--- | :--- | :--- | :--- |
| `select_one state` | `loc_state` | Select State | `minimal` | |
| `select_one district` | `loc_district` | Select District | `minimal` | `state = ${loc_state}` |
| `select_one village` | `loc_village` | Select Village | `minimal` | `district = ${loc_district}` |
| `geopoint` | `loc_gps` | Capture GPS Location | | |

## 5. Asset/Consumption Checklist
Using `select_multiple` for rapid inventory.

| type | name | label | appearance | |
| :--- | :--- | :--- | :--- | :--- |
| `select_multiple assets` | `hh_assets` | Which of the following assets does the household own? | `multiline` | |
| `calculate` | `calc_asset_count` | Total assets owned | | `count-selected(${hh_assets})` |

## 6. Education & Employment Profile
Standardized blocks for capturing socio-economic and professional status.

### A. Education Details
| type | name | label | appearance | relevant |
| :--- | :--- | :--- | :--- | :--- |
| `select_one edu_level` | `edu_highest_level` | Highest level of education completed | `minimal` | |
| `text` | `edu_institution` | Name of the last institution attended | | `${edu_highest_level} != 'none'` |
| `integer` | `edu_year_completed` | Year of completion | | `${edu_highest_level} != 'none'` |
| `select_one edu_stream` | `edu_stream` | Field of study / Stream | `minimal` | `${edu_highest_level} = 'degree' or ${edu_highest_level} = 'diploma'` |

### B. Employment & Occupation
| type | name | label | appearance | relevant |
| :--- | :--- | :--- | :--- | :--- |
| `select_one emp_status` | `emp_status` | Current employment status | `horizontal` | |
| `select_one occ_category` | `occ_category` | Broad occupational category | `minimal` | `${emp_status} = 'employed'` |
| `text` | `occ_job_title` | Specific job title / Designation | | `${emp_status} = 'employed'` |
| `integer` | `emp_years_exp` | Total years of professional experience | | `${emp_status} = 'employed'` |
| `integer` | `emp_monthly_income` | Average monthly income | | `${emp_status} = 'employed'` |

## 7. Technical Skills & Competencies
A matrix-style approach to capture skill proficiency.

### A. Skill Inventory
| type | name | label | appearance | |
| :--- | :--- | :--- | :--- | :--- |
| `select_multiple tech_skills` | `skills_known` | Which of the following technical skills do you possess? | `multiline` | |

### B. Proficiency Matrix (Dynamic)
Use a repeat group filtered by the `skills_known` selection to capture proficiency for each selected skill.

| type | name | label | appearance | relevant |
| :--- | :--- | :--- | :--- | :--- |
| `begin_repeat` | `grp_skill_proficiency` | Skill Proficiency Details | | |
| `calculate` | `curr_skill` | Current Skill | | |
| `note` | `skill_note` | Rate your proficiency for: ${curr_skill} | | |
| `select_one prof_level` | `prof_level` | Proficiency Level (Beginner to Expert) | `horizontal` | |
| `integer` | `years_using_skill` | Years of experience with this skill | | |
| `end_repeat` | | | | | |
