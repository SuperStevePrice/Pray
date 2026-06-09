"""
prayers/serenity.py — The Serenity Prayer definition.

Short form attributed to Reinhold Niebuhr, c. 1932-1943.
"""

from .base import Prayer, voices_for


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
        "english":    voices_for("english"),
        "german":    voices_for("german"),
        "italian":    voices_for("italian"),
        "latin":    voices_for("latin"),
        "french":    voices_for("french"),
        "spanish":    voices_for("spanish"),
        "portuguese":    voices_for("portuguese"),
        "polish": voices_for("polish"),
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
