"""
prayers/__init__.py — Prayer registry.
Import all prayers here and register them in PRAYERS dict.
To add a new prayer: create a new module, import it here, add to PRAYERS.
"""

from .ave_maria       import AveMaria
from .ave_verum_corpus import AveVerumCorpus
from .lords_prayer    import LordsPrayer
from .serenity        import Serenity
from .psalm_23        import Psalm23
from .peace           import Peace
from .nunc_dimittis   import NuncDimittis
from .miserere        import Miserere
from .gloria_patri    import GloriaPatri
from .sanctus         import Sanctus
from .magnificat      import Magnificat
from .base            import Prayer

# ── Registry ───────────────────────────────────────────────────────────────────
PRAYERS: dict = {
    "ave":        AveMaria,
    "ave_verum":  AveVerumCorpus,
    "lords":      LordsPrayer,
    "serenity":   Serenity,
    "psalm23":    Psalm23,
    "peace":      Peace,
    "nunc":       NuncDimittis,
    "miserere":   Miserere,
    "gloria":     GloriaPatri,
    "sanctus":    Sanctus,
    "magnificat": Magnificat,
}

# Aliases for --prayer argument
PRAYER_ALIASES: dict = {
    # Ave Maria
    "ave":           "ave",
    "ave maria":     "ave",
    "avemaria":      "ave",
    "hail mary":     "ave",
    "hailmary":      "ave",
    # Ave Verum Corpus
    "ave_verum":         "ave_verum",
    "ave verum":         "ave_verum",
    "ave verum corpus":  "ave_verum",
    "averumcorpus":      "ave_verum",
    "hail true body":    "ave_verum",
    # Lord's Prayer
    "lords":         "lords",
    "lord":          "lords",
    "lords prayer":  "lords",
    "lordsprayer":   "lords",
    "our father":    "lords",
    "ourfather":     "lords",
    "paternoster":   "lords",
    "pater noster":  "lords",
    "vaterunser":    "lords",
    "padre nostro":  "lords",
    "notre pere":    "lords",
    "notre père":    "lords",
    # Serenity Prayer
    "serenity":          "serenity",
    "serenity prayer":   "serenity",
    "gelassenheit":      "serenity",
    # 23rd Psalm
    "psalm23":                     "psalm23",
    "psalm 23":                    "psalm23",
    "23rd psalm":                  "psalm23",
    "the lord is my shepherd":     "psalm23",
    "der herr ist mein hirte":     "psalm23",
    # Peace Prayer
    "peace":                 "peace",
    "peace prayer":          "peace",
    "prayer of st francis":  "peace",
    "st francis":            "peace",
    "make me a channel":     "peace",
    "channel of your peace": "peace",
    # Nunc Dimittis
    "nunc":              "nunc",
    "nunc dimittis":     "nunc",
    "song of simeon":    "nunc",
    "compline":          "nunc",
    # Miserere
    "miserere":          "miserere",
    "psalm51":           "miserere",
    "psalm 51":          "miserere",
    "have mercy":        "miserere",
    # Gloria Patri
    "gloria":            "gloria",
    "gloria patri":      "gloria",
    "glory be":          "gloria",
    "glory be to the father": "gloria",
    "doxology":          "gloria",
    "lesser doxology":   "gloria",
    "ehre sei dem vater": "gloria",
    # Sanctus
    "sanctus":           "sanctus",
    "holy holy holy":    "sanctus",
    "sanctus sanctus":   "sanctus",
    "trisagion":         "sanctus",
    "heilig heilig heilig": "sanctus",
    # Magnificat
    "magnificat":        "magnificat",
    "mary's song":       "magnificat",
    "song of mary":      "magnificat",
    "luke 1":            "magnificat",
    "my soul magnifies":  "magnificat",
    "meine seele erhebt": "magnificat",
}

__all__ = ["Prayer", "PRAYERS", "PRAYER_ALIASES"]
