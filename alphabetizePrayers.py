#!/usr/bin/env python3
"""Alphabetize prayers ignoring 'The' at start"""
import subprocess
from pathlib import Path

# Prayer order, alphabetically (ignoring "The" at start)
PRAYER_ORDER = [
    "ave",           # Ave Maria
    "gloria",        # Gloria
    "peace",         # Instrument of Thy Peace
    "magnificat",    # Magnificat
    "miserere",      # Miserere Psalm 51
    "nunc",          # Nunc Dimittis
    "psalm23",       # The Lord is My Shepherd (L - Lord)
    "lords",         # The Lord's Prayer (L - Lord)
    "sanctus",       # Sanctus
    "serenity",      # Serenity Prayer
]

PRAYER_NAMES = {
    "ave": "Ave Maria",
    "gloria": "Gloria",
    "peace": "Instrument of Thy Peace",
    "lords": "The Lord's Prayer",
    "magnificat": "Magnificat",
    "miserere": "Miserere Psalm 51",
    "nunc": "Nunc Dimittis",
    "sanctus": "Sanctus",
    "serenity": "Serenity Prayer",
    "psalm23": "The Lord is My Shepherd"
}

path = Path.home() / "Projects/Pray/docs/index.html"
html = path.read_text()

# Generate new options in alphabetical order
new_options = "\n".join([
    f'      <option value="{key}">{PRAYER_NAMES[key]}</option>'
    for key in PRAYER_ORDER
])

# Find and replace old options (they're between the two select lines)
import re
old_pattern = r'<option value="ave">.*?</option>\s*\n\s*<option value="gloria">.*?</option>.*?<option value="psalm23">.*?</option>'
if re.search(old_pattern, html, re.DOTALL):
    html = re.sub(old_pattern, new_options, html, flags=re.DOTALL)
    print("✅ Reordered prayer options")
else:
    print("⚠️ Could not find prayer options to reorder")

path.write_text(html)
subprocess.run(["git", "add", "docs/index.html"], cwd=str(Path.home() / "Projects/Pray"))
subprocess.run(["git", "commit", "-m", "Alphabetize prayers (ignoring 'The')"], cwd=str(Path.home() / "Projects/Pray"))
subprocess.run(["git", "push"], cwd=str(Path.home() / "Projects/Pray"))
print("✅ Committed and pushed")
