#!/usr/bin/env python3
"""
installPray.py — Install pray.py to ~/bin with backup and PATH verification.

Usage:
    python3 installPray.py
"""

import os
import shutil
import stat
import sys
from datetime import datetime
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────

HOME        = Path.home()
BIN         = HOME / "bin"
BACKUP      = BIN / "backup"
PRAY_SRC    = Path(__file__).parent / "bin" / "pray.py"
PRAY_DST    = BIN / "pray.py"
PRAYERS_SRC = Path(__file__).parent / "prayers"
PRAYERS_DST = BIN / "prayers"
ALPHA       = BACKUP / "pray.py.alpha"

# ── Helpers ────────────────────────────────────────────────────────────────────

def make_executable(path: Path) -> None:
    path.chmod(stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP |
               stat.S_IROTH | stat.S_IXOTH)

def check_path() -> None:
    path_dirs = os.environ.get("PATH", "").split(":")
    if str(BIN) not in path_dirs:
        print(f"\n  ⚠️   Warning: {BIN} is not on your PATH.")
        print("      Add this to your shell profile (~/.kshrc or equivalent):")
        print(f"      export PATH=\"$HOME/bin:$PATH\"\n")
    else:
        print(f"  ✅  {BIN} is on your PATH.")

# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    print("\ninstallPray.py — Pray Installer")
    print("=" * 60)
    print('  "Ask, and it shall be given you; seek, and ye shall find."')
    print("                                          — Matthew 7:7\n")

    # ── Verify source exists ───────────────────────────────────────────────────
    if not PRAY_SRC.exists():
        print(f"  ❌  Source not found: {PRAY_SRC}")
        print("      Run installPray.py from the root of the Pray project.")
        sys.exit(1)
    print(f"  📄  Source   : {PRAY_SRC}")

    # ── Create ~/bin if needed ─────────────────────────────────────────────────
    if not BIN.exists():
        print(f"  📁  Creating : {BIN}")
        BIN.mkdir(parents=True, exist_ok=True)
        make_executable(BIN)
        print(f"  ✅  Created  : {BIN}")
    else:
        print(f"  ✅  Found    : {BIN}")

    # ── Create ~/bin/backup if needed ─────────────────────────────────────────
    if not BACKUP.exists():
        print(f"  📁  Creating : {BACKUP}")
        BACKUP.mkdir(parents=True, exist_ok=True)
        print(f"  ✅  Created  : {BACKUP}")
    else:
        print(f"  ✅  Found    : {BACKUP}")

    # ── Alpha backup ───────────────────────────────────────────────────────────
    if not ALPHA.exists():
        shutil.copy2(PRAY_SRC, ALPHA)
        make_executable(ALPHA)
        print(f"\n  ✝️   Alpha backup (the first): {ALPHA}")
    else:
        print(f"\n  ✝️   Alpha backup already exists: {ALPHA}")

    # ── Handle existing ~/bin/pray.py ─────────────────────────────────────────
    if PRAY_DST.exists():
        print(f"\n  ⚠️   {PRAY_DST} already exists.")
        answer = input("      Install new version? [y/N] ").strip().lower()

        if answer != "y":
            print("\n  Installation cancelled. Existing pray.py unchanged.")
            sys.exit(0)

        timestamp   = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = BACKUP / f"pray.py.{timestamp}"
        shutil.copy2(PRAY_DST, backup_path)
        make_executable(backup_path)
        print(f"  💾  Backed up existing: {backup_path}")

    # ── Install pray.py ────────────────────────────────────────────────────────
    shutil.copy2(PRAY_SRC, PRAY_DST)
    make_executable(PRAY_DST)
    print(f"\n  ✅  Installed : {PRAY_DST}")

    # ── Install prayers/ module ────────────────────────────────────────────────
    if PRAYERS_DST.exists():
        shutil.rmtree(PRAYERS_DST)
    shutil.copytree(PRAYERS_SRC, PRAYERS_DST)
    print(f"  ✅  Installed : {PRAYERS_DST}/")

    # ── Verify ────────────────────────────────────────────────────────────────
    print("\n  Verification:")
    os.system(f"ls -l {PRAY_DST}")

    print()
    check_path()

    print("\n  Pray. Installation complete.")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
