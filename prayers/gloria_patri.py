"""
prayers/gloria_patri.py — Gloria Patri (Lesser Doxology).

One of the oldest Christian doxologies, used at the close of psalms
and canticles across Catholic, Orthodox, Anglican, and Lutheran traditions.
Text: public domain.
"""

from .base import Prayer, voices_for


GloriaPatri = Prayer(
    name  = "gloria",
    title = "Gloria Patri",
    native_titles = {
        "english":    "Glory be to the Father",
        "german":     "Ehre sei dem Vater",
        "italian":    "Gloria al Padre",
        "latin":      "Gloria Patri",
        "french":     "Gloire au Père",
        "spanish":    "Gloria al Padre",
        "portuguese": "Glória ao Pai",
        "polish":     "Chwała Ojcu",
    },
    texts = {
        "english": (
            "Glory be to the Father,\n"
            "and to the Son,\n"
            "and to the Holy Ghost;\n"
            "as it was in the beginning,\n"
            "is now, and ever shall be,\n"
            "world without end.\n"
            "Amen."
        ),
        "german": (
            "Ehre sei dem Vater\n"
            "und dem Sohn\n"
            "und dem Heiligen Geist,\n"
            "wie es war im Anfang,\n"
            "jetzt und immerdar\n"
            "und in Ewigkeit.\n"
            "Amen."
        ),
        "italian": (
            "Gloria al Padre\n"
            "e al Figlio\n"
            "e allo Spirito Santo,\n"
            "come era nel principio,\n"
            "ora e sempre\n"
            "nei secoli dei secoli.\n"
            "Amen."
        ),
        "latin": (
            "Gloria Patri\n"
            "et Filio\n"
            "et Spiritui Sancto,\n"
            "sicut erat in principio\n"
            "et nunc et semper\n"
            "et in saecula saeculorum.\n"
            "Amen."
        ),
        "french": (
            "Gloire au Père,\n"
            "au Fils\n"
            "et au Saint-Esprit,\n"
            "comme il était au commencement,\n"
            "maintenant et toujours\n"
            "dans les siècles des siècles.\n"
            "Amen."
        ),
        "spanish": (
            "Gloria al Padre,\n"
            "al Hijo\n"
            "y al Espíritu Santo,\n"
            "como era en el principio,\n"
            "ahora y siempre\n"
            "por los siglos de los siglos.\n"
            "Amén."
        ),
        "portuguese": (
            "Glória ao Pai,\n"
            "ao Filho\n"
            "e ao Espírito Santo,\n"
            "como era no princípio,\n"
            "agora e sempre\n"
            "pelos séculos dos séculos.\n"
            "Amém."
        ),
        "polish": (
            "Chwała Ojcu\n"
            "i Synowi,\n"
            "i Duchowi Świętemu,\n"
            "jak była na początku,\n"
            "teraz i zawsze\n"
            "i na wieki wieków.\n"
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
