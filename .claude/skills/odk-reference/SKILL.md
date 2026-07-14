---
name: odk-reference
description: Look up ODK Form Skills standards — variable naming conventions, standardized special values, cascading select patterns, reusable form modules, constraint and XPath patterns, and common pitfalls. Use when the user asks how to name variables, which missing-value codes to use, how to build hierarchical choice lists, what reusable modules exist, or invokes /odk-reference. Read-only reference lookup.
allowed-tools: Read, Glob, Grep
---

# odk-reference

Access ODK Form Skills standards, naming conventions, and reusable module templates.

## Sections

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

- Read `skills.md` for the full operational manual.
- Query the `odk-docs` MCP server (`https://odk-docs.mcp.kapa.ai`) for anything beyond these references — official ODK docs and community forum knowledge.
