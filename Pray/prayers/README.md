# Prayers

This folder contains the prayer definitions for Pray.

Each prayer is a Python module that defines a `Prayer` instance
with texts, voices, and language aliases.

## Current Prayers

| File              | Key     | Title            |
|-------------------|---------|-----------------|
| `ave_maria.py`    | `ave`   | Ave Maria        |
| `lords_prayer.py` | `lords` | Lord's Prayer    |

## Adding a Prayer

1. Copy `ave_maria.py` as a template
2. Fill in the `Prayer(...)` fields:
   - `name` — short CLI key (e.g. `"gloria"`)
   - `title` — display name (e.g. `"Gloria in Excelsis"`)
   - `native_titles` — name in each language
   - `texts` — prayer text per language
   - `voices` — voice roster per language
   - `language_aliases` — all accepted spellings
3. Import and register in `__init__.py`:
   ```python
   from .gloria import Gloria
   PRAYERS["gloria"] = Gloria
   PRAYER_ALIASES["gloria"] = "gloria"
   ```
4. Run `python3 testPray.py --prayer gloria` to verify

## Candidate Future Prayers

- Gloria in Excelsis
- Magnificat
- Te Deum
- Salve Regina
- Anima Christi
- Hail Holy Queen
- Nicene Creed
