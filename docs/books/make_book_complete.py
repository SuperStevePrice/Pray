#!/usr/bin/env python3
import json, os
from PIL import Image as PILImage
from reportlab.lib.pagesizes import inch
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import *

PRAY_DIR = "/Users/steve/Projects/Pray"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PAGE_W, PAGE_H = 6*inch, 9*inch
MARGIN = 0.8*inch
IMG_DIR = os.path.join(PRAY_DIR, 'docs/images')
FLAT_DIR = os.path.join(SCRIPT_DIR, 'flat_images')
os.makedirs(FLAT_DIR, exist_ok=True)

TEXTS = json.load(open(os.path.join(SCRIPT_DIR, 'texts.json')))
ORDER = ['psalm23','ave','hail-mary','ave_verum','gloria','lords','magnificat','miserere','nunc','peace','sanctus','serenity']
IMAGES = {"psalm23":"psalm23.png","ave":"ave-maria.png","hail-mary":"hail-mary.png","ave_verum":"ave-verum-corpus.png","gloria":"gloria.png","lords":"Breaking_of_The_Bread.png","magnificat":"magnificat.png","miserere":"miserere.png","nunc":"nunc-dimittis.png","peace":"peace.png","sanctus":"sanctus.png","serenity":"serenity.png"}
TITLES = {'english': {'psalm23':'The 23rd Psalm','ave':'Ave Maria','hail-mary':'Hail Mary','ave_verum':'Ave Verum Corpus','gloria':'Gloria','lords':"The Lord's Prayer",'magnificat':'Magnificat','miserere':'Miserere — Psalm 51','nunc':'Nunc Dimittis','peace':'The Peace Prayer','sanctus':'Sanctus','serenity':'The Serenity Prayer'},'german': {'psalm23':'Psalm 23','ave':'Ave Maria','hail-mary':'Gegrüßet seist du, Maria','ave_verum':'Ave Verum Corpus','gloria':'Gloria','lords':'Das Vaterunser','magnificat':'Magnificat','miserere':'Miserere — Psalm 51','nunc':'Nunc Dimittis','peace':'Das Friedensgebet','sanctus':'Sanctus','serenity':'Das Gelassenheitsgebet'},'spanish': {'psalm23':'Salmo 23','ave':'Ave María','hail-mary':'Dios te salve, María','ave_verum':'Ave Verum Corpus','gloria':'Gloria','lords':'El Padrenuestro','magnificat':'Magníficat','miserere':'Miserere — Salmo 51','nunc':'Nunc Dimittis','peace':'La Oración por la Paz','sanctus':'Sanctus','serenity':'La Oración de la Serenidad'}}
BOOK_TITLES = {'english': 'A Book of Common Prayer', 'german': 'Ein Buch des gemeinsamen Gebets', 'spanish': 'Un Libro de Oración Común'}
VERSIONS = {'english': 'Version 2026-09-11', 'german': 'Versión 2026-09-11', 'spanish': 'Versión 2026-09-11'}

def flat_image(fname):
    out = os.path.join(FLAT_DIR, fname)
    if not os.path.exists(out):
        im = PILImage.open(os.path.join(IMG_DIR, fname))
        if im.mode in ('RGBA','LA','P'):
            bg = PILImage.new('RGB', im.size, (255,255,255))
            im2 = im.convert('RGBA')
            bg.paste(im2, mask=im2.split()[-1])
            im = bg
        else:
            im = im.convert('RGB')
        im.save(out)
    im = PILImage.open(out)
    return out, im.size

S_title = ParagraphStyle('BookTitle', fontName='Times-Roman', fontSize=32, leading=38, alignment=TA_CENTER, textColor=colors.HexColor('#2b2b2b'), spaceAfter=24)
S_subtitle = ParagraphStyle('Subtitle', fontName='Times-Roman', fontSize=14, leading=18, alignment=TA_CENTER, textColor=colors.HexColor('#555555'))
S_chapter = ParagraphStyle('ChapterTitle', fontName='Times-Roman', fontSize=20, leading=26, alignment=TA_CENTER, spaceAfter=6)
S_verse = ParagraphStyle('Verse', fontName='Times-Roman', fontSize=12.5, leading=19.5, alignment=TA_CENTER)
S_credit_head = ParagraphStyle('CreditHead', fontName='Times-Bold', fontSize=15, leading=20, alignment=TA_CENTER, spaceAfter=18, textColor=colors.HexColor('#2b2b2b'))
S_credit_body = ParagraphStyle('CreditBody', fontName='Times-Roman', fontSize=11, leading=17, alignment=TA_LEFT, spaceAfter=10)

CREDITS_TITLE = {
    'english': 'Copyright &amp; Attribution',
    'german': 'Copyright &amp; Urheberrechte',
    'spanish': 'Derechos de Autor y Atribución',
}
CREDITS_BODY = {
    'english': [
        'This collection brings together prayers from the Christian tradition, believed to be in the public domain, '
        'alongside original content prepared for this edition.',
        '<b>Hail Mary (2026)</b> — original composition written by Steve Price.',
        'All artwork in this volume was created by ChatGPT, under the direction of Steve Price.',
        '© 2026 Steve Price. Compilation, arrangement, and original content.',
    ],
    'german': [
        'Diese Sammlung vereint Gebete aus der christlichen Tradition, die als gemeinfrei gelten, '
        'zusammen mit Originalinhalten, die für diese Ausgabe verfasst wurden.',
        '<b>Gegrüßet seist du, Maria (2026)</b> — Originalkomposition, verfasst von Steve Price.',
        'Alle Kunstwerke in diesem Band wurden von ChatGPT unter der Leitung von Steve Price erstellt.',
        '© 2026 Steve Price. Zusammenstellung, Anordnung und Originalinhalte.',
    ],
    'spanish': [
        'Esta colección reúne oraciones de la tradición cristiana, consideradas de dominio público, '
        'junto con contenido original preparado para esta edición.',
        '<b>Dios te salve, María (2026)</b> — composición original escrita por Steve Price.',
        'Todas las obras de arte de este volumen fueron creadas por ChatGPT, bajo la dirección de Steve Price.',
        '© 2026 Steve Price. Compilación, disposición y contenido original.',
    ],
}

# Per-prayer source notes, shown in English in every edition for consistency.
SOURCE_NOTES_HEAD = {
    'english': 'Sources',
    'german': 'Quellen',
    'spanish': 'Fuentes',
}
SOURCE_NOTES_INTRO = {
    'english': 'Traditional and scriptural sources for the prayers in this edition (listed in English for consistency across translations):',
    'german': 'Traditionelle und biblische Quellen der Gebete in dieser Ausgabe (zur Einheitlichkeit über alle Übersetzungen hinweg auf Englisch angegeben):',
    'spanish': 'Fuentes tradicionales y bíblicas de las oraciones de esta edición (indicadas en inglés para mantener la coherencia entre las traducciones):',
}
SOURCE_NOTES = [
    'The 23rd Psalm — traditional biblical text (Hebrew Scriptures), public domain.',
    'Ave Maria — traditional Catholic prayer based on Luke 1, public domain.',
    'Hail Mary — see note above regarding the 2026 composition.',
    'Ave Verum Corpus — medieval Eucharistic hymn, traditionally attributed to Pope Innocent VI (14th century), public domain.',
    'Gloria — traditional liturgical text (Gloria in Excelsis Deo), public domain.',
    "The Lord's Prayer — from the Gospels (Matthew 6, Luke 11), public domain.",
    'Magnificat — the Song of Mary, from the Gospel of Luke 1, public domain.',
    'Miserere (Psalm 51) — traditional biblical text, public domain.',
    'Nunc Dimittis — the Song of Simeon, from the Gospel of Luke 2, public domain.',
    'The Peace Prayer — commonly attributed to St. Francis of Assisi; its familiar modern wording dates to the early 20th century.',
    "Sanctus — traditional liturgical text, drawing on Isaiah 6:3 and Revelation 4:8, public domain.",
    'The Serenity Prayer — commonly attributed to the American theologian Reinhold Niebuhr.',
]

def build_book(lang, outpath):
    doc = BaseDocTemplate(outpath, pagesize=(PAGE_W, PAGE_H), leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    frame = Frame(MARGIN, MARGIN, PAGE_W-2*MARGIN, PAGE_H-2*MARGIN, id='main')
    doc.addPageTemplates([PageTemplate(id='main', frames=[frame])])
    story = []
    
    # COVER PAGE
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph(BOOK_TITLES[lang], S_title))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Sacred Prayers in Many Voices", S_subtitle))
    story.append(Spacer(1, 2.0*inch))
    story.append(Paragraph(VERSIONS[lang], S_subtitle))
    story.append(PageBreak())

    # COPYRIGHT & ATTRIBUTION PAGE
    story.append(Spacer(1, 0.4*inch))
    story.append(Paragraph(CREDITS_TITLE[lang], S_credit_head))
    for para in CREDITS_BODY[lang]:
        story.append(Paragraph(para, S_credit_body))
    story.append(Spacer(1, 0.25*inch))
    story.append(Paragraph(SOURCE_NOTES_HEAD[lang], S_credit_head))
    story.append(Paragraph(SOURCE_NOTES_INTRO[lang], S_credit_body))
    for note in SOURCE_NOTES:
        story.append(Paragraph('• ' + note, S_credit_body))
    story.append(PageBreak())

    # PRAYER PAGES
    for key in ORDER:
        title = TITLES[lang][key]
        path, (iw, ih) = flat_image(IMAGES[key])
        max_w, max_h = PAGE_W - 2*MARGIN, 5.6*inch
        scale = min(max_w/iw, max_h/ih)
        w, h = iw*scale, ih*scale
        
        story.append(Spacer(1, 0.15*inch))
        story.append(Paragraph(title, S_chapter))
        story.append(Image(path, width=w, height=h))
        story.append(PageBreak())
        
        text = TEXTS[key][lang].strip()
        lines = [l.strip() for l in text.split('\n')]
        html = '<br/>'.join(l if l else '&nbsp;' for l in lines)
        story.append(Spacer(1, 0.55*inch))
        story.append(Paragraph(html, S_verse))
        story.append(PageBreak())
    
    doc.multiBuild(story)

build_book('english', os.path.join(PRAY_DIR, 'docs/books/en/The_Book_of_Prayer.pdf'))
build_book('german', os.path.join(PRAY_DIR, 'docs/books/de/Das_Buch_des_Gebets.pdf'))
build_book('spanish', os.path.join(PRAY_DIR, 'docs/books/es/El_Libro_de_Oracion.pdf'))
print("✅ Complete PDFs with cover pages generated!")
