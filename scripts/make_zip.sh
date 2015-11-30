#!/bin/bash

set -x

python scripts/remove_celltoolbar.py

./scripts/make_includes.sh

rm -f formation-python.zip
zip -r formation-python.zip -@ < include.lst
