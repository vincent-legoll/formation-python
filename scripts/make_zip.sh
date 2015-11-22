#!/bin/bash

./scripts/nb2slides.sh
python scripts/remove_celltoolbar.py

zip -r -i@include.lst formation-python.zip \
00-InitPython-generalites.ipynb \
00-InitPython-generalites.slides.html \
01-InitPython-langage.ipynb \
01-InitPython-langage.slides.html \
02-InitPython-langage.ipynb \
02-InitPython-langage.slides.html \
mon_module.py \
fig \
exos \
interessant.txt

# README.md
# scripts
# todo.txt
