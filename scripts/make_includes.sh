#!/bin/bash

incfile="include.lst"

# Add explicitely named files
cp manual_include.lst $incfile

# Add all .py files from exos dir
ls exos/*.py >> $incfile
