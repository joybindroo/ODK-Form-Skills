# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed

- Moved `requirements.txt` into the skill directory (`skills/odk-xlsform/`) so
  the skill is self-contained. Installing the skill via the documented
  `cp -r skills/odk-xlsform ...` now carries its dependencies, and
  `pip install -r requirements.txt` resolves from the skill dir where agents
  run. Updated the README structure/install docs and `SKILL.md` accordingly.

### Fixed

- `extract_template_metadata` in `scripts/xlsform_generator.py` raised
  `'str' object has no attribute 'value'` and returned `None` on every call —
  it combined `iter_rows(values_only=True)` with cell-object indexing. It now
  reads the header value tuple directly and drops empty trailing columns.
- Stripped a trailing space from the `'audio '` header in the `survey` sheet
  of `templates/odk_template.xlsx` (the documented source of truth for column
  order).
