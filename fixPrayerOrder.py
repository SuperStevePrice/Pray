#!/usr/bin/env python3
"""Fix prayer order: Lord prayers should be between I and M alphabetically"""
import subprocess
from pathlib import Path

path = Path.home() / "Projects/Pray/docs/index.html"
html = path.read_text()

# Remove the Lord prayers from wherever they are
html = html.replace('      <option value="psalm23">The Lord is My Shepherd</option>\n', '')
html = html.replace('      <option value="lords">The Lord\'s Prayer</option>\n', '')

# Insert them after "Instrument of Thy Peace"
insert_after = '      <option value="peace">Instrument of Thy Peace</option>'
lord_options = '''      <option value="psalm23">The Lord is My Shepherd</option>
      <option value="lords">The Lord's Prayer</option>'''

if insert_after in html:
    html = html.replace(
        insert_after,
        insert_after + '\n' + lord_options
    )
    print("✅ Moved Lord prayers to correct position (after I, before M)")
else:
    print("⚠️ Could not find insertion point")

path.write_text(html)
subprocess.run(["git", "add", "docs/index.html"], cwd=str(Path.home() / "Projects/Pray"))
subprocess.run(["git", "commit", "-m", "Fix: Move Lord prayers to correct alphabetical position (I → L → M)"], cwd=str(Path.home() / "Projects/Pray"))
subprocess.run(["git", "push"], cwd=str(Path.home() / "Projects/Pray"))
print("✅ Committed and pushed")
