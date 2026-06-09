"""
prayers/ave_maria.py — Ave Maria (Hail Mary) prayer definition.
"""

from .base import Prayer, voices_for


# ── Prayer definition ──────────────────────────────────────────────────────────

AveMaria = Prayer(
    name  = "ave",
    title = "Ave Maria",
    native_titles = {
        "english":    "Hail Mary",
        "german":     "Gegrüßet seist du, Maria",
        "italian":    "Ave Maria",
        "latin":      "Ave Maria",
        "french":     "Je vous salue, Marie",
        "spanish":    "Dios te salve, María",
        "portuguese": "Ave Maria",
        "polish":     "Zdrowaś Maryjo",
    },
    texts = {
        "english": (
            "Hail Mary, full of grace, the Lord is with thee.\n"
            "Blessed art thou among women,\n"
            "and blessed is the fruit of thy womb, Jesus.\n"
            "Holy Mary, Mother of God, pray for us sinners,\n"
            "now and at the hour of our death. Amen."
        ),
        "german": (
            "Gegrüßet seist du, Maria, voll der Gnade, der Herr ist mit dir.\n"
            "Du bist gebenedeit unter den Frauen,\n"
            "und gebenedeit ist die Frucht deines Leibes, Jesus.\n"
            "Heilige Maria, Mutter Gottes, bitte für uns Sünder\n"
            "jetzt und in der Stunde unseres Todes. Amen."
        ),
        "italian": (
            "Ave Maria, piena di grazia, il Signore è con te.\n"
            "Tu sei benedetta fra le donne,\n"
            "e benedetto è il frutto del tuo seno, Gesù.\n"
            "Santa Maria, Madre di Dio, prega per noi peccatori,\n"
            "adesso e nell'ora della nostra morte. Amen."
        ),
        "latin": (
            "Ave Maria, gratia plena, Dominus tecum.\n"
            "Benedicta tu in mulieribus,\n"
            "et benedictus fructus ventris tui, Iesus.\n"
            "Sancta Maria, Mater Dei, ora pro nobis peccatoribus,\n"
            "nunc et in hora mortis nostrae. Amen."
        ),
        "french": (
            "Je vous salue, Marie, pleine de grâce,\n"
            "le Seigneur est avec vous.\n"
            "Vous êtes bénie entre toutes les femmes,\n"
            "et Jésus, le fruit de vos entrailles, est béni.\n"
            "Sainte Marie, Mère de Dieu,\n"
            "priez pour nous, pauvres pécheurs,\n"
            "maintenant et à l'heure de notre mort. Amen."
        ),
        "spanish": (
            "Dios te salve, María, llena eres de gracia,\n"
            "el Señor es contigo.\n"
            "Bendita tú eres entre todas las mujeres,\n"
            "y bendito es el fruto de tu vientre, Jesús.\n"
            "Santa María, Madre de Dios,\n"
            "ruega por nosotros, pecadores,\n"
            "ahora y en la hora de nuestra muerte. Amén."
        ),
        "portuguese": (
            "Ave Maria, cheia de graça,\n"
            "o Senhor é convosco.\n"
            "Bendita sois vós entre as mulheres,\n"
            "e bendito é o fruto do vosso ventre, Jesus.\n"
            "Santa Maria, Mãe de Deus,\n"
            "rogai por nós, pecadores,\n"
            "agora e na hora da nossa morte. Amém."
        ),
        "polish": (
            "Zdrowaś Maryjo, łaski pełna,\n"
            "Pan z Tobą.\n"
            "Błogosławionaś Ty między niewiastami\n"
            "i błogosławiony owoc żywota Twojego, Jezus.\n"
            "Święta Maryjo, Matko Boża,\n"
            "módl się za nami grzesznymi\n"
            "teraz i w godzinę śmierci naszej. Amen."
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
