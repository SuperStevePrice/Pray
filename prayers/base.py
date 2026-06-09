"""
prayers/base.py — Base class and shared types for all prayers in Pray.

Each prayer module defines a Prayer instance with:
    - name:             canonical short name (e.g. "ave")
    - title:            full display title (e.g. "Ave Maria")
    - native_titles:    dict of language → native title
    - texts:            dict of language → prayer text
    - voices:           dict of language → {voice_name: say_voice_string}
    - language_aliases: dict of alias → canonical language key
    - latin_note:       optional note printed when Latin is requested
"""

from dataclasses import dataclass
from typing import Optional


# ── Regional voice registry ────────────────────────────────────────────────────
# Standard 8-voice family available across most languages.
# Regional single voices are added per language where available.
# Source: macOS say -v '?' (see docs/say_voices.txt)

def standard_voices(lang_tag: str) -> dict:
    """Build the standard 8-voice roster for a given say language tag."""
    return {
        "Eddy":    f"Eddy ({lang_tag})",
        "Flo":     f"Flo ({lang_tag})",
        "Grandma": f"Grandma ({lang_tag})",
        "Grandpa": f"Grandpa ({lang_tag})",
        "Reed":    f"Reed ({lang_tag})",
        "Rocko":   f"Rocko ({lang_tag})",
        "Sandy":   f"Sandy ({lang_tag})",
        "Shelley": f"Shelley ({lang_tag})",
    }


# Full voice roster per language — call voices_for(language) in prayer modules.
# Merges standard family voices with regional single voices.

REGIONAL_VOICES: dict = {
    "english": {
        **standard_voices("English (US)"),
        # Regional single voices
        "Samantha": "Samantha",           # en_US — classic American
        "Daniel":   "Daniel",             # en_GB — British
        "Karen":    "Karen",              # en_AU — Australian
        "Moira":    "Moira",              # en_IE — Irish
        "Rishi":    "Rishi",              # en_IN — Indian
        "Tessa":    "Tessa",              # en_ZA — South African
    },
    "german": {
        **standard_voices("German (Germany)"),
        "Anna":     "Anna",               # de_DE — single classic voice
    },
    "italian": {
        **standard_voices("Italian (Italy)"),
        "Alice":    "Alice",              # it_IT — single classic voice
    },
    "latin": {
        # No native Latin voice — Italian voices render Church Latin best
        **standard_voices("Italian (Italy)"),
        "Alice":    "Alice",              # it_IT
    },
    "french": {
        **standard_voices("French (France)"),
        "Jacques":  "Jacques",            # fr_FR
        "Thomas":   "Thomas",             # fr_FR
        "Amélie":   "Amélie",             # fr_CA — Canadian French
    },
    "spanish": {
        **standard_voices("Spanish (Spain)"),
        "Mónica":   "Mónica",             # es_ES — Spain
        "Paulina":  "Paulina",            # es_MX — Mexican
    },
    "portuguese": {
        **standard_voices("Portuguese (Brazil)"),
        "Luciana":  "Luciana",            # pt_BR — Brazilian
        "Joana":    "Joana",              # pt_PT — European Portuguese
    },
    "polish": {
        # Only one Polish voice available on macOS
        "Zosia":    "Zosia",
        # Standard names aliased to Zosia for consistency
        "Grandma":  "Zosia",
        "Grandpa":  "Zosia",
        "Eddy":     "Zosia",
        "Flo":      "Zosia",
        "Reed":     "Zosia",
        "Rocko":    "Zosia",
        "Sandy":    "Zosia",
        "Shelley":  "Zosia",
    },
}


def voices_for(language: str) -> dict:
    """Return the full voice roster for a given language.
    Falls back to English voices if language not found."""
    return REGIONAL_VOICES.get(language, REGIONAL_VOICES["english"])


@dataclass
class Prayer:
    name:           str                        # canonical: "ave", "lords"
    title:          str                        # display: "Ave Maria"
    native_titles:  dict                       # language → native title
    texts:          dict                       # language → text
    voices:         dict                       # language → {name: say_string}
    language_aliases: dict                     # alias → canonical language
    latin_note:     str = ""                   # shown when latin requested

    def language_names(self) -> list:
        return list(self.texts.keys())

    def voice_names(self) -> list:
        return list(next(iter(self.voices.values())).keys())

    def resolve_language(self, raw: str) -> Optional[str]:
        """Resolve a raw language string (any case/alias) to canonical key."""
        return self.language_aliases.get(raw.lower(), None)

    def resolve_voice(self, raw: str) -> Optional[str]:
        """Resolve a raw voice name (any case) to canonical key."""
        cap = raw.capitalize()
        names = self.voice_names()
        return cap if cap in names else None
