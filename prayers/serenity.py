"""
prayers/serenity.py — The Serenity Prayer definition.

Short form attributed to Reinhold Niebuhr, c. 1932-1943.
"""

from .base import Prayer

def _voices(lang_tag: str) -> dict[str, str]:
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

Serenity = Prayer(
    name  = "serenity",
    title = "The Serenity Prayer",
    native_titles = {
        "english":    "The Serenity Prayer",
        "german":     "Das Gelassenheitsgebet",
        "italian":    "La Preghiera della Serenità",
        "latin":      "Oratio Serenitatis",
        "french":     "La Prière de la Sérénité",
        "spanish":    "La Oración de la Serenidad",
        "portuguese": "A Oração da Serenidade",
        "polish":     "Modlitwa o Pogodę Ducha",
    },
    texts = {
        "english": (
            "God, grant me the serenity\n"
            "to accept the things I cannot change,\n"
            "courage to change the things I can,\n"
            "and wisdom to know the difference.\n"
            "Amen."
        ),
        "german": (
            "Gott, gib mir die Gelassenheit,\n"
            "Dinge hinzunehmen, die ich nicht ändern kann,\n"
            "den Mut, Dinge zu ändern, die ich ändern kann,\n"
            "und die Weisheit, das eine vom anderen zu unterscheiden.\n"
            "Amen."
        ),
        "italian": (
            "Dio, concedimi la serenità\n"
            "di accettare le cose che non posso cambiare,\n"
            "il coraggio di cambiare le cose che posso,\n"
            "e la saggezza di conoscere la differenza.\n"
            "Amen."
        ),
        "latin": (
            "Deus, da mihi serenitatem\n"
            "accipere ea quae mutare non possum,\n"
            "fortitudinem mutare ea quae possum,\n"
            "et sapientiam differentiam cognoscere.\n"
            "Amen."
        ),
        "french": (
            "Seigneur, accorde-moi la sérénité\n"
            "d'accepter les choses que je ne peux pas changer,\n"
            "le courage de changer les choses que je peux,\n"
            "et la sagesse d'en connaître la différence.\n"
            "Amen."
        ),
        "spanish": (
            "Dios, concédeme la serenidad\n"
            "para aceptar las cosas que no puedo cambiar,\n"
            "el valor para cambiar las que sí puedo,\n"
            "y la sabiduría para reconocer la diferencia.\n"
            "Amén."
        ),
        "portuguese": (
            "Deus, concede-me a serenidade\n"
            "para aceitar as coisas que não posso mudar,\n"
            "coragem para mudar as que posso,\n"
            "e sabedoria para distinguir uma das outras.\n"
            "Amém."
        ),
        "polish": (
            "Boże, użycz mi pogody ducha,\n"
            "abym godził się z tym, czego nie mogę zmienić,\n"
            "odwagi, abym zmieniał to, co mogę zmienić,\n"
            "i mądrości, abym odróżniał jedno od drugiego.\n"
            "Amen."
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
        "polish": {
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
        "english": "english", "englisch": "english", "inglese": "english",
        "german": "german", "deutsch": "german", "tedesco": "german",
        "italian": "italian", "italiano": "italian",
        "latin": "latin", "latina": "latin", "lateinisch": "latin",
        "latino": "latin", "lingua latina": "latin", "linqua latina": "latin",
        "french": "french", "français": "french", "francais": "french",
        "französisch": "french", "francese": "french",
        "spanish": "spanish", "español": "spanish", "espanol": "spanish",
        "spanisch": "spanish", "spagnolo": "spanish",
        "portuguese": "portuguese", "português": "portuguese",
        "portugues": "portuguese", "portugiesisch": "portuguese",
        "portoghese": "portuguese",
        "polish": "polish", "polski": "polish", "polnisch": "polish",
        "polacco": "polish",
    },
    latin_note=(
        "  ℹ️   Latin requested: no dedicated Latin voice is available on macOS.\n"
        "      Using Italian voices, which render Church Latin most faithfully.\n"
    ),
)
