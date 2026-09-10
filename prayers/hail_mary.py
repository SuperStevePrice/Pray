"""
prayers/hail_mary.py — Hail Mary (original Marian prayer by Steve Price)
"""

from .base import Prayer, voices_for


# ── Prayer definition ──────────────────────────────────────────────────────────

HailMary = Prayer(
    name  = "hail-mary",
    title = "Hail Mary",
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
            "Hail Mary, full of grace\n"
            "I can not wait to see your face\n"
            "And dwell in that immortal place\n"
            "Your son has made for every race\n"
            "Where we shall live without a trace\n"
            "Of sorrow, tears, or sighing."
        ),
        "german": (
            "Gegrüßet seist du, Maria, voll der Gnade\n"
            "Ich kann nicht warten, dein Antlitz zu sehen\n"
            "Und in jenem unsterblichen Ort zu wohnen\n"
            "Den dein Sohn für jedes Volk bereitet hat\n"
            "Wo wir leben werden ohne eine Spur\n"
            "Von Trauer, Tränen oder Seufzern."
        ),
        "italian": (
            "Ave Maria, piena di grazia\n"
            "Non posso aspettare di vedere il tuo volto\n"
            "E abitare in quel luogo immortale\n"
            "Che tuo figlio ha fatto per ogni popolo\n"
            "Dove vivremo senza traccia\n"
            "Di dolore, lacrime o sospiri."
        ),
        "latin": (
            "Ave Maria, gratia plena\n"
            "Vultum tuum videre non possum praestolari\n"
            "Et in loco illo immortali habitare\n"
            "Quem filius tuus omni genti praeparavit\n"
            "Ubi vivemus sine ulla vestigio\n"
            "Doloris, lacrimarum, vel suspirii."
        ),
        "french": (
            "Je vous salue, Marie, pleine de grâce\n"
            "Je ne peux attendre de voir votre visage\n"
            "Et demeurer en ce lieu immortel\n"
            "Que votre fils a préparé pour chaque peuple\n"
            "Où nous vivrons sans trace\n"
            "De chagrin, de larmes ou de soupirs."
        ),
        "spanish": (
            "Dios te salve, María, llena eres de gracia\n"
            "No puedo esperar a ver tu rostro\n"
            "Y habitar en ese lugar inmortal\n"
            "Que tu Hijo ha hecho para cada pueblo\n"
            "Donde viviremos sin rastro\n"
            "De dolor, lágrimas o suspiros."
        ),
        "portuguese": (
            "Ave Maria, cheia de graça\n"
            "Não posso esperar para ver o vosso rosto\n"
            "E habitar naquele lugar imortal\n"
            "Que vosso Filho fez para cada povo\n"
            "Onde viveremos sem rastro\n"
            "De tristeza, lágrimas ou suspiros."
        ),
        "polish": (
            "Zdrowaś Maryjo, łaski pełna\n"
            "Nie mogę czekać, aby zobaczyć Twoją twarz\n"
            "I mieszkać w tym nieśmiertelnym miejscu\n"
            "Które Twój Syn przygotował dla każdego narodu\n"
            "Gdzie będziemy żyć bez śladu\n"
            "Smutku, łez ani westchnień."
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
    image = "hail-mary.png",
)
