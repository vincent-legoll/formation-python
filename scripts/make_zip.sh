#!/bin/bash

./scripts/nb2slides.sh
python scripts/remove_celltoolbar.py

rm -f formation-python.zip
zip -r formation-python.zip -@ < include.lst

# README.md
# scripts
# todo.txt
