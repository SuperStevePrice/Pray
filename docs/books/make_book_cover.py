#!/usr/bin/env python3
import json, os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

PRAY_DIR = "/Users/steve/Projects/Pray"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PAGE_W, PAGE_H = 6*inch, 9*inch

TEXTS = json.load(open(os.path.join(SCRIPT_DIR, 'texts.json')))
ORDER = ['psalm23','ave','hail-mary','ave_verum','gloria','lords','magnificat','miserere','nunc','peace','sanctus','serenity']

def build_pdf(lang, outfile):
    c = canvas.Canvas(outfile, pagesize=(PAGE_W, PAGE_H))
    
    # COVER PAGE
    c.setFont("Times-Roman", 32)
    titles = {'english': 'The Book of Prayer', 'german': 'Das Buch des Gebets', 'spanish': 'El Libro de Oracion'}
    c.drawCentredString(PAGE_W/2, PAGE_H * 0.6, titles[lang])
    c.setFont("Times-Roman", 14)
    c.drawCentredString(PAGE_W/2, PAGE_H * 0.5, "Sacred Prayers in Many Voices")
    c.drawCentredString(PAGE_W/2, PAGE_H * 0.2, "Version 2026-09-11")
    c.showPage()
    
    # Prayer pages
    c.setFont("Times-Roman", 12)
    for key in ORDER:
        c.drawString(0.5*inch, PAGE_H - 0.8*inch, key.upper())
        c.showPage()
    
    c.save()

build_pdf('english', os.path.join(PRAY_DIR, 'docs/books/en/The_Book_of_Prayer.pdf'))
build_pdf('german', os.path.join(PRAY_DIR, 'docs/books/de/Das_Buch_des_Gebets.pdf'))
build_pdf('spanish', os.path.join(PRAY_DIR, 'docs/books/es/El_Libro_de_Oracion.pdf'))
print("✅ PDFs with covers generated!")
