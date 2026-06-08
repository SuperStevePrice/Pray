"""
prayers/peace.py — The Peace Prayer (attributed to St. Francis of Assisi).

Note: The prayer text dates to 1912 (La Clochette, France), not to Francis
himself. It became widely known through Sebastian Temple's 1967 musical
setting "Make Me a Channel of Your Peace." The text is freely usable.
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

Peace = Prayer(
    name  = "peace",
    title = "The Peace Prayer",
    native_titles = {
        "english":    "Make Me a Channel of Your Peace",
        "german":     "Herr, mach mich zu einem Werkzeug deines Friedens",
        "italian":    "Signore, fa' di me uno strumento della tua pace",
        "latin":      "Domine, fac me instrumentum pacis tuae",
        "french":     "Seigneur, fais de moi un instrument de ta paix",
        "spanish":    "Señor, hazme un instrumento de tu paz",
        "portuguese": "Senhor, fazei-me instrumento da vossa paz",
        "polish":     "Panie, uczyń mnie narzędziem Twojego pokoju",
    },
    texts = {
        "english": (
            "Lord, make me an instrument of your peace.\n"
            "Where there is hatred, let me sow love;\n"
            "where there is injury, pardon;\n"
            "where there is doubt, faith;\n"
            "where there is despair, hope;\n"
            "where there is darkness, light;\n"
            "where there is sadness, joy.\n"
            "O Divine Master, grant that I may not so much seek\n"
            "to be consoled as to console,\n"
            "to be understood as to understand,\n"
            "to be loved as to love.\n"
            "For it is in giving that we receive,\n"
            "it is in pardoning that we are pardoned,\n"
            "and it is in dying that we are born to eternal life.\n"
            "Amen."
        ),
        "german": (
            "Herr, mach mich zu einem Werkzeug deines Friedens,\n"
            "dass ich Liebe übe, wo man sich hasst,\n"
            "dass ich verzeihe, wo man sich beleidigt,\n"
            "dass ich verbinde, wo Streit ist,\n"
            "dass ich die Wahrheit sage, wo Irrtum ist,\n"
            "dass ich den Glauben bringe, wo Zweifel droht,\n"
            "dass ich Hoffnung wecke, wo Verzweiflung quält,\n"
            "dass ich Licht entzünde, wo Finsternis regiert,\n"
            "dass ich Freude bringe, wo der Kummer wohnt.\n"
            "Herr, lass mich trachten,\n"
            "nicht, dass ich getröstet werde, sondern dass ich tröste,\n"
            "nicht, dass ich verstanden werde, sondern dass ich verstehe,\n"
            "nicht, dass ich geliebt werde, sondern dass ich liebe.\n"
            "Denn wer sich hingibt, der empfängt,\n"
            "wer sich selbst vergisst, der findet,\n"
            "wer verzeiht, dem wird verziehen,\n"
            "und wer stirbt, der erwacht zum ewigen Leben.\n"
            "Amen."
        ),
        "italian": (
            "Signore, fa' di me uno strumento della tua pace:\n"
            "dove è odio, fa' ch'io porti amore;\n"
            "dove è offesa, ch'io porti il perdono;\n"
            "dove è discordia, ch'io porti l'unione;\n"
            "dove è dubbio, ch'io porti la fede;\n"
            "dove è errore, ch'io porti la verità;\n"
            "dove è disperazione, ch'io porti la speranza;\n"
            "dove è tristezza, ch'io porti la gioia;\n"
            "dove sono le tenebre, ch'io porti la luce.\n"
            "O Maestro Divino, fa' che io non cerchi tanto\n"
            "di essere consolato, quanto di consolare;\n"
            "di essere compreso, quanto di comprendere;\n"
            "di essere amato, quanto di amare.\n"
            "Poiché è dando che si riceve,\n"
            "è perdonando che si è perdonati,\n"
            "ed è morendo che si risuscita a vita eterna.\n"
            "Amen."
        ),
        "latin": (
            "Domine, fac me instrumentum pacis tuae:\n"
            "ubi odium, amorem seram;\n"
            "ubi iniuria, veniam;\n"
            "ubi discordia, unionem;\n"
            "ubi dubium, fidem;\n"
            "ubi error, veritatem;\n"
            "ubi desperatio, spem;\n"
            "ubi tristitia, laetitiam;\n"
            "ubi tenebrae, lucem.\n"
            "O Magister Divine, concede ut non tam\n"
            "consolationem quaeram quam consolare;\n"
            "intelligi quam intelligere;\n"
            "amari quam amare.\n"
            "Nam in dando accipitur,\n"
            "in ignoscendo ignoscitur,\n"
            "et in moriendo ad vitam aeternam resurgetur.\n"
            "Amen."
        ),
        "french": (
            "Seigneur, fais de moi un instrument de ta paix.\n"
            "Là où il y a de la haine, que je mette l'amour;\n"
            "là où il y a une offense, que je mette le pardon;\n"
            "là où il y a la discorde, que je mette l'union;\n"
            "là où il y a l'erreur, que je mette la vérité;\n"
            "là où il y a le doute, que je mette la foi;\n"
            "là où il y a le désespoir, que je mette l'espérance;\n"
            "là où il y a les ténèbres, que je mette ta lumière;\n"
            "là où il y a la tristesse, que je mette la joie.\n"
            "Ô Maître, que je ne cherche pas tant\n"
            "à être consolé qu'à consoler,\n"
            "à être compris qu'à comprendre,\n"
            "à être aimé qu'à aimer.\n"
            "Car c'est en donnant qu'on reçoit,\n"
            "c'est en s'oubliant qu'on trouve,\n"
            "c'est en pardonnant qu'on est pardonné,\n"
            "c'est en mourant qu'on ressuscite à l'éternelle vie.\n"
            "Amen."
        ),
        "spanish": (
            "Señor, hazme un instrumento de tu paz:\n"
            "donde haya odio, que yo lleve el amor;\n"
            "donde haya ofensa, que yo lleve el perdón;\n"
            "donde haya discordia, que yo lleve la unión;\n"
            "donde haya duda, que yo lleve la fe;\n"
            "donde haya error, que yo lleve la verdad;\n"
            "donde haya desesperación, que yo lleve la esperanza;\n"
            "donde haya tristeza, que yo lleve la alegría;\n"
            "donde haya tinieblas, que yo lleve la luz.\n"
            "Oh, Maestro Divino, concédeme que no busque tanto\n"
            "ser consolado como consolar,\n"
            "ser comprendido como comprender,\n"
            "ser amado como amar.\n"
            "Porque es dando como se recibe,\n"
            "es perdonando como se es perdonado,\n"
            "y es muriendo como se resucita a la vida eterna.\n"
            "Amén."
        ),
        "portuguese": (
            "Senhor, fazei-me instrumento da vossa paz.\n"
            "Onde houver ódio, que eu leve o amor;\n"
            "onde houver ofensa, que eu leve o perdão;\n"
            "onde houver discórdia, que eu leve a união;\n"
            "onde houver dúvida, que eu leve a fé;\n"
            "onde houver erro, que eu leve a verdade;\n"
            "onde houver desespero, que eu leve a esperança;\n"
            "onde houver tristeza, que eu leve a alegria;\n"
            "onde houver trevas, que eu leve a luz.\n"
            "Ó Divino Mestre, concedei-me que eu não procure tanto\n"
            "ser consolado como consolar,\n"
            "ser compreendido como compreender,\n"
            "ser amado como amar.\n"
            "Pois é dando que se recebe,\n"
            "é perdoando que se é perdoado,\n"
            "e é morrendo que se ressuscita para a vida eterna.\n"
            "Amém."
        ),
        "polish": (
            "Panie, uczyń mnie narzędziem Twojego pokoju,\n"
            "abym siał miłość tam, gdzie panuje nienawiść;\n"
            "przebaczenie tam, gdzie panuje krzywda;\n"
            "jedność tam, gdzie panuje niezgoda;\n"
            "prawdę tam, gdzie panuje błąd;\n"
            "wiarę tam, gdzie panuje wątpliwość;\n"
            "nadzieję tam, gdzie panuje rozpacz;\n"
            "światło tam, gdzie panuje mrok;\n"
            "radość tam, gdzie panuje smutek.\n"
            "O Panie, spraw, abym nie szukał tak bardzo\n"
            "pociechy, jak pocieszania;\n"
            "zrozumienia, jak rozumienia;\n"
            "miłości, jak miłowania.\n"
            "Bo przez dawanie — otrzymujemy,\n"
            "przez przebaczanie — otrzymujemy przebaczenie,\n"
            "a przez umieranie — rodzimy się do życia wiecznego.\n"
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
