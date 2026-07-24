#!/usr/bin/env python3
"""
Deploy Pray - af1a2ce design.
Regenerates the <select id="prayer"> option list, the TEXTS object, and the
PRAYER_IMAGES object directly from prayers/, so every registered prayer
shows up automatically. Also stamps a live version string into the About
modal.
"""
import json, re, subprocess
from datetime import datetime
from pathlib import Path
from prayers import PRAYERS

# Friendly, mixed-case labels shown in the dropdown. The <option value="...">
# still uses the raw key (so TEXTS[prayerSel.value] lookups keep working) —
# only the visible text changes.
PRAYER_NAMES = {
    "ave": "Ave Maria",
    "ave_verum": "Ave Verum Corpus",
    "gloria": "Gloria",
    "lords": "Lord's Prayer",
    "magnificat": "Magnificat",
    "miserere": "Miserere — Psalm 51",
    "nunc": "Nunc Dimittis",
    "peace": "Peace Prayer",
    "psalm23": "23rd Psalm",
    "sanctus": "Sanctus",
    "serenity": "Serenity Prayer",
}

# Map of prayer key -> image filename. Add an entry here whenever you add a
# new prayer with its own artwork; prayers without an entry just won't show
# an image (no crash).
PRAYER_IMAGES = {
    "ave": "ave-maria.png",
    "ave_verum": "ave-verum-corpus.png",
    "lords": "Breaking_of_The_Bread.png",
    "serenity": "serenity.png",
    "psalm23": "psalm23.png",
    "peace": "peace.png",
    "nunc": "nunc-dimittis.png",
    "miserere": "miserere.png",
    "gloria": "gloria.png",
    "sanctus": "sanctus.png",
    "magnificat": "magnificat.png",
}

prayers_sorted = sorted(PRAYERS.keys(), key=lambda k: PRAYER_NAMES.get(k, k))

# Build TEXTS = { key: { lang: text, ... }, ... } from the actual Prayer objects
texts_dict = {}
for key in prayers_sorted:
    prayer = PRAYERS[key]
    langs = prayer.language_names() if callable(prayer.language_names) else prayer.language_names
    texts_dict[key] = {lang.lower(): prayer.texts.get(lang.lower(), '') for lang in langs}

images_dict = {key: PRAYER_IMAGES[key] for key in prayers_sorted if key in PRAYER_IMAGES}

# Get af1a2ce HTML as the base template
subprocess.run(["git", "show", "af1a2ce:docs/index.html"], stdout=open('/tmp/base.html', 'w'))
with open('/tmp/base.html') as f:
    html = f.read()

# ── Replace the <select id="prayer"> option list (mixed-case labels) ───────
new_options = "\n".join(
    f'        <option value="{key}">{PRAYER_NAMES.get(key, key)}</option>' for key in prayers_sorted
)
select_pattern = re.compile(r'(<select id="prayer">\n)(.*?)(\n\s*</select>)', re.S)
if select_pattern.search(html):
    html = select_pattern.sub(lambda m: m.group(1) + new_options + m.group(3), html, count=1)
    print(f"✅ Rewrote <select id=\"prayer\"> with {len(prayers_sorted)} options (friendly names)")
else:
    print("⚠️  Could not find <select id=\"prayer\">...</select> — check docs/index.html markup.")

# ── Replace const TEXTS = {...}; ─────────────────────────────────────────────
texts_pattern = re.compile(r'const TEXTS = \{.*?\n\};\n', re.S)
new_texts_js = f"const TEXTS = {json.dumps(texts_dict, indent=2, ensure_ascii=False)};\n"
if texts_pattern.search(html):
    html = texts_pattern.sub(lambda m: new_texts_js, html, count=1)
    print(f"✅ Rewrote TEXTS with {len(texts_dict)} prayers")
else:
    print("⚠️  Could not find 'const TEXTS = {...};' block — check docs/index.html.")

# ── Replace const PRAYER_IMAGES = {...}; ────────────────────────────────────
images_pattern = re.compile(r'const PRAYER_IMAGES = \{.*?\};')
new_images_js = f"const PRAYER_IMAGES = {json.dumps(images_dict, ensure_ascii=False)};"
if images_pattern.search(html):
    html = images_pattern.sub(lambda m: new_images_js, html, count=1)
    print(f"✅ Rewrote PRAYER_IMAGES with {len(images_dict)} entries")
else:
    print("⚠️  Could not find 'const PRAYER_IMAGES = {...};' — check docs/index.html.")

# ── Remove the non-functional Music button and audio element ───────────────
# docs/audio/ doesn't exist and never has — the <audio> tag points at a file
# that 404s for every prayer, so the button has never actually played
# anything. Strip it out entirely rather than leave dead UI in place.
audio_tag_pattern = re.compile(r'<audio id="gregorian-audio" loop>.*?</audio>\n?', re.S)
html, n = audio_tag_pattern.subn('', html)
print(f"✅ Removed <audio id=\"gregorian-audio\"> element ({n} found)")

music_button_pattern = re.compile(r'<button[^>]*id="btn-music"[^>]*>.*?</button>\n?', re.S)
html, n = music_button_pattern.subn('', html)
print(f"✅ Removed Music <button> ({n} found)")

js_const_pattern = re.compile(
    r"const btnMusic = document\.getElementById\('btn-music'\);\n"
    r"const audio = document\.getElementById\('gregorian-audio'\);\n"
)
html, n = js_const_pattern.subn('', html)
print(f"✅ Removed btnMusic/audio JS const declarations ({n} found)")

js_handler_pattern = re.compile(
    r"btnMusic\.addEventListener\('click', \(\) => \{.*?\}\);\n", re.S
)
html, n = js_handler_pattern.subn('', html)
print(f"✅ Removed btnMusic click handler ({n} found)")

# ── Update the "Version" stamp shown in the About Pray modal ───────────────
commit_hash = subprocess.run(
    ["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True
).stdout.strip()
deploy_time = datetime.now().strftime("%Y-%m-%d %H:%M")
new_version_line = f"Version {deploy_time} · {commit_hash}"
version_pattern = re.compile(r"Version \d{4}-\d{2}-\d{2} \d{2}:\d{2} · [0-9a-fA-F]{6,}")
if version_pattern.search(html):
    html = version_pattern.sub(new_version_line, html)
    print(f"✅ Updated version stamp → {new_version_line}")
else:
    print("⚠️  Could not find an existing 'Version ...' string to replace.")

Path('docs/index.html').write_text(html)
print("✅ Generated docs/index.html")
subprocess.run(["git", "add", "docs/index.html"])
subprocess.run(["git", "commit", "-m", "Remove non-functional Music button (no audio files exist)"])
subprocess.run(["git", "push"])
print("✅ Committed and pushed")
