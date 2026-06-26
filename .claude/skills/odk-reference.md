# /odk-reference

Access ODK Form Skills standards, naming conventions, and reusable module templates.

## Usage

```
/odk-reference [section]
```

Where section is one of:
- `naming` — Variable naming conventions (snake_case, prefixes, module structure)
- `special-values` — Standard missing/NA codes (-88, -89, -90, 99)
- `cascading` — Hierarchical choice list patterns (State → District → Village)
- `modules` — Reusable form blocks (household roster, consent, demographics, etc.)
- `constraints` — Constraint patterns for numeric fields, dates, etc.
- `xpath` — Common XPath expressions for `relevant` and `constraint` logic
- `pitfalls` — Common mistakes and how to avoid them (formula stripping, choice value types, etc.)
- `all` — Full technical reference

## Quick Reference

**Variable Naming:**
```
snake_case with module prefix:
  demog_age, demog_gender     (demographics)
  hh_size, hh_roster          (household)
  agri_plot_area, agri_yield  (agriculture)
  grp_*                       (repeat groups)
  calc_*                      (calculated fields)
```

**Special Values:**
```
-88 = Don't know
-89 = Refused
-90 = Not applicable
99 = Other (specify)

Constraint: . >= 0 or . = -88 or . = -89 or . = -90
```

**Cascading Selects:**
1. Add filter columns to `choices` sheet (e.g., `state`, `district`)
2. Use `choice_filter` in `survey` sheet (e.g., `state = ${state}`)
3. Pass choices as dict to generator: `{'state': [...], 'city': [...]}`

## Reusable Modules

Standardized blocks available:
- **Header/Metadata**: `start`, `end`, `deviceid`, `phonenumber`, `username`, `calc_duration`
- **Informed Consent**: `consent_note` → `consent_given` → `consent_fail`
- **Household Roster**: `hh_size` → `begin_repeat` (`grp_hh_roster`) → member fields
- **Geographic ID**: Cascading `loc_state` → `loc_district` → `loc_village` + `loc_gps`
- **Asset Checklist**: `select_multiple assets` → `calc_asset_count`
- **Socio-Economic**: Education levels, employment categories, income sources
- **Technical Skills**: Skill proficiency tracking with repeat group

## Key Files

| File | Purpose |
|---|---|
| `skills.md` | Complete operational manual (all sections above) |
| `references/technical_reference.md` | Technical details, XPath patterns, implementation pitfalls |
| `skills_archive/conventions/conventions.md` | Historical naming standards |
| `skills_archive/modules/modules.md` | Reusable form modules |
| `templates/schema.json` | Field type schema |
| `templates/field_types.json` | Available ODK field types |

## Learn More

Read the full documentation in `skills.md` for:
- Complete naming convention guide
- Special value constraint patterns
- Validation pipeline steps
- Analysis workflow (pyODKmcp + database querying)
- Full module templates with examples
