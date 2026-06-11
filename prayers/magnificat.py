"""
prayers/magnificat.py — Magnificat (Song of Mary) prayer definition.
"""

from .base import Prayer, voices_for


# ── Prayer definition ──────────────────────────────────────────────────────────

Magnificat = Prayer(
    name  = "magnificat",
    title = "Magnificat",
    native_titles = {
        "english":    "Magnificat",
        "german":     "Magnificat",
        "italian":    "Magnificat",
        "latin":      "Magnificat",
        "french":     "Magnificat",
        "spanish":    "Magnificat",
        "portuguese": "Magnificat",
        "polish":     "Magnificat",
    },
    texts = {
        "english": (
            "My soul magnifies the Lord,\n"
            "and my spirit rejoices in God my Saviour.\n"
            "For he hath regarded the low estate of his handmaiden:\n"
            "for behold, from henceforth all generations shall call me blessed.\n"
            "For he that is mighty hath done to me great things;\n"
            "and holy is his name.\n"
            "And his mercy is on them that fear him\n"
            "from generation to generation.\n"
            "He hath showed strength with his arm;\n"
            "he hath scattered the proud in the imagination of their hearts.\n"
            "He hath put down the mighty from their seat,\n"
            "and exalted them of low degree.\n"
            "He hath filled the hungry with good things;\n"
            "and the rich he hath sent empty away.\n"
            "He hath holpen his servant Israel,\n"
            "in remembrance of his mercy.\n"
            "As he spake to our fathers,\n"
            "to Abraham, and to his seed for ever."
        ),
        "german": (
            "Meine Seele erhebt den Herrn,\n"
            "und mein Geist freut sich Gottes, meines Heilands.\n"
            "Denn er hat die Niedrigkeit seiner Magd angesehen.\n"
            "Siehe, von nun an werden mich selig preisen alle Kindeskinder.\n"
            "Denn der Mächtige hat Großes an mir getan,\n"
            "und sein Name ist heilig.\n"
            "Und seine Barmherzigkeit währet für und für\n"
            "bei denen, die ihn fürchten.\n"
            "Er übet Gewalt mit seinem Arm\n"
            "und zerstreuet, die hoffärtig sind in ihres Herzens Sinn.\n"
            "Er stößet die Gewaltigen von Stuhl\n"
            "und erhebet die Niedrigen.\n"
            "Hungrige füllet er mit Gütern\n"
            "und läßt die Reichen ledig ausgehen.\n"
            "Er denket der Barmherzigkeit\n"
            "und hilft seinem Knechte Israel auf.\n"
            "Wie er geredet hat zu unsern Vätern,\n"
            "Abraham und seinen Samen ewiglich."
        ),
        "italian": (
            "L'anima mia magnifica il Signore,\n"
            "e lo spirito mio esulta in Dio, mio salvatore.\n"
            "Perché ha guardato l'umiltà della sua serva.\n"
            "Ecco, d'ora in poi tutte le generazioni mi chiameranno beata.\n"
            "Grandi cose ha fatto in me l'Onnipotente,\n"
            "e santo è il suo nome.\n"
            "La sua misericordia si estende\n"
            "di generazione in generazione su quelli che lo temono.\n"
            "Ha manifestato la forza del suo braccio,\n"
            "ha disperso i superbi nei pensieri del loro cuore.\n"
            "Ha rovesciato i potenti dai troni,\n"
            "ha innalzato gli umili.\n"
            "Ha ricolmato di beni gli affamati,\n"
            "ha rimandato i ricchi a mani vuote.\n"
            "Ha soccorso Israele, suo servo,\n"
            "ricordandosi della sua misericordia.\n"
            "Come aveva promesso ai nostri padri,\n"
            "ad Abramo e alla sua discendenza per sempre."
        ),
        "latin": (
            "Magnificat anima mea Dominum,\n"
            "et exultavit spiritus meus in Deo salutari meo,\n"
            "quia respexit humilitatem ancillae suae.\n"
            "Ecce enim ex hoc beatam me dicent omnes generationes,\n"
            "quia fecit mihi magna qui potens est,\n"
            "et sanctum nomen eius,\n"
            "et misericordia eius in progenies et progenies\n"
            "timientibus eum.\n"
            "Fecit potentiam in brachio suo,\n"
            "dispersit superbos mente cordis sui.\n"
            "Deposuit potentes de sede\n"
            "et exaltavit humiles.\n"
            "Esurientes implevit bonis\n"
            "et divites dimisit inanes.\n"
            "Suscepit Israel, puer suus,\n"
            "recordatus misericordiae suae,\n"
            "sicut locutus est ad patres nostros,\n"
            "Abraham et semini eius in saecula."
        ),
        "french": (
            "Mon âme exalte le Seigneur,\n"
            "et mon esprit tressaille en Dieu, mon Sauveur,\n"
            "car il a jeté les yeux sur l'humilité de sa servante.\n"
            "Désormais toutes les générations m'appelleront bienheureuse,\n"
            "car le Tout-Puissant a fait en moi de grandes choses.\n"
            "Saint est son nom,\n"
            "et sa miséricorde s'étend d'âge en âge\n"
            "sur ceux qui le craignent.\n"
            "Il a montré la force de son bras;\n"
            "il a dispersé ceux qui s'enorgueillissaient dans les pensées de leur cœur.\n"
            "Il a précipité les puissants de leurs trônes,\n"
            "et il a élevé les humbles.\n"
            "Il a comblé de biens les affamés,\n"
            "et il a renvoyé les riches les mains vides.\n"
            "Il a secouru Israël, son serviteur,\n"
            "se souvenant de sa miséricorde,\n"
            "selon qu'il l'avait dit à nos pères,\n"
            "à Abraham et à sa descendance pour jamais."
        ),
        "spanish": (
            "Engrandece mi alma al Señor,\n"
            "y mi espíritu se alegra en Dios mi Salvador.\n"
            "Porque ha mirado la bajeza de su sierva;\n"
            "pues he aquí, desde ahora me dirán bienaventurada todas las generaciones.\n"
            "Porque el Poderoso ha hecho obras grandes en mí;\n"
            "santo es su nombre.\n"
            "Y su misericordia es de generación en generación\n"
            "a los que le temen.\n"
            "Hizo proezas con su brazo;\n"
            "esparció a los soberbios en el pensamiento de sus corazones.\n"
            "Quitó de los tronos a los poderosos,\n"
            "y exaltó a los humildes.\n"
            "A los hambrientos colmó de bienes,\n"
            "y a los ricos envió vacíos.\n"
            "Socorrió a Israel su siervo,\n"
            "acordándose de la misericordia,\n"
            "de la cual habló a nuestros padres,\n"
            "a Abraham y a su descendencia para siempre."
        ),
        "portuguese": (
            "A minha alma engrandece o Senhor,\n"
            "e o meu espírito se alegra em Deus, meu Salvador,\n"
            "porque atentou na humildade de sua serva.\n"
            "Pois, eis que desde agora todas as gerações me chamarão bem-aventurada,\n"
            "porquanto o Onipotente fez em mim grandes coisas,\n"
            "e seu nome é santo.\n"
            "E a sua misericórdia é de geração em geração\n"
            "sobre aqueles que o temem.\n"
            "Demonstrou o seu poder com o seu braço\n"
            "e dispersou os soberbos no pensamento de seus corações.\n"
            "Derrubou dos tronos os poderosos\n"
            "e exaltou os humildes.\n"
            "Encheu os famintos de bens\n"
            "e despediu vazios os ricos.\n"
            "Socorreu a Israel, seu servo,\n"
            "lembrando-se da sua misericórdia,\n"
            "como falou a nossos pais,\n"
            "a Abraão e à sua descendência para sempre."
        ),
        "polish": (
            "Wielbi dusza moja Pana,\n"
            "i raduje się duch mój w Bogu, moim Zbawicielu.\n"
            "Bo wejrzał na uniżenie służebnicy swojej.\n"
            "Otóż, od tego czasu będą mnie nazywać błogosławioną wszystkie pokolenia.\n"
            "Bo uczynił mi rzeczy wielkie Wszechmogący,\n"
            "i święte jest jego imię.\n"
            "A jego miłosierdzie rozciąga się ponad pokoleniami\n"
            "na tych, którzy się go boją.\n"
            "Wykazał moc ramienia swojego;\n"
            "rozpędził pychowych w myślach serca ich.\n"
            "Zdjął z tronu możnych\n"
            "i wywyższył pokory.\n"
            "Głodnych napełnił dobrami\n"
            "i bogatych odesłał z niczym.\n"
            "Wziął w opiekę Izraela, sługę swojego,\n"
            "pamiętając o miłosierdziu,\n"
            "jak mówił do ojców naszych,\n"
            "do Abrahama i jego potomstwa na wieki."
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
