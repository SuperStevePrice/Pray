#!/usr/bin/env python3
"""
Deploy Pray - af1a2ce design + PRAYER_AUDIO mapping.
Each prayer gets its own music file.
"""
import json, subprocess
from pathlib import Path
from prayers import PRAYERS

PRAYER_NAMES = {"ave": "Ave Maria", "gloria": "Gloria", "peace": "Instrument of Thy Peace",
    "lords": "Lord's Prayer", "magnificat": "Magnificat", "miserere": "Miserere Psalm 51",
    "nunc": "Nunc Dimittis", "sanctus": "Sanctus", "serenity": "Serenity Prayer",
    "psalm23": "The Lord is My Shepherd"}

PRAYER_IMAGES = {"ave": "ave-maria.png", "lords": "Breaking_of_The_Bread.png",
    "serenity": "serenity.png", "psalm23": "psalm23.png", "peace": "peace.png",
    "nunc": "nunc-dimittis.png", "miserere": "miserere.png", "gloria": "gloria.png",
    "sanctus": "sanctus.png", "magnificat": "magnificat.png"}

PRAYER_AUDIO = {"ave": "ave-maria-gregorian.mp3", "gloria": "vivaldi-gloria-RV-589.mp3",
    "peace": "instrument-of-thy-peace.mp3", "lords": "lords-prayer-mario-lanza.mp3",
    "magnificat": "magnificat-reawaken.mp3", "miserere": "miserere-allegri.mp3",
    "nunc": "nunc-dimittis-gregorian.mp3", "sanctus": "sanctus-gregorian.mp3",
    "serenity": "serenity-prayer.mp3", "psalm23": "psalm23-shepherd.mp3"}

prayers_sorted = sorted(PRAYERS, key=lambda p: PRAYER_NAMES.get(p, p))

prayers_json = {}
for p in prayers_sorted:
    prayer = PRAYERS[p]
    text = prayer.texts.get('english', list(prayer.texts.values())[0] if prayer.texts else '')
    langs = prayer.language_names() if callable(prayer.language_names) else prayer.language_names
    languages = {lang: prayer.texts.get(lang.lower(), '') for lang in langs}
    prayers_json[p] = {'text': text, 'languages': languages}

prayer_names_json = {p: PRAYER_NAMES.get(p, p) for p in prayers_sorted}
prayer_images_json = {p: PRAYER_IMAGES.get(p) for p in prayers_sorted}
prayer_audio_json = {p: PRAYER_AUDIO.get(p) for p in prayers_sorted}

# Get af1a2ce HTML and inject PRAYER_AUDIO
subprocess.run(["git", "show", "af1a2ce:docs/index.html"], stdout=open('/tmp/base.html', 'w'))

with open('/tmp/base.html') as f:
    html = f.read()

# Inject JSON data before closing script tag
inject = f"""
        const PRAYERS_DATA = {json.dumps(prayers_json)};
        const PRAYER_NAMES = {json.dumps(prayer_names_json)};
        const PRAYER_IMAGES = {json.dumps(prayer_images_json)};
        const PRAYER_AUDIO = {json.dumps(prayer_audio_json)};
"""

html = html.replace('const PRAYERS_DATA = ', inject + '        const PRAYERS_DATA_OLD = ')
# Fix the toggleMusic function to use PRAYER_AUDIO
html = html.replace(
    "const audioPath = 'audio/ave-maria-gregorian.mp3';",
    "const audioPath = 'audio/' + PRAYER_AUDIO[this.selectedPrayer];"
)

Path('docs/index.html').write_text(html)
print("✅ Generated docs/index.html (af1a2ce design + PRAYER_AUDIO)")

subprocess.run(["git", "add", "docs/index.html"])
subprocess.run(["git", "commit", "-m", "Hybrid: af1a2ce design + PRAYER_AUDIO mapping"])
subprocess.run(["git", "push"])
print("✅ Committed and pushed")
