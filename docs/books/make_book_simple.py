#!/usr/bin/env python3
import json, os
from PIL import Image as PILImage
from reportlab.lib.pagesizes import inch
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
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

S_chapter = ParagraphStyle('ChapterTitle', fontName="Times-Roman", fontSize=20, leading=26, alignment=TA_CENTER, spaceAfter=6)
S_verse = ParagraphStyle('Verse', fontName="Times-Roman", fontSize=12.5, leading=19.5, alignment=TA_CENTER)

def build_body(lang, outpath):
    doc = BaseDocTemplate(outpath, pagesize=(PAGE_W, PAGE_H), leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    frame = Frame(MARGIN, MARGIN, PAGE_W-2*MARGIN, PAGE_H-2*MARGIN, id='main')
    doc.addPageTemplates([PageTemplate(id='main', frames=[frame])])
    story = []
    
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

build_body('english', os.path.join(PRAY_DIR, 'docs/books/en/The_Book_of_Prayer.pdf'))
build_body('german', os.path.join(PRAY_DIR, 'docs/books/de/Das_Buch_des_Gebets.pdf'))
build_body('spanish', os.path.join(PRAY_DIR, 'docs/books/es/El_Libro_de_Oracion.pdf'))
print("✅ PDFs generated!")
