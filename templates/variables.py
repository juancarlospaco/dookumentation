#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Templates as viariables for Dookumentation."""


import os


__all__ = ["HTML_PLUS", "HTML_PLAIN", "RST", "MD", "ODT", "XML", "TXT"]


here = os.path.dirname(__file__)


HTML_PLAIN, HTML_PLUS, RST, MD, ODT, XML, TXT = "", "", "", "", "", "", ""


with open(os.path.join(here, "template.plain.html"), encoding="utf-8") as __html:
    HTML_PLAIN = __html.read()


with open(os.path.join(here, "template.html"), encoding="utf-8") as __html:
    HTML_PLUS = __html.read()


with open(os.path.join(here, "template.rst.md"), encoding="utf-8") as __rst_md:
    MD = RST = __rst_md.read()


with open(os.path.join(here, "template.fodt"), encoding="utf-8") as __odt:
    ODT = __odt.read()


with open(os.path.join(here, "template.xml"), encoding="utf-8") as __xml:
    XML = __xml.read()


with open(os.path.join(here, "template.txt"), encoding="utf-8") as __txt:
    TXT = __txt.read()
