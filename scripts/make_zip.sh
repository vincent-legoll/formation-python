#!/bin/bash

set -x

# Remove slideshow lines and convert to pdf
python scripts/process.py $1

./scripts/make_includes.sh

rm -f formation-python.zip
zip -r formation-python.zip -@ < include.lst
