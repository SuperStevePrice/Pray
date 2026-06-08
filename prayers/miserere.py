"""
prayers/miserere.py — Psalm 51 (Miserere mei, Deus).

Text: King James Version (public domain).
The classic psalm of repentance, attributed to David after Nathan's rebuke.
Used in Compline, Ash Wednesday, and penitential services across traditions.
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

Miserere = Prayer(
    name  = "miserere",
    title = "Psalm 51 — Miserere",
    native_titles = {
        "english":    "Have mercy on me, O God",
        "german":     "Gott, sei mir gnädig",
        "italian":    "Pietà di me, o Dio",
        "latin":      "Miserere mei, Deus",
        "french":     "Aie pitié de moi, ô Dieu",
        "spanish":    "Ten misericordia de mí, oh Dios",
        "portuguese": "Tem misericórdia de mim, ó Deus",
        "polish":     "Zmiłuj się nade mną, Boże",
    },
    texts = {
        "english": (
            "Have mercy upon me, O God,\n"
            "according to thy lovingkindness:\n"
            "according unto the multitude of thy tender mercies\n"
            "blot out my transgressions.\n"
            "Wash me thoroughly from mine iniquity,\n"
            "and cleanse me from my sin.\n"
            "For I acknowledge my transgressions:\n"
            "and my sin is ever before me.\n"
            "Create in me a clean heart, O God;\n"
            "and renew a right spirit within me.\n"
            "Cast me not away from thy presence;\n"
            "and take not thy holy spirit from me.\n"
            "Restore unto me the joy of thy salvation;\n"
            "and uphold me with thy free spirit.\n"
            "The sacrifices of God are a broken spirit:\n"
            "a broken and a contrite heart, O God,\n"
            "thou wilt not despise.\n"
            "Amen."
        ),
        "german": (
            "Gott, sei mir gnädig nach deiner Güte,\n"
            "und tilge meine Sünden nach deiner großen Barmherzigkeit.\n"
            "Wasche mich rein von meiner Missetat\n"
            "und reinige mich von meiner Sünde.\n"
            "Denn ich erkenne meine Missetat,\n"
            "und meine Sünde ist immer vor mir.\n"
            "Schaffe in mir, Gott, ein reines Herz\n"
            "und gib mir einen neuen, beständigen Geist.\n"
            "Verwirf mich nicht von deinem Angesicht\n"
            "und nimm deinen heiligen Geist nicht von mir.\n"
            "Erfreue mich wieder mit deiner Hilfe,\n"
            "und mit einem willigen Geist rüste mich aus.\n"
            "Das Opfer, das Gott gefällt, ist ein geängsteter Geist;\n"
            "ein geängstetes, zerschlagenes Herz\n"
            "wirst du, Gott, nicht verachten.\n"
            "Amen."
        ),
        "italian": (
            "Pietà di me, o Dio, nel tuo amore,\n"
            "nella tua grande misericordia cancella il mio peccato.\n"
            "Lavami da tutte le mie colpe,\n"
            "mondami dal mio peccato.\n"
            "Riconosco la mia colpa,\n"
            "il mio peccato mi sta sempre dinanzi.\n"
            "Crea in me, o Dio, un cuore puro,\n"
            "rinnova in me uno spirito saldo.\n"
            "Non scacciarmi dalla tua presenza\n"
            "e non togliermi il tuo santo spirito.\n"
            "Rendimi la gioia della tua salvezza,\n"
            "sostienimi con uno spirito generoso.\n"
            "Uno spirito contrito è sacrificio a Dio;\n"
            "un cuore contrito e affranto\n"
            "tu, o Dio, non disprezzi.\n"
            "Amen."
        ),
        "latin": (
            "Miserere mei, Deus,\n"
            "secundum magnam misericordiam tuam;\n"
            "et secundum multitudinem miserationum tuarum\n"
            "dele iniquitatem meam.\n"
            "Amplius lava me ab iniquitate mea,\n"
            "et a peccato meo munda me.\n"
            "Quoniam iniquitatem meam ego cognosco,\n"
            "et peccatum meum contra me est semper.\n"
            "Cor mundum crea in me, Deus,\n"
            "et spiritum rectum innova in visceribus meis.\n"
            "Ne proicias me a facie tua,\n"
            "et spiritum sanctum tuum ne auferas a me.\n"
            "Redde mihi laetitiam salutaris tui,\n"
            "et spiritu principali confirma me.\n"
            "Sacrificium Deo spiritus contribulatus;\n"
            "cor contritum et humiliatum, Deus, non despicies.\n"
            "Amen."
        ),
        "french": (
            "Aie pitié de moi, ô Dieu, dans ta bonté;\n"
            "selon ta grande miséricorde, efface mes transgressions.\n"
            "Lave-moi complètement de mon iniquité,\n"
            "et purifie-moi de mon péché.\n"
            "Car je reconnais mes transgressions,\n"
            "et mon péché est constamment devant moi.\n"
            "Crée en moi un cœur pur, ô Dieu,\n"
            "et renouvelle en moi un esprit bien disposé.\n"
            "Ne me rejette pas loin de ta face,\n"
            "et ne me retire pas ton Esprit Saint.\n"
            "Rends-moi la joie de ton salut,\n"
            "et qu'un esprit généreux me soutienne.\n"
            "Les sacrifices qui plaisent à Dieu, c'est un esprit brisé;\n"
            "un cœur brisé et contrit,\n"
            "tu ne le mépriseras pas, ô Dieu.\n"
            "Amen."
        ),
        "spanish": (
            "Ten misericordia de mí, oh Dios, conforme a tu bondad;\n"
            "conforme a la multitud de tus piedades borra mis rebeliones.\n"
            "Lávame más y más de mi maldad,\n"
            "y límpiame de mi pecado.\n"
            "Porque yo reconozco mis rebeliones,\n"
            "y mi pecado está siempre delante de mí.\n"
            "Crea en mí, oh Dios, un corazón limpio,\n"
            "y renueva un espíritu recto dentro de mí.\n"
            "No me eches de delante de ti,\n"
            "y no quites de mí tu Santo Espíritu.\n"
            "Vuélveme el gozo de tu salvación,\n"
            "y espíritu noble me sustente.\n"
            "Los sacrificios de Dios son el espíritu quebrantado;\n"
            "al corazón contrito y humillado\n"
            "no despreciarás tú, oh Dios.\n"
            "Amén."
        ),
        "portuguese": (
            "Tem misericórdia de mim, ó Deus, segundo a tua benignidade;\n"
            "apaga as minhas transgressões segundo a multidão das tuas misericórdias.\n"
            "Lava-me completamente da minha iniquidade\n"
            "e purifica-me do meu pecado.\n"
            "Porque eu conheço as minhas transgressões,\n"
            "e o meu pecado está sempre diante de mim.\n"
            "Cria em mim, ó Deus, um coração puro,\n"
            "e renova em mim um espírito reto.\n"
            "Não me lances fora da tua presença\n"
            "e não retires de mim o teu Espírito Santo.\n"
            "Restitui-me a alegria da tua salvação\n"
            "e sustenta-me com um espírito voluntário.\n"
            "Os sacrifícios de Deus são o espírito quebrantado;\n"
            "a um coração quebrantado e contrito\n"
            "não desprezarás, ó Deus.\n"
            "Amém."
        ),
        "polish": (
            "Zmiłuj się nade mną, Boże, w swojej łaskawości,\n"
            "w ogromie swego miłosierdzia wymaż moją nieprawość.\n"
            "Obmyj mnie zupełnie z mojej winy\n"
            "i oczyść mnie z grzechu.\n"
            "Uznaję bowiem moją nieprawość,\n"
            "mój grzech jest zawsze przede mną.\n"
            "Stwórz we mnie, Boże, serce czyste\n"
            "i odnów we mnie moc ducha.\n"
            "Nie odrzucaj mnie od swojego oblicza\n"
            "i nie odbieraj mi swego Ducha Świętego.\n"
            "Przywróć mi radość Twojego zbawienia\n"
            "i wzmocnij mnie duchem ofiarnym.\n"
            "Ofiarą Bogu miłą jest duch skruszony;\n"
            "sercem skruszonym i pokornym\n"
            "Ty, Boże, nie gardzisz.\n"
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
