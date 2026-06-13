#!/usr/bin/env python3
"""Update Lord's Prayer to The Lord's Prayer"""
import subprocess
from pathlib import Path

path = Path.home() / "Projects/Pray/docs/index.html"
html = path.read_text()

# 1. Update the option display text
old_option = '<option value="lords">Lord\'s Prayer</option>'
new_option = '<option value="lords">The Lord\'s Prayer</option>'
html = html.replace(old_option, new_option)
print("✅ Updated option text")

# 2. Update PRAYER_NAMES constant
old_names = '"lords": "Lord\'s Prayer"'
new_names = '"lords": "The Lord\'s Prayer"'
html = html.replace(old_names, new_names)
print("✅ Updated PRAYER_NAMES")

path.write_text(html)
subprocess.run(["git", "add", "docs/index.html"], cwd=str(Path.home() / "Projects/Pray"))
subprocess.run(["git", "commit", "-m", 'Rename: "Lord\'s Prayer" → "The Lord\'s Prayer"'], cwd=str(Path.home() / "Projects/Pray"))
subprocess.run(["git", "push"], cwd=str(Path.home() / "Projects/Pray"))
print("✅ Committed and pushed")
