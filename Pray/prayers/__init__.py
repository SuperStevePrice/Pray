"""
prayers/__init__.py — Prayer registry.

Import all prayers here and register them in PRAYERS dict.
To add a new prayer: create a new module, import it here, add to PRAYERS.
"""

from .ave_maria    import AveMaria
from .lords_prayer import LordsPrayer
from .base         import Prayer

# ── Registry ───────────────────────────────────────────────────────────────────
# Key is the canonical --prayer argument value.

PRAYERS: dict[str, Prayer] = {
    "ave":   AveMaria,
    "lords": LordsPrayer,
}

# Aliases for --prayer argument
PRAYER_ALIASES: dict[str, str] = {
    # Ave Maria
    "ave":          "ave",
    "ave maria":    "ave",
    "avemaria":     "ave",
    "hail mary":    "ave",
    "hailmary":     "ave",
    # Lord's Prayer
    "lords":        "lords",
    "lord":         "lords",
    "lords prayer": "lords",
    "lordsprayer":  "lords",
    "our father":   "lords",
    "ourfather":    "lords",
    "paternoster":  "lords",
    "pater noster": "lords",
    "vaterunser":   "lords",
    "padre nostro": "lords",
    "notre pere":   "lords",
    "notre père":   "lords",
}

__all__ = ["Prayer", "PRAYERS", "PRAYER_ALIASES"]
