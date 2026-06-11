"""Dump PT->EN do django.po para montar a carga de dados (uso único)."""

import polib

po = polib.pofile("locale/en/LC_MESSAGES/django.po")
for e in po:
    if e.obsolete or not e.msgstr:
        continue
    print(repr(e.msgid))
    print("  =>", repr(e.msgstr))
