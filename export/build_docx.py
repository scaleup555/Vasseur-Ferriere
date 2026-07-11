#!/usr/bin/env python3
"""Génère l'export Word (.docx) d'un tome à partir de son fichier .md source.

Format standard fixé par CLAUDE.md :
- Page 5,5 x 8,5 pouces (format poche), marges 0,6"/0,7"
- Times New Roman 12, interligne 1,15
- Titres de chapitre centrés
- Alinéa (retrait de première ligne) sur chaque paragraphe, y compris le premier de chaque chapitre

Usage: python3 build_docx.py <source.md> <output.docx>
"""
import sys
import re
from docx import Document
from docx.shared import Inches, Pt, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH


def build(src_path, out_path):
    with open(src_path, encoding="utf-8") as f:
        text = f.read()

    lines = [l.rstrip() for l in text.split("\n")]

    doc = Document()
    section = doc.sections[0]
    section.page_width = Inches(5.5)
    section.page_height = Inches(8.5)
    section.left_margin = Inches(0.6)
    section.right_margin = Inches(0.6)
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)

    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(12)

    def add_centered(text_, size, bold=False, space_after=0):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(text_)
        r.font.name = "Times New Roman"
        r.font.size = Pt(size)
        r.bold = bold
        p.paragraph_format.space_after = Pt(space_after)
        return p

    def add_body(text_):
        p = doc.add_paragraph()
        p.paragraph_format.first_line_indent = Inches(0.3)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(text_)
        r.font.name = "Times New Roman"
        r.font.size = Pt(12)
        return p

    def add_scene_break():
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("*")
        r.font.name = "Times New Roman"
        r.font.size = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        return p

    idx = 0
    # Title block: first non-empty lines until first blank line group, before "Chapitre 1"
    title_lines = []
    while idx < len(lines) and not lines[idx].startswith("Chapitre "):
        if lines[idx].strip():
            title_lines.append(lines[idx].strip())
        idx += 1

    if title_lines:
        add_centered(title_lines[0], 22, bold=True, space_after=6)
        for t in title_lines[1:]:
            add_centered(t, 14, space_after=6)
        doc.add_paragraph()

    chapter_re = re.compile(r"^Chapitre \d+ — .+$")

    while idx < len(lines):
        line = lines[idx]
        if chapter_re.match(line):
            doc.add_page_break()
            add_centered(line, 16, bold=True, space_after=24)
            idx += 1
            continue
        if line.strip() == "*":
            add_scene_break()
            idx += 1
            continue
        if line.strip():
            add_body(line.strip())
        idx += 1

    doc.save(out_path)
    print(f"Écrit : {out_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 build_docx.py <source.md> <output.docx>")
        sys.exit(1)
    build(sys.argv[1], sys.argv[2])
