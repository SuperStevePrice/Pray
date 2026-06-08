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
