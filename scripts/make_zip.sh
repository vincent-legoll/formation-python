#!/bin/bash

set -x

python scripts/process.py --pdf

./scripts/make_includes.sh

rm -f formation-python.zip
zip -r formation-python.zip -@ < include.lst
