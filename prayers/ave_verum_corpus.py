"""
prayers/ave_verum_corpus.py — Ave Verum Corpus prayer definition.
"""
from .base import Prayer, voices_for

# ── Prayer definition ──────────────────────────────────────────────────────────
AveVerumCorpus = Prayer(
    name  = "ave_verum",
    title = "Ave Verum Corpus",
    native_titles = {
        "english":    "Hail, True Body",
        "german":     "Sei gegrüßt, wahrer Leib",
        "italian":    "Ave, o vero Corpo",
        "latin":      "Ave Verum Corpus",
        "french":     "Salut, vrai Corps",
        "spanish":    "Salve, verdadero Cuerpo",
        "portuguese": "Ave, ó verdadeiro Corpo",
        "polish":     "Witaj, prawdziwe Ciało",
    },
    texts = {
        "english": (
            "Hail, true Body, born of the Virgin Mary,\n"
            "who truly suffered, sacrificed on the cross for mankind,\n"
            "from whose pierced side flowed water and blood:\n"
            "be for us a foretaste in the trial of death.\n"
            "\n"
            "O sweet Jesus, O holy Jesus, O Jesus, son of Mary.\n"
            "Have mercy on me. Amen."
        ),
        "german": (
            "Sei gegrüßt, wahrer Leib, geboren von der Jungfrau Maria,\n"
            "der du wahrhaft gelitten hast, geopfert am Kreuz für den Menschen,\n"
            "dessen durchbohrte Seite von Wasser und Blut floss:\n"
            "sei uns ein Vorgeschmack in der Prüfung des Todes.\n"
            "\n"
            "O süßer Jesus, o gütiger Jesus, o Jesus, Sohn der Maria.\n"
            "Erbarme dich meiner. Amen."
        ),
        "italian": (
            "Ave, o vero corpo, nato da Maria Vergine,\n"
            "che veramente patì e fu immolato sulla croce per l'uomo,\n"
            "dal cui fianco squarciato sgorgarono acqua e sangue:\n"
            "fa' che noi possiamo gustarti nella prova suprema della morte.\n"
            "\n"
            "O Gesù dolce, o Gesù pio, o Gesù figlio di Maria.\n"
            "Pietà di me. Amen."
        ),
        "latin": (
            "Ave verum corpus, natum de Maria Virgine,\n"
            "vere passum, immolatum in cruce pro homine,\n"
            "cuius latus perforatum fluxit aqua et sanguine:\n"
            "esto nobis praegustatum in mortis examine.\n"
            "\n"
            "O Iesu dulcis, O Iesu pie, O Iesu, fili Mariae.\n"
            "Miserere mei. Amen."
        ),
        "french": (
            "Salut, vrai Corps né de la Vierge Marie,\n"
            "ayant vraiment souffert et qui fut immolé sur la croix pour l'homme,\n"
            "toi dont le côté transpercé laissa couler l'eau et le sang:\n"
            "sois pour nous un réconfort dans l'heure de la mort.\n"
            "\n"
            "Ô doux, ô bon, ô Jésus fils de Marie.\n"
            "Aie pitié de moi. Ainsi soit-il."
        ),
        "spanish": (
            "Salve, verdadero Cuerpo, nacido de la Virgen María,\n"
            "verdaderamente atormentado, sacrificado en la cruz por la humanidad,\n"
            "de cuyo costado perforado fluyó agua y sangre:\n"
            "sé para nosotros un anticipo en el trance de la muerte.\n"
            "\n"
            "¡Oh, dulce Jesús! ¡Oh, piadoso Jesús! ¡Oh, Jesús, hijo de María!\n"
            "Ten piedad de mí. Amén."
        ),
        "portuguese": (
            "Salve, ó verdadeiro Corpo, nascido da Virgem Maria,\n"
            "que verdadeiramente padeceu e foi imolado na cruz pelo homem,\n"
            "do qual o lado transpassado jorrou água e sangue:\n"
            "sê para nós um antegosto na hora da morte.\n"
            "\n"
            "Ó doce Jesus, ó piedoso Jesus, ó Jesus, Filho de Maria.\n"
            "Tem piedade de mim. Amém."
        ),
        "polish": (
            "Witaj, prawdziwe Ciało, zrodzone z Maryi Dziewicy,\n"
            "prawdziwie umęczone i ofiarowane na krzyżu za człowieka,\n"
            "z Twego przebitego boku wypłynęła krew i woda:\n"
            "bądź nam przedsmakiem w godzinę śmierci.\n"
            "\n"
            "O Jezu słodki, o Jezu dobrotliwy, o Jezu, Synu Maryi.\n"
            "Zmiłuj się nade mną. Amen."
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
