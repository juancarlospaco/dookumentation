#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Templates as viariables for Dookumentation."""


import os


__all__ = ["HTML", "RST", "MD", "ODT", "XML"]


here = os.path.dirname(__file__)


with open(os.path.join(here, "template.html"), encoding="utf-8") as __html:
    HTML = __html.read()


with open(os.path.join(here, "template.rst.md"), encoding="utf-8") as __rst_md:
    MD = RST = __rst_md.read()


with open(os.path.join(here, "template.fodt"), encoding="utf-8") as __odt:
    ODT = __odt.read()


with open(os.path.join(here, "template.xml"), encoding="utf-8") as __xml:
    XML = __xml.read()
