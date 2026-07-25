#!/usr/bin/env python3
"""
deployPray.py — dynamic, in-place deploy.

Regenerates the <select id="prayer"> option list, the TEXTS object, and the
PRAYER_IMAGES object inside the CURRENT docs/index.html (sourced from the
prayers/ registry), and refreshes the About-modal version stamp.

Unlike the previous version, this does NOT rebuild the page from a frozen
historical commit. It edits the live page in place, so hand-maintained
features — the Book download table (BOOKS), the QR code, and the
language-aware About modal — are preserved automatically. Only the four
generated regions are touched.

Usage:
    python bin/deployPray.py                    # regenerate, commit, push
    python bin/deployPray.py -m "your message"  # custom commit message
    python bin/deployPray.py --no-push          # commit only, don't push
    python bin/deployPray.py --dry-run          # write docs/index.preview.html; no git
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Resolve the repo root from this file's location (bin/ lives under the root),
# so the script works no matter which directory you run it from.
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
INDEX = REPO_ROOT / "docs" / "index.html"

from prayers import PRAYERS  # noqa: E402  (import after sys.path insert)

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


def build_data():
    """Build the sorted prayer list, TEXTS dict, and images dict from the registry."""
    prayers_sorted = sorted(PRAYERS.keys(), key=lambda k: PRAYER_NAMES.get(k, k))

    texts_dict = {}
    for key in prayers_sorted:
        prayer = PRAYERS[key]
        langs = (prayer.language_names()
                 if callable(prayer.language_names) else prayer.language_names)
        texts_dict[key] = {lang.lower(): prayer.texts.get(lang.lower(), '') for lang in langs}

    images_dict = {key: PRAYER_IMAGES[key] for key in prayers_sorted if key in PRAYER_IMAGES}
    return prayers_sorted, texts_dict, images_dict


def main():
    ap = argparse.ArgumentParser(description="Dynamic in-place deploy for Pray.")
    ap.add_argument("-m", "--message",
                    default="Deploy Pray: regenerate prayer list, texts, images; refresh version stamp")
    ap.add_argument("--no-push", action="store_true", help="commit but do not push")
    ap.add_argument("--dry-run", action="store_true",
                    help="write docs/index.preview.html for inspection; no write to index.html, no git")
    args = ap.parse_args()

    if not INDEX.exists():
        sys.exit(f"✋ Not found: {INDEX} — is this the Pray repo?")

    prayers_sorted, texts_dict, images_dict = build_data()
    html = INDEX.read_text(encoding="utf-8")

    # ── Safety guard: confirm we're editing the real, current page ─────────────
    required = ['const TEXTS = {', '<select id="prayer">', 'const PRAYER_IMAGES = {']
    missing = [r for r in required if r not in html]
    if missing:
        sys.exit(f"✋ Aborting: docs/index.html is missing {missing} — unexpected markup, nothing changed.")
    # Non-fatal: warn if the hand-maintained features aren't where we expect them.
    for feat in ('const BOOKS', 'aboutLangSel', 'about-qr'):
        if feat not in html:
            print(f"⚠️  Heads-up: '{feat}' not found in the current page — it may be older than expected.")

    ok = True

    # ── <select id="prayer"> options ──────────────────────────────────────────
    new_options = "\n".join(
        f'        <option value="{k}">{PRAYER_NAMES.get(k, k)}</option>' for k in prayers_sorted
    )
    sel = re.compile(r'(<select id="prayer">\n)(.*?)(\n\s*</select>)', re.S)
    if sel.search(html):
        html = sel.sub(lambda m: m.group(1) + new_options + m.group(3), html, count=1)
        print(f'✅ Rewrote <select id="prayer"> with {len(prayers_sorted)} options')
    else:
        print('⚠️  Could not rewrite <select id="prayer">'); ok = False

    # ── const TEXTS = {...}; ──────────────────────────────────────────────────
    new_texts = f"const TEXTS = {json.dumps(texts_dict, indent=2, ensure_ascii=False)};\n"
    tx = re.compile(r'const TEXTS = \{.*?\n\};\n', re.S)
    if tx.search(html):
        html = tx.sub(lambda m: new_texts, html, count=1)
        print(f"✅ Rewrote TEXTS with {len(texts_dict)} prayers")
    else:
        print("⚠️  Could not rewrite TEXTS"); ok = False

    # ── const PRAYER_IMAGES = {...}; ──────────────────────────────────────────
    new_images = f"const PRAYER_IMAGES = {json.dumps(images_dict, ensure_ascii=False)};"
    im = re.compile(r'const PRAYER_IMAGES = \{.*?\};')
    if im.search(html):
        html = im.sub(lambda m: new_images, html, count=1)
        print(f"✅ Rewrote PRAYER_IMAGES with {len(images_dict)} entries")
    else:
        print("⚠️  Could not rewrite PRAYER_IMAGES"); ok = False

    # ── About-modal version stamp ─────────────────────────────────────────────
    commit_hash = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    ).stdout.strip()
    stamp = f"Version {datetime.now().strftime('%Y-%m-%d %H:%M')} · {commit_hash}"
    vp = re.compile(r"Version \d{4}-\d{2}-\d{2} \d{2}:\d{2} · [0-9a-fA-F]{6,}")
    if vp.search(html):
        html = vp.sub(stamp, html)
        print(f"✅ Updated version stamp → {stamp}")
    else:
        print("⚠️  No existing version stamp found (left unchanged)")

    if not ok:
        sys.exit("✋ Aborting before write: a required block was not rewritten. Nothing changed, nothing committed.")

    # ── Dry run: write a preview and stop ─────────────────────────────────────
    if args.dry_run:
        preview = REPO_ROOT / "docs" / "index.preview.html"
        preview.write_text(html, encoding="utf-8")
        print(f"📝 Dry run — wrote {preview.relative_to(REPO_ROOT)} for inspection. No git actions taken.")
        return

    # ── Write, commit, push ───────────────────────────────────────────────────
    INDEX.write_text(html, encoding="utf-8")
    print(f"✅ Wrote {INDEX.relative_to(REPO_ROOT)}")
    subprocess.run(["git", "add", str(INDEX)], cwd=REPO_ROOT)
    commit = subprocess.run(["git", "commit", "-m", args.message], cwd=REPO_ROOT)
    if commit.returncode != 0:
        print("ℹ️  Nothing to commit (index.html unchanged).")
        return
    if args.no_push:
        print("✅ Committed (push skipped).")
    else:
        subprocess.run(["git", "push"], cwd=REPO_ROOT)
        print("✅ Committed and pushed.")


if __name__ == "__main__":
    main()
