#!/usr/bin/env python3
"""
testPray.py — Test suite for pray.py.

Rolls through every prayer, language, and voice combination,
runs each at high speed (rate 175), captures output,
and writes a timestamped log to logs/.

Usage:
    python3 testPray.py                    # test all prayers
    python3 testPray.py --prayer ave       # test Ave Maria only
    python3 testPray.py --prayer lords     # test Lord's Prayer only
    python3 testPray.py --dry-run          # show what would be tested, no audio
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# ── Setup ──────────────────────────────────────────────────────────────────────

ROOT     = Path(__file__).parent
BIN      = ROOT / "bin" / "pray.py"
LOGS_DIR = ROOT / "logs"
RATE     = 175   # fast — testing existence, not quality

sys.path.insert(0, str(ROOT))
from prayers import PRAYERS, PRAYER_ALIASES
from prayers.base import Prayer

# ── Test runner ────────────────────────────────────────────────────────────────

def run_test(prayer: Prayer, language: str, voice: str, dry_run: bool) -> tuple[bool, str]:
    """
    Run a single test case. Returns (success, message).
    """
    label = f"{prayer.name} {language} {voice}"

    if dry_run:
        return True, f"dry-run: {label}"

    voice_str = prayer.voices[language].get(voice)
    if not voice_str:
        return False, f"error: {label} — voice not found in roster"

    text = prayer.texts[language].replace("\n", " ")

    try:
        result = subprocess.run(
            ["say", "-v", voice_str, "-r", str(RATE), text],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode == 0:
            return True, f"good: {label}"
        else:
            err = result.stderr.strip().replace("\n", " ")
            return False, f"error: {label} — {err}"
    except subprocess.TimeoutExpired:
        return False, f"error: {label} — timed out"
    except FileNotFoundError:
        return False, f"error: {label} — 'say' command not found (macOS only)"


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="testPray.py",
        description="Test suite for pray.py — exercises all prayer/language/voice combinations.",
    )
    parser.add_argument(
        "--prayer", "-p",
        default=None,
        choices=list(PRAYERS.keys()),
        help="Test a single prayer only.",
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Show what would be tested without playing audio.",
    )
    args = parser.parse_args()

    # ── Setup log file ─────────────────────────────────────────────────────────
    LOGS_DIR.mkdir(exist_ok=True)
    timestamp  = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path   = LOGS_DIR / f"testPray_{timestamp}.log"

    prayers_to_test = (
        {args.prayer: PRAYERS[args.prayer]}
        if args.prayer
        else PRAYERS
    )

    # ── Pre-calculate total test count ────────────────────────────────────────
    total_tests = 0
    for prayer in prayers_to_test.values():
        for language in prayer.language_names():
            seen: set[str] = set()
            for voice_name in prayer.voice_names():
                voice_str = prayer.voices[language].get(voice_name, "")
                if voice_str not in seen:
                    seen.add(voice_str)
                    total_tests += 1

    lines   = []
    passed  = 0
    failed  = 0
    skipped = 0
    current = 0

    header = (
        f"testPray.py — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"{'─' * 60}\n"
        f"Prayers : {', '.join(prayers_to_test.keys())}\n"
        f"Total   : {total_tests} tests\n"
        f"Rate    : {RATE} wpm\n"
        f"Dry run : {args.dry_run}\n"
        f"{'─' * 60}\n"
    )
    print(header)
    lines.append(header)

    for prayer_key, prayer in prayers_to_test.items():
        section = f"\n[{prayer.title}]\n"
        print(section)
        lines.append(section)

        for language in prayer.language_names():
            tested_voice_strings: set[str] = set()
            for voice_name in prayer.voice_names():
                voice_str = prayer.voices[language].get(voice_name, "")
                if voice_str in tested_voice_strings:
                    skipped += 1
                    continue
                tested_voice_strings.add(voice_str)

                current += 1
                pct = int(current / total_tests * 100)

                success, message = run_test(prayer, language, voice_name, args.dry_run)
                # Percentage only to stdout, not to log
                print(f"  [{pct:3d}%] {message}")
                lines.append(f"  {message}\n")
                if success:
                    passed += 1
                else:
                    failed += 1

    # ── Summary ────────────────────────────────────────────────────────────────
    summary = (
        f"\n{'─' * 60}\n"
        f"Summary : {passed} passed, {failed} failed, {skipped} skipped (duplicate aliases)\n"
        f"Log     : {log_path}\n"
        f"{'─' * 60}\n"
    )
    print(summary)
    lines.append(summary)

    # ── Write log ──────────────────────────────────────────────────────────────
    with open(log_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
