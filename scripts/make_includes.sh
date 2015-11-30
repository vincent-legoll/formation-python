#!/bin/bash

incfile="include.lst"

cat > $incfile <<- EOM
00-InitPython-generalites.ipynb
01-InitPython-langage.ipynb
02-InitPython-langage.ipynb
03-InitPython-microprojet.ipynb
mon_module.py
test.py
fig/compile_interprete.png
fig/python-logo.png
fig/icon.png
interessant.txt
README.md
EOM

# Add all .py files from exos dir
ls exos/*.py >> $incfile
