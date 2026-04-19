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
