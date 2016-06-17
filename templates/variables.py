#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Templates for Dookumentation."""


with open("template.html", encoding="utf-8") as html_template:
    HTML = html_template.read()


with open("template.rst.md", encoding="utf-8") as rst_md_template:
    MD = RST = rst_md_template.read()


with open("template.fodt", encoding="utf-8") as odt_template:
    ODT = odt_template.read()
