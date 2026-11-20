#!/usr/bin/env python3
import json, os
from PIL import Image as PILImage
from reportlab.lib.pagesizes import inch
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import *
from reportlab.pdfbase import pdfmetrics

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
BOOK_TITLES = {'english': 'The Book of Prayer', 'german': 'Das Buch des Gebets', 'spanish': 'El Libro de Oracion'}
VERSIONS = {'english': 'Version 2026-09-11', 'german': 'Versión 2026-09-11', 'spanish': 'Versión 2026-09-11'}

def flat_image(fname):
    out = os.path.join(FLAT_DIR, fname)
    if not os.path.exists(out):
        try:
            im = PILImage.open(os.path.join(IMG_DIR, fname))
            if im.mode in ('RGBA','LA','P'):
                bg = PILImage.new('RGB', im.size, (255,255,255))
                im2 = im.convert('RGBA')
                bg.paste(im2, mask=im2.split()[-1])
                im = bg
            else:
                im = im.convert('RGB')
            im.save(out)
        except Exception as e:
            print(f"Warning: Could not process {fname}: {e}")
            return None, (0, 0)
    try:
        im = PILImage.open(out)
        return out, im.size
    except:
        return None, (0, 0)

S_title = ParagraphStyle('BookTitle', fontName='Times-Roman', fontSize=32, leading=38, alignment=TA_CENTER, textColor=colors.HexColor('#2b2b2b'), spaceAfter=24)
S_subtitle = ParagraphStyle('Subtitle', fontName='Times-Roman', fontSize=14, leading=18, alignment=TA_CENTER, textColor=colors.HexColor('#555555'))
S_chapter = ParagraphStyle('ChapterTitle', fontName='Times-Roman', fontSize=18, leading=24, alignment=TA_CENTER, spaceAfter=12, textColor=colors.HexColor('#2b2b2b'))
S_verse = ParagraphStyle('Verse', fontName='Times-Roman', fontSize=11, leading=17, alignment=TA_CENTER, textColor=colors.HexColor('#333333'))

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
    story.append(Spacer(1, 3.5*inch))
    story.append(Paragraph(VERSIONS[lang], S_subtitle))
    story.append(PageBreak())
    
    # PRAYER PAGES
    for key in ORDER:
        title = TITLES[lang][key]
        img_path, (iw, ih) = flat_image(IMAGES[key])
        
        # Prayer title
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph(title, S_chapter))
        
        # Prayer image
        if img_path and iw > 0 and ih > 0:
            max_w, max_h = PAGE_W - 2*MARGIN, 2.2*inch
            scale = min(max_w/iw, max_h/ih)
            w, h = iw*scale, ih*scale
            story.append(Image(img_path, width=w, height=h))
        
        story.append(Spacer(1, 0.3*inch))
        
        # Prayer text
        if key in TEXTS and lang in TEXTS[key]:
            text = TEXTS[key][lang].strip()
            lines = [l.strip() for l in text.split('\n')]
            html = '<br/>'.join(l if l else '&nbsp;' for l in lines)
            story.append(Paragraph(html, S_verse))
        else:
            story.append(Paragraph(f"[Text not available]", S_verse))
        
        story.append(PageBreak())
    
    doc.multiBuild(story)

build_book('english', os.path.join(PRAY_DIR, 'docs/books/en/The_Book_of_Prayer.pdf'))
build_book('german', os.path.join(PRAY_DIR, 'docs/books/de/Das_Buch_des_Gebets.pdf'))
build_book('spanish', os.path.join(PRAY_DIR, 'docs/books/es/El_Libro_de_Oracion.pdf'))
print("✅ Complete PDFs with cover, images, text, and version 2026-09-11 generated!")
