"""
prayers/crucified_thief.py — Hail, O Thief (original liturgical prayer by Steve Price,
for the Penitent/Crucified Thief of Luke's Gospel)
"""

from .base import Prayer, voices_for


# ── Prayer definition ──────────────────────────────────────────────────────────

CrucifiedThief = Prayer(
    name  = "crucified-thief",
    title = "Hail, O Thief",
    native_titles = {
        "english":    "Hail, O Thief",
        "german":     "Sei gegrüßt, o Schächer",
        "italian":    "Ave, o Ladrone",
        "latin":      "Salve, O Latro",
        "french":     "Salut, ô Larron",
        "spanish":    "Salve, oh Ladrón",
        "portuguese": "Salve, ó Ladrão",
        "polish":     "Witaj, Łotrze",
    },
    texts = {
        "english": (
            "Hail, O Thief, redeemed upon the Cross,\n"
            "Who by the side of Christ didst hear the word of grace:\n"
            "\u201cThis day thou shalt be with me in paradise.\u201d\n"
            "Criminal made saint in a single mercy,\n"
            "Pray for us sinners, now and at the hour of our death."
        ),
        "german": (
            "Sei gegrüßt, o Schächer, erlöst am Kreuz,\n"
            "der du an der Seite Christi das Wort der Gnade hörtest:\n"
            "\u201eHeute wirst du mit mir im Paradiese sein.\u201c\n"
            "Verbrecher, in einer einzigen Barmherzigkeit zum Heiligen gemacht,\n"
            "bitte für uns Sünder, jetzt und in der Stunde unseres Todes."
        ),
        "italian": (
            "Ave, o Ladrone, redento sulla Croce,\n"
            "che al fianco di Cristo udisti la parola di grazia:\n"
            "\u201cOggi sarai con me nel paradiso.\u201d\n"
            "Criminale fatto santo in un'unica misericordia,\n"
            "prega per noi peccatori, adesso e nell'ora della nostra morte."
        ),
        "latin": (
            "Salve, O Latro, in Cruce redemptus,\n"
            "qui iuxta Christum verbum gratiae audisti:\n"
            "\u201cHodie mecum eris in paradiso.\u201d\n"
            "Facinorosus sanctus una misericordia factus,\n"
            "ora pro nobis peccatoribus, nunc et in hora mortis nostrae."
        ),
        "french": (
            "Salut, ô Larron, racheté sur la Croix,\n"
            "toi qui, aux côtés du Christ, entendis la parole de grâce :\n"
            "\u00ab Aujourd'hui tu seras avec moi dans le paradis. \u00bb\n"
            "Criminel devenu saint en une seule miséricorde,\n"
            "prie pour nous, pauvres pécheurs, maintenant et à l'heure de notre mort."
        ),
        "spanish": (
            "Salve, oh Ladrón, redimido en la Cruz,\n"
            "tú que, al lado de Cristo, oíste la palabra de gracia:\n"
            "\u201cHoy estarás conmigo en el paraíso.\u201d\n"
            "Criminal hecho santo en una sola misericordia,\n"
            "ruega por nosotros, pecadores, ahora y en la hora de nuestra muerte."
        ),
        "portuguese": (
            "Salve, ó Ladrão, remido na Cruz,\n"
            "tu que, ao lado de Cristo, ouviste a palavra da graça:\n"
            "\u201cHoje estarás comigo no paraíso.\u201d\n"
            "Criminoso feito santo numa só misericórdia,\n"
            "rogai por nós, pecadores, agora e na hora da nossa morte."
        ),
        "polish": (
            "Witaj, Łotrze, odkupiony na Krzyżu,\n"
            "który u boku Chrystusa usłyszałeś słowo łaski:\n"
            "\u201eDziś będziesz ze Mną w raju.\u201d\n"
            "Zbrodniarz uczyniony świętym przez jedno miłosierdzie,\n"
            "módl się za nami grzesznymi, teraz i w godzinę śmierci naszej."
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
    image = "crucified-thief.png",
)
