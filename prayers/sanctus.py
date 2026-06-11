"""
prayers/sanctus.py — Sanctus (Holy, Holy, Holy) prayer definition.
"""

from .base import Prayer, voices_for


# ── Prayer definition ──────────────────────────────────────────────────────────

Sanctus = Prayer(
    name  = "sanctus",
    title = "Sanctus",
    native_titles = {
        "english":    "Holy, Holy, Holy",
        "german":     "Heilig, heilig, heilig",
        "italian":    "Santo, Santo, Santo",
        "latin":      "Sanctus, Sanctus, Sanctus",
        "french":     "Saint, Saint, Saint",
        "spanish":    "Santo, Santo, Santo",
        "portuguese": "Santo, Santo, Santo",
        "polish":     "Święty, Święty, Święty",
    },
    texts = {
        "english": (
            "Holy, holy, holy, Lord God of hosts.\n"
            "Heaven and earth are full of thy glory.\n"
            "Glory be to thee, O Lord Most High.\n"
            "Blessed is he that cometh in the name of the Lord.\n"
            "Hosanna in the highest."
        ),
        "german": (
            "Heilig, heilig, heilig ist der Herr, Gott der Heerscharen.\n"
            "Himmel und Erde sind erfüllt von deiner Herrlichkeit.\n"
            "Gelobt seist du, Herr in der Höhe.\n"
            "Gesegnet ist, der da kommt im Namen des Herrn.\n"
            "Hosanna in der Höhe."
        ),
        "italian": (
            "Santo, Santo, Santo il Signore Dio dell'universo.\n"
            "I cieli e la terra sono pieni della tua gloria.\n"
            "Osanna nell'alto dei cieli.\n"
            "Benedetto colui che viene nel nome del Signore.\n"
            "Osanna nell'alto dei cieli."
        ),
        "latin": (
            "Sanctus, Sanctus, Sanctus Dominus Deus Sabaoth.\n"
            "Pleni sunt caeli et terra gloria tua.\n"
            "Hosanna in excelsis.\n"
            "Benedictus qui venit in nomine Domini.\n"
            "Hosanna in excelsis."
        ),
        "french": (
            "Saint, Saint, Saint est le Seigneur, Dieu de l'univers.\n"
            "Le ciel et la terre sont remplis de ta gloire.\n"
            "Hosanna au plus haut des cieux.\n"
            "Béni soit celui qui vient au nom du Seigneur.\n"
            "Hosanna au plus haut des cieux."
        ),
        "spanish": (
            "Santo, Santo, Santo es el Señor, Dios del universo.\n"
            "Llenos están el cielo y la tierra de tu gloria.\n"
            "Hosanna en el cielo.\n"
            "Bendito el que viene en nombre del Señor.\n"
            "Hosanna en el cielo."
        ),
        "portuguese": (
            "Santo, Santo, Santo é o Senhor, Deus do universo.\n"
            "Cheios estão o céu e a terra da tua glória.\n"
            "Hosana nas alturas.\n"
            "Bendito o que vem em nome do Senhor.\n"
            "Hosana nas alturas."
        ),
        "polish": (
            "Święty, Święty, Święty jest Pan, Bóg mocy.\n"
            "Pełne są niebiosa i ziemia Twojej chwały.\n"
            "Hosanna na wysokościach.\n"
            "Błogosławiony, który przychodzi w imię Pańskie.\n"
            "Hosanna na wysokościach."
        ),
    },
    voices = {
        "english":    voices_for("english"),
        "german":     voices_for("german"),
        "italian":    voices_for("italian"),
        "latin":      voices_for("latin"),
        "french":     voices_for("french"),
        "spanish":    voices_for("spanish"),
        "portuguese": voices_for("portuguese"),
        "polish":     voices_for("polish"),
    },
    language_aliases = {
        # English
        "english":       "english",
        "englisch":      "english",
        "inglese":       "english",
        # German
        "german":        "german",
        "deutsch":       "german",
        "tedesco":       "german",
        # Italian
        "italian":       "italian",
        "italiano":      "italian",
        # Latin
        "latin":         "latin",
        "latina":        "latin",
        "lateinisch":    "latin",
        "latino":        "latin",
        "lingua latina": "latin",
        # French
        "french":        "french",
        "français":      "french",
        "francais":      "french",
        "französisch":   "french",
        "francese":      "french",
        # Spanish
        "spanish":       "spanish",
        "español":       "spanish",
        "espanol":       "spanish",
        "spanisch":      "spanish",
        "spagnolo":      "spanish",
        # Portuguese
        "portuguese":    "portuguese",
        "português":     "portuguese",
        "portugues":     "portuguese",
        "portugiesisch": "portuguese",
        "portoghese":    "portuguese",
        # Polish
        "polish":        "polish",
        "polski":        "polish",
        "polnisch":      "polish",
        "polacco":       "polish",
    },
    latin_note=(
        "  ℹ️   Latin requested: no dedicated Latin voice is available on macOS.\n"
        "      Using Italian voices, which render Church Latin most faithfully.\n"
    ),
)
