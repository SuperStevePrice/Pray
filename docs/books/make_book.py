#!/usr/bin/env python3
"""
make_book.py — builds the Book of Pray (English) and Buch des Gebets (German)
as print-ready 6"x9" PDFs from the Pray repo's texts and images.
"""
import json, os, io
from PIL import Image as PILImage
from reportlab.lib.pagesizes import inch
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, PageBreak, Image, HRFlowable,
                                NextPageTemplate)
from reportlab.platypus.tableofcontents import TableOfContents
from pypdf import PdfReader, PdfWriter

PAGE_W, PAGE_H = 6*inch, 9*inch
MARGIN = 0.8*inch
IMG_DIR = '/home/claude/Pray/docs/images'
FLAT_DIR = '/home/claude/flat_images'
os.makedirs(FLAT_DIR, exist_ok=True)

pdfmetrics.registerFont(TTFont('EBG', '/home/claude/fonts/EBGaramond-Regular.ttf'))
pdfmetrics.registerFont(TTFont('EBGI', '/home/claude/fonts/EBGaramond-Italic.ttf'))

TEXTS = json.load(open('/home/claude/texts.json'))

ORDER = ['psalm23','ave','ave_verum','gloria','lords','magnificat',
         'miserere','nunc','peace','sanctus','serenity']

IMAGES = {"psalm23":"psalm23.png","ave":"ave-maria.png","ave_verum":"ave-verum-corpus.png",
          "gloria":"gloria.png","lords":"Breaking_of_The_Bread.png","magnificat":"magnificat.png",
          "miserere":"miserere.png","nunc":"nunc-dimittis.png","peace":"peace.png",
          "sanctus":"sanctus.png","serenity":"serenity.png"}

TITLES = {
 'english': {'psalm23':'The 23rd Psalm','ave':'Ave Maria','ave_verum':'Ave Verum Corpus',
   'gloria':'Gloria','lords':"The Lord's Prayer",'magnificat':'Magnificat',
   'miserere':'Miserere — Psalm 51','nunc':'Nunc Dimittis','peace':'The Peace Prayer',
   'sanctus':'Sanctus','serenity':'The Serenity Prayer'},
 'german': {'psalm23':'Psalm 23','ave':'Ave Maria','ave_verum':'Ave Verum Corpus',
   'gloria':'Gloria','lords':'Das Vaterunser','magnificat':'Magnificat',
   'miserere':'Miserere — Psalm 51','nunc':'Nunc Dimittis','peace':'Das Friedensgebet',
   'sanctus':'Sanctus','serenity':'Das Gelassenheitsgebet'},
}

META = {
 'english': dict(
    title='The Book of Prayer',
    subtitle='Eleven Sacred Prayers',
    author='Rodney Stephen (Steve) Price',
    contents='Contents',
    about_title='About Pray',
    about=[
      "<i>Pray</i> speaks sacred prayers aloud in eight languages, using your "
      "browser's built-in speech synthesis. The living app may be visited at "
      "<i>supersteveprice.github.io/Pray</i>.",
      "Created by Rodney Stephen (Steve) Price, 2026.",
      "Devotional artwork, including <i>The First Eucharist</i>, is AI-generated, "
      "directed by Rodney Stephen (Steve) Price, 2026.",
      "Prayer texts are traditional liturgical and biblical texts in the "
      "public domain.",
      "Cover: alpine landscape.",
      "<i>Pray</i> is open source: <i>github.com/SuperStevePrice/Pray</i>."
    ],
    version='Version 2026-07-08 · 9b01e2e',
    colophon="Set in EB Garamond · MMXXVI"),
 'german': dict(
    title='Das Buch des Gebets',
    subtitle='Elf heilige Gebete',
    author='Rodney Stephen (Steve) Price',
    contents='Inhalt',
    about_title='Über Pray',
    about=[
      "<i>Pray</i> spricht heilige Gebete in acht Sprachen laut aus und nutzt "
      "dabei die im Browser eingebaute Sprachsynthese. Die lebendige App findet "
      "sich unter <i>supersteveprice.github.io/Pray</i>.",
      "Erstellt von Rodney Stephen (Steve) Price, 2026.",
      "Die Andachtsbilder, darunter <i>The First Eucharist</i> (Die erste "
      "Eucharistie), sind KI-generiert, gestaltet unter der Leitung von "
      "Rodney Stephen (Steve) Price, 2026.",
      "Die Gebetstexte sind überlieferte liturgische und biblische Texte, "
      "die gemeinfrei sind.",
      "Umschlag: Alpenlandschaft.",
      "<i>Pray</i> ist quelloffen: <i>github.com/SuperStevePrice/Pray</i>."
    ],
    version='Version 2026-07-08 · 9b01e2e',
    colophon="Gesetzt in EB Garamond · MMXXVI"),
}

def flat_image(fname):
    """Flatten RGBA onto white; return path to a clean RGB PNG plus (w,h)."""
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

# ---------- styles ----------
S_title    = ParagraphStyle('BookTitle', fontName='EBG', fontSize=30, leading=36,
                            alignment=TA_CENTER, textColor=colors.HexColor('#2b2b2b'))
S_subtitle = ParagraphStyle('BookSub', fontName='EBGI', fontSize=15, leading=20,
                            alignment=TA_CENTER, textColor=colors.HexColor('#555555'))
S_author   = ParagraphStyle('Author', fontName='EBG', fontSize=13, leading=18,
                            alignment=TA_CENTER)
S_chapter  = ParagraphStyle('ChapterTitle', fontName='EBG', fontSize=20, leading=26,
                            alignment=TA_CENTER, spaceAfter=6)
S_verse    = ParagraphStyle('Verse', fontName='EBG', fontSize=12.5, leading=19.5,
                            alignment=TA_CENTER)
S_body     = ParagraphStyle('Body', fontName='EBG', fontSize=11.5, leading=17,
                            alignment=TA_CENTER)
S_colophon = ParagraphStyle('Colophon', fontName='EBGI', fontSize=10, leading=14,
                            alignment=TA_CENTER, textColor=colors.HexColor('#777777'))
S_toc      = ParagraphStyle('TOCEntry', fontName='EBG', fontSize=12, leading=20)

class BookDoc(BaseDocTemplate):
    def afterFlowable(self, f):
        if isinstance(f, Paragraph) and f.style.name == 'ChapterTitle':
            self.notify('TOCEntry', (0, f.getPlainText(), self.page))

def page_decor(canv, doc):
    canv.saveState()
    canv.setFont('EBG', 10)
    canv.setFillColor(colors.HexColor('#666666'))
    canv.drawCentredString(PAGE_W/2, 0.45*inch, str(canv.getPageNumber()))
    canv.restoreState()

def plain_page(canv, doc):
    pass

def rule():
    return HRFlowable(width='22%', thickness=0.6, color=colors.HexColor('#999999'),
                      spaceBefore=4, spaceAfter=16, hAlign='CENTER')

def build_body(lang, outpath):
    m = META[lang]
    doc = BookDoc(outpath, pagesize=(PAGE_W, PAGE_H),
                  leftMargin=MARGIN, rightMargin=MARGIN,
                  topMargin=MARGIN, bottomMargin=MARGIN,
                  title=m['title'], author=m['author'])
    frame = Frame(MARGIN, MARGIN, PAGE_W-2*MARGIN, PAGE_H-2*MARGIN, id='main')
    doc.addPageTemplates([
        PageTemplate(id='plain', frames=[frame], onPage=plain_page),
        PageTemplate(id='numbered', frames=[frame], onPage=page_decor),
    ])

    story = []
    # --- title page (unnumbered) ---
    story.append(Spacer(1, 2.1*inch))
    story.append(Paragraph(m['title'], S_title))
    story.append(Spacer(1, 0.25*inch))
    story.append(rule())
    story.append(Paragraph(m['subtitle'], S_subtitle))
    story.append(Spacer(1, 2.2*inch))
    story.append(Paragraph(m['author'], S_author))
    story.append(NextPageTemplate('numbered'))
    story.append(PageBreak())

    # --- contents ---
    story.append(Spacer(1, 0.4*inch))
    story.append(Paragraph(m['contents'], S_chapter))
    story.append(rule())
    toc = TableOfContents()
    toc.levelStyles = [S_toc]
    toc.dotsMinLevel = 0
    story.append(toc)
    story.append(PageBreak())

    # --- chapters ---
    usable_w = PAGE_W - 2*MARGIN
    for i, key in enumerate(ORDER):
        title = TITLES[lang][key]
        path, (iw, ih) = flat_image(IMAGES[key])
        # fit image below the title: max width usable, max height 5.6in
        max_w, max_h = usable_w, 5.6*inch
        scale = min(max_w/iw, max_h/ih)
        w, h = iw*scale, ih*scale

        story.append(Spacer(1, 0.15*inch))
        story.append(Paragraph(title, S_chapter))
        story.append(rule())
        story.append(Image(path, width=w, height=h))
        story.append(PageBreak())

        text = TEXTS[key][lang].strip()
        lines = [l.strip() for l in text.split('\n')]
        html = '<br/>'.join(l if l else '&nbsp;' for l in lines)
        story.append(Spacer(1, 0.55*inch))
        story.append(Paragraph(html, S_verse))
        story.append(PageBreak())

    # --- About / Info (last page, mirrors the app's Info modal) ---
    story.append(Spacer(1, 0.4*inch))
    story.append(Paragraph(m['about_title'], S_chapter))
    story.append(rule())
    for para in m['about']:
        story.append(Paragraph(para, S_body))
        story.append(Spacer(1, 10))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph(m['version'], S_colophon))
    story.append(Spacer(1, 4))
    story.append(Paragraph(m['colophon'], S_colophon))

    doc.multiBuild(story)

def build_cover(lang, outpath):
    from reportlab.graphics.barcode.qr import QrCodeWidget
    from reportlab.graphics.shapes import Drawing
    from reportlab.graphics import renderPDF

    m = META[lang]
    c = pdfcanvas.Canvas(outpath, pagesize=(PAGE_W, PAGE_H))

    # full-bleed portrait crop featuring the lakeside church (right of image)
    c.drawImage('/home/claude/cover_church.png', 0, 0,
                width=PAGE_W, height=PAGE_H)

    # translucent title band across the sky, above the steeple
    band_h = 1.5*inch
    band_y = PAGE_H - band_h
    c.setFillColor(colors.Color(0, 0, 0, alpha=0.42))
    c.rect(0, band_y, PAGE_W, band_h, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont('EBG', 29)
    c.drawCentredString(PAGE_W/2, band_y + band_h - 0.72*inch, m['title'])
    c.setFont('EBGI', 13.5)
    c.drawCentredString(PAGE_W/2, band_y + band_h - 1.14*inch, m['subtitle'])

    # author band at the foot
    c.setFillColor(colors.Color(0, 0, 0, alpha=0.42))
    c.rect(0, 0, PAGE_W, 0.55*inch, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont('EBG', 12.5)
    c.drawCentredString(PAGE_W/2, 0.21*inch, m['author'])

    # QR tile, lower-left over the water, clear of the church
    qr_size = 1.0*inch
    pad = 6
    qx, qy = 0.5*inch, 0.95*inch
    c.setFillColor(colors.Color(1, 1, 1, alpha=0.92))
    c.roundRect(qx - pad, qy - pad, qr_size + 2*pad, qr_size + 2*pad,
                5, stroke=0, fill=1)
    qr = QrCodeWidget('https://supersteveprice.github.io/Pray/',
                      barLevel='M', barBorder=1)
    b = qr.getBounds()
    d = Drawing(qr_size, qr_size,
                transform=[qr_size/(b[2]-b[0]), 0, 0,
                           qr_size/(b[3]-b[1]), 0, 0])
    d.add(qr)
    renderPDF.draw(d, c, qx, qy)
    c.setFillColor(colors.white)
    c.setFont('EBGI', 9.5)
    c.drawString(qx - pad, qy - pad - 0.22*inch,
                 'supersteveprice.github.io/Pray')
    c.showPage()
    c.save()

def assemble(lang, final):
    cov, body = f'/home/claude/cover_{lang}.pdf', f'/home/claude/body_{lang}.pdf'
    build_cover(lang, cov)
    build_body(lang, body)
    w = PdfWriter()
    for p in PdfReader(cov).pages: w.add_page(p)
    for p in PdfReader(body).pages: w.add_page(p)
    with open(final, 'wb') as f:
        w.write(f)
    print(final, len(w.pages), 'pages')

assemble('english', '/home/claude/The_Book_of_Prayer.pdf')
assemble('german',  '/home/claude/Das_Buch_des_Gebets.pdf')
