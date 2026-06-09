"""
prayers/psalm_23.py — The 23rd Psalm definition.

English text: King James Version (1611), public domain.
"""

from .base import Prayer, voices_for


Psalm23 = Prayer(
    name  = "psalm23",
    title = "The 23rd Psalm",
    native_titles = {
        "english":    "The Lord is my Shepherd",
        "german":     "Der Herr ist mein Hirte",
        "italian":    "Il Signore è il mio pastore",
        "latin":      "Dominus pascit me",
        "french":     "L'Éternel est mon berger",
        "spanish":    "El Señor es mi pastor",
        "portuguese": "O Senhor é o meu pastor",
        "polish":     "Pan jest moim pasterzem",
    },
    texts = {
        "english": (
            "The Lord is my shepherd; I shall not want.\n"
            "He maketh me to lie down in green pastures:\n"
            "he leadeth me beside the still waters.\n"
            "He restoreth my soul:\n"
            "he leadeth me in the paths of righteousness\n"
            "for his name's sake.\n"
            "Yea, though I walk through the valley\n"
            "of the shadow of death,\n"
            "I will fear no evil: for thou art with me;\n"
            "thy rod and thy staff they comfort me.\n"
            "Thou preparest a table before me\n"
            "in the presence of mine enemies:\n"
            "thou anointest my head with oil;\n"
            "my cup runneth over.\n"
            "Surely goodness and mercy shall follow me\n"
            "all the days of my life:\n"
            "and I will dwell in the house of the Lord for ever.\n"
            "Amen."
        ),
        "german": (
            "Der Herr ist mein Hirte, mir wird nichts mangeln.\n"
            "Er weidet mich auf einer grünen Aue\n"
            "und führet mich zum frischen Wasser.\n"
            "Er erquicket meine Seele.\n"
            "Er führet mich auf rechter Straße\n"
            "um seines Namens willen.\n"
            "Und ob ich schon wanderte im finstern Tal,\n"
            "fürchte ich kein Unglück;\n"
            "denn du bist bei mir,\n"
            "dein Stecken und Stab trösten mich.\n"
            "Du bereitest vor mir einen Tisch\n"
            "im Angesicht meiner Feinde.\n"
            "Du salbest mein Haupt mit Öl\n"
            "und schenkest mir voll ein.\n"
            "Gutes und Barmherzigkeit werden mir folgen\n"
            "mein Leben lang,\n"
            "und ich werde bleiben im Hause des Herrn immerdar.\n"
            "Amen."
        ),
        "italian": (
            "Il Signore è il mio pastore: non manco di nulla.\n"
            "Su pascoli erbosi mi fa riposare,\n"
            "ad acque tranquille mi conduce.\n"
            "Rinfranca l'anima mia.\n"
            "Mi guida per il giusto cammino\n"
            "a motivo del suo nome.\n"
            "Anche se vado per una valle oscura,\n"
            "non temo alcun male, perché tu sei con me.\n"
            "Il tuo bastone e il tuo vincastro\n"
            "mi danno sicurezza.\n"
            "Davanti a me tu prepari una mensa\n"
            "sotto gli occhi dei miei nemici.\n"
            "Ungi di olio il mio capo;\n"
            "il mio calice trabocca.\n"
            "Sì, bontà e fedeltà mi saranno compagne\n"
            "tutti i giorni della mia vita,\n"
            "abiterò nella casa del Signore per lunghi giorni.\n"
            "Amen."
        ),
        "latin": (
            "Dominus pascit me, nihil mihi deerit.\n"
            "In pascuis virentibus me collocat,\n"
            "super aquas quietis me adducit.\n"
            "Animam meam reficit.\n"
            "Deducit me per semitas iustitiae\n"
            "propter nomen suum.\n"
            "Nam et si ambulavero in valle umbrae mortis,\n"
            "non timebo mala, quoniam tu mecum es.\n"
            "Virga tua et baculus tuus,\n"
            "ipsa me consolabuntur.\n"
            "Pones coram me mensam\n"
            "adversus eos qui tribulant me.\n"
            "Impinguasti in oleo caput meum;\n"
            "calix meus inebrians quam praeclarus est.\n"
            "Et misericordia tua subsequetur me\n"
            "omnibus diebus vitae meae,\n"
            "et ut inhabitem in domo Domini\n"
            "in longitudinem dierum.\n"
            "Amen."
        ),
        "french": (
            "L'Éternel est mon berger: je ne manquerai de rien.\n"
            "Il me fait reposer dans de verts pâturages,\n"
            "il me dirige près des eaux paisibles.\n"
            "Il restaure mon âme.\n"
            "Il me conduit dans les sentiers de la justice,\n"
            "à cause de son nom.\n"
            "Quand je marche dans la vallée de l'ombre de la mort,\n"
            "je ne crains aucun mal, car tu es avec moi:\n"
            "ta houlette et ton bâton me rassurent.\n"
            "Tu dresses devant moi une table,\n"
            "en face de mes adversaires;\n"
            "tu oins d'huile ma tête,\n"
            "et ma coupe déborde.\n"
            "Oui, le bonheur et la grâce m'accompagneront\n"
            "tous les jours de ma vie,\n"
            "et j'habiterai dans la maison de l'Éternel\n"
            "pour de longs jours.\n"
            "Amen."
        ),
        "spanish": (
            "El Señor es mi pastor; nada me faltará.\n"
            "En lugares de delicados pastos me hará descansar;\n"
            "junto a aguas de reposo me pastoreará.\n"
            "Confortará mi alma.\n"
            "Me guiará por sendas de justicia\n"
            "por amor de su nombre.\n"
            "Aunque ande en valle de sombra de muerte,\n"
            "no temeré mal alguno, porque tú estarás conmigo;\n"
            "tu vara y tu cayado me infundirán aliento.\n"
            "Aderezas mesa delante de mí\n"
            "en presencia de mis angustiadores;\n"
            "unges mi cabeza con aceite;\n"
            "mi copa está rebosando.\n"
            "Ciertamente el bien y la misericordia me seguirán\n"
            "todos los días de mi vida,\n"
            "y en la casa del Señor moraré por largos días.\n"
            "Amén."
        ),
        "portuguese": (
            "O Senhor é o meu pastor; nada me faltará.\n"
            "Ele me faz repousar em pastos verdejantes.\n"
            "Leva-me para junto das águas tranquilas.\n"
            "Refrigera a minha alma.\n"
            "Guia-me pelas veredas da justiça\n"
            "por amor do seu nome.\n"
            "Ainda que eu andasse pelo vale da sombra da morte,\n"
            "não temeria mal algum, porque tu estás comigo;\n"
            "o teu cajado e o teu bordão me consolam.\n"
            "Preparas uma mesa perante mim\n"
            "na presença dos meus adversários.\n"
            "Unges a minha cabeça com óleo;\n"
            "o meu cálice transborda.\n"
            "Certamente que a bondade e a misericórdia\n"
            "me seguirão todos os dias da minha vida,\n"
            "e habitarei na casa do Senhor por longos dias.\n"
            "Amém."
        ),
        "polish": (
            "Pan jest moim pasterzem, nie brak mi niczego.\n"
            "Pozwala mi leżeć na zielonych pastwiskach.\n"
            "Prowadzi mnie nad wody, gdzie mogę odpocząć.\n"
            "Orzeźwia moją duszę.\n"
            "Wiedzie mnie po właściwych ścieżkach\n"
            "przez wzgląd na swoją chwałę.\n"
            "Chociażbym chodził ciemną doliną,\n"
            "zła się nie ulęknę, bo Ty jesteś ze mną.\n"
            "Twój kij i Twoja laska są moją pociechą.\n"
            "Zastawiasz przede mną stół\n"
            "wobec moich przeciwników.\n"
            "Namaszczasz olejkiem moją głowę,\n"
            "mój kielich jest pełny po brzegi.\n"
            "Dobroć i łaska będą mi towarzyszyć\n"
            "przez wszystkie dni mego życia\n"
            "i zamieszkam w domu Pana\n"
            "po najdłuższe czasy.\n"
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
