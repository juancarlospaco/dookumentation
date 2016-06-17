#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Templates for Dookumentation."""


import os


here = os.path.dirname(__file__)


with open(os.path.join(here, "template.html"), encoding="utf-8") as html_template:
    HTML = html_template.read()


with open(os.path.join(here, "template.rst.md"), encoding="utf-8") as rst_md_template:
    MD = RST = rst_md_template.read()


with open(os.path.join(here, "template.fodt"), encoding="utf-8") as odt_template:
    ODT = odt_template.read()


with open(os.path.join(here, "template.xml"), encoding="utf-8") as xml_template:
    XML = xml_template.read()
