#!/usr/bin/env python3
"""
RETIRED (safe no-op) — Add the Apostles' Creed image, then commit and push.

Superseded by bin/deployPray.py, which regenerates the prayer <option> list,
its order, and its labels from the prayers/ registry on every deploy.

Why this was retired:
It was shell commands saved with a .py extension (it errors under python3), and the image it added is already committed.

This stub has been neutralized: it does not read or write any file and does
not run git. It cannot alter docs/index.html or push anything.

To change the prayer list, order, or labels, edit prayers/ (and, for the
visible label, PRAYER_NAMES in bin/deployPray.py), then run:

    python bin/deployPray.py            # add --dry-run to preview first

The original one-shot logic remains available in git history if ever needed.
"""
import sys

print(__doc__.strip())
print("\nNo changes made. Nothing written, nothing committed, nothing pushed.")
sys.exit(0)
