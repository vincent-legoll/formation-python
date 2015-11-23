#!/bin/bash

python scripts/remove_celltoolbar.py

rm -f formation-python.zip
zip -r formation-python.zip -@ < include.lst
