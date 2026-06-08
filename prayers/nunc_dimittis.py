"""
prayers/nunc_dimittis.py — The Nunc Dimittis (Song of Simeon).

Text: Luke 2:29-32, King James Version (public domain).
Traditional Compline canticle — sung or said at the close of day.
"""

from .base import Prayer

def _voices(lang_tag: str) -> dict:
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

NuncDimittis = Prayer(
    name  = "nunc",
    title = "Nunc Dimittis",
    native_titles = {
        "english":    "Lord, now lettest thou thy servant depart in peace",
        "german":     "Herr, nun lässest du deinen Diener in Frieden fahren",
        "italian":    "Ora lascia, o Signore, che il tuo servo vada in pace",
        "latin":      "Nunc dimittis servum tuum, Domine",
        "french":     "Maintenant, Seigneur, tu laisses ton serviteur s'en aller en paix",
        "spanish":    "Ahora, Señor, despides a tu siervo en paz",
        "portuguese": "Agora, Senhor, despedes o teu servo em paz",
        "polish":     "Teraz, o Panie, pozwalasz odejść swojemu słudze w pokoju",
    },
    texts = {
        "english": (
            "Lord, now lettest thou thy servant depart in peace,\n"
            "according to thy word.\n"
            "For mine eyes have seen thy salvation,\n"
            "which thou hast prepared before the face of all people;\n"
            "a light to lighten the Gentiles,\n"
            "and the glory of thy people Israel.\n"
            "Glory be to the Father, and to the Son,\n"
            "and to the Holy Ghost;\n"
            "as it was in the beginning, is now, and ever shall be,\n"
            "world without end. Amen."
        ),
        "german": (
            "Herr, nun lässest du deinen Diener in Frieden fahren,\n"
            "wie du gesagt hast.\n"
            "Denn meine Augen haben deinen Heiland gesehen,\n"
            "welchen du bereitet hast vor allen Völkern,\n"
            "ein Licht zur Erleuchtung der Heiden\n"
            "und zum Preis deines Volkes Israel.\n"
            "Ehre sei dem Vater und dem Sohn\n"
            "und dem Heiligen Geist,\n"
            "wie es war im Anfang, jetzt und immerdar\n"
            "und in Ewigkeit. Amen."
        ),
        "italian": (
            "Ora lascia, o Signore, che il tuo servo vada in pace,\n"
            "secondo la tua parola.\n"
            "Perché i miei occhi hanno visto la tua salvezza,\n"
            "che hai preparata davanti a tutti i popoli:\n"
            "luce per illuminare le genti\n"
            "e gloria del tuo popolo Israele.\n"
            "Gloria al Padre, al Figlio\n"
            "e allo Spirito Santo,\n"
            "come era nel principio, ora e sempre\n"
            "nei secoli dei secoli. Amen."
        ),
        "latin": (
            "Nunc dimittis servum tuum, Domine,\n"
            "secundum verbum tuum in pace.\n"
            "Quia viderunt oculi mei salutare tuum,\n"
            "quod parasti ante faciem omnium populorum:\n"
            "lumen ad revelationem gentium\n"
            "et gloriam plebis tuae Israel.\n"
            "Gloria Patri et Filio\n"
            "et Spiritui Sancto,\n"
            "sicut erat in principio et nunc et semper\n"
            "et in saecula saeculorum. Amen."
        ),
        "french": (
            "Maintenant, Seigneur, tu laisses ton serviteur s'en aller en paix,\n"
            "selon ta parole.\n"
            "Car mes yeux ont vu ton salut,\n"
            "que tu as préparé devant tous les peuples:\n"
            "lumière pour éclairer les nations\n"
            "et gloire d'Israël ton peuple.\n"
            "Gloire au Père, au Fils\n"
            "et au Saint-Esprit,\n"
            "comme il était au commencement, maintenant et toujours\n"
            "dans les siècles des siècles. Amen."
        ),
        "spanish": (
            "Ahora, Señor, despides a tu siervo en paz,\n"
            "conforme a tu palabra.\n"
            "Porque han visto mis ojos tu salvación,\n"
            "la cual has preparado en presencia de todos los pueblos:\n"
            "luz para iluminar a las naciones\n"
            "y gloria de tu pueblo Israel.\n"
            "Gloria al Padre, al Hijo\n"
            "y al Espíritu Santo,\n"
            "como era en el principio, ahora y siempre\n"
            "por los siglos de los siglos. Amén."
        ),
        "portuguese": (
            "Agora, Senhor, despedes o teu servo em paz,\n"
            "segundo a tua palavra.\n"
            "Porque os meus olhos viram a tua salvação,\n"
            "a qual preparaste em presença de todos os povos:\n"
            "luz para iluminar as nações\n"
            "e glória do teu povo Israel.\n"
            "Glória ao Pai, ao Filho\n"
            "e ao Espírito Santo,\n"
            "como era no princípio, agora e sempre\n"
            "pelos séculos dos séculos. Amém."
        ),
        "polish": (
            "Teraz, o Panie, pozwalasz odejść swojemu słudze w pokoju,\n"
            "według Twojego słowa.\n"
            "Bo moje oczy ujrzały Twoje zbawienie,\n"
            "które przygotowałeś wobec wszystkich narodów:\n"
            "światło na oświecenie pogan\n"
            "i chwałę ludu Twego, Izraela.\n"
            "Chwała Ojcu i Synowi\n"
            "i Duchowi Świętemu,\n"
            "jak była na początku, teraz i zawsze\n"
            "i na wieki wieków. Amen."
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
