"""
prayers/lords_prayer.py — The Lord's Prayer (Paternoster) definition.
"""

from .base import Prayer

def _voices(lang_tag: str) -> dict[str, str]:
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

LordsPrayer = Prayer(
    name  = "lords",
    title = "The Lord's Prayer",
    native_titles = {
        "english":    "The Lord's Prayer",
        "german":     "Vaterunser",
        "italian":    "Padre Nostro",
        "latin":      "Pater Noster",
        "french":     "Notre Père",
        "spanish":    "Padre Nuestro",
        "portuguese": "Pai Nosso",
        "polish":     "Ojcze nasz",
    },
    texts = {
        "english": (
            "Our Father, who art in heaven,\n"
            "hallowed be thy name.\n"
            "Thy kingdom come, thy will be done,\n"
            "on earth as it is in heaven.\n"
            "Give us this day our daily bread,\n"
            "and forgive us our trespasses,\n"
            "as we forgive those who trespass against us.\n"
            "And lead us not into temptation,\n"
            "but deliver us from evil.\n"
            "For thine is the kingdom, the power, and the glory,\n"
            "for ever and ever. Amen."
        ),
        "german": (
            "Vater unser im Himmel,\n"
            "geheiligt werde dein Name.\n"
            "Dein Reich komme, dein Wille geschehe,\n"
            "wie im Himmel, so auf Erden.\n"
            "Unser tägliches Brot gib uns heute.\n"
            "Und vergib uns unsere Schuld,\n"
            "wie auch wir vergeben unsern Schuldigern.\n"
            "Und führe uns nicht in Versuchung,\n"
            "sondern erlöse uns von dem Bösen.\n"
            "Denn dein ist das Reich und die Kraft\n"
            "und die Herrlichkeit in Ewigkeit. Amen."
        ),
        "italian": (
            "Padre nostro, che sei nei cieli,\n"
            "sia santificato il tuo nome.\n"
            "Venga il tuo regno, sia fatta la tua volontà,\n"
            "come in cielo così in terra.\n"
            "Dacci oggi il nostro pane quotidiano,\n"
            "e rimetti a noi i nostri debiti,\n"
            "come noi li rimettiamo ai nostri debitori.\n"
            "E non ci indurre in tentazione,\n"
            "ma liberaci dal male.\n"
            "Amen."
        ),
        "latin": (
            "Pater noster, qui es in caelis,\n"
            "sanctificetur nomen tuum.\n"
            "Adveniat regnum tuum,\n"
            "fiat voluntas tua,\n"
            "sicut in caelo, et in terra.\n"
            "Panem nostrum quotidianum da nobis hodie,\n"
            "et dimitte nobis debita nostra,\n"
            "sicut et nos dimittimus debitoribus nostris.\n"
            "Et ne nos inducas in tentationem,\n"
            "sed libera nos a malo.\n"
            "Amen."
        ),
        "french": (
            "Notre Père, qui es aux cieux,\n"
            "que ton nom soit sanctifié.\n"
            "Que ton règne vienne,\n"
            "que ta volonté soit faite\n"
            "sur la terre comme au ciel.\n"
            "Donne-nous aujourd'hui notre pain de ce jour.\n"
            "Pardonne-nous nos offenses,\n"
            "comme nous pardonnons aussi à ceux qui nous ont offensés.\n"
            "Et ne nous soumets pas à la tentation,\n"
            "mais délivre-nous du mal.\n"
            "Car c'est à toi qu'appartiennent le règne,\n"
            "la puissance et la gloire, aux siècles des siècles. Amen."
        ),
        "spanish": (
            "Padre nuestro, que estás en el cielo,\n"
            "santificado sea tu nombre.\n"
            "Venga tu reino,\n"
            "hágase tu voluntad\n"
            "en la tierra como en el cielo.\n"
            "Danos hoy nuestro pan de cada día.\n"
            "Perdona nuestras ofensas,\n"
            "como también nosotros perdonamos\n"
            "a los que nos ofenden.\n"
            "No nos dejes caer en tentación\n"
            "y líbranos del mal. Amén."
        ),
        "portuguese": (
            "Pai nosso, que estais nos céus,\n"
            "santificado seja o vosso nome.\n"
            "Venha a nós o vosso reino.\n"
            "Seja feita a vossa vontade,\n"
            "assim na terra como no céu.\n"
            "O pão nosso de cada dia nos dai hoje.\n"
            "Perdoai-nos as nossas ofensas,\n"
            "assim como nós perdoamos\n"
            "a quem nos tem ofendido.\n"
            "E não nos deixeis cair em tentação,\n"
            "mas livrai-nos do mal. Amém."
        ),
        "polish": (
            "Ojcze nasz, któryś jest w niebie,\n"
            "święć się imię Twoje.\n"
            "Przyjdź królestwo Twoje,\n"
            "bądź wola Twoja,\n"
            "jako w niebie tak i na ziemi.\n"
            "Chleba naszego powszedniego daj nam dzisiaj.\n"
            "I odpuść nam nasze winy,\n"
            "jako i my odpuszczamy naszym winowajcom.\n"
            "I nie wódź nas na pokuszenie,\n"
            "ale nas zbaw ode złego. Amen."
        ),
    },
    voices = {
        "english":    _voices("English (US)"),
        "german":     _voices("German (Germany)"),
        "italian":    _voices("Italian (Italy)"),
        "latin":      _voices("Italian (Italy)"),
        "french":     _voices("French (France)"),
        "spanish":    _voices("Spanish (Spain)"),
        "portuguese": _voices("Portuguese (Brazil)"),
        "polish":     {
            "Zosia":   "Zosia",
            "Grandma": "Zosia",
            "Grandpa": "Zosia",
            "Eddy":    "Zosia",
            "Flo":     "Zosia",
            "Reed":    "Zosia",
            "Rocko":   "Zosia",
            "Sandy":   "Zosia",
            "Shelley": "Zosia",
        },
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
        "linqua latina": "latin",
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
