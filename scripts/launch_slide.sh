#!/bin/bash

if [ $# -eq 0 ]; then
  echo Usage: `basename $0` 0, 1, 2 or 3 [--execute] 1>&2
  exit 1
fi

port=`expr 8000 + $1`

case $1 in
  "0")
      nbfile="00-InitPython-generalites.ipynb"
      ;;
  "1")
      nbfile="01-InitPython-langage.ipynb"
      ;;
  "2")
      nbfile="02-InitPython-langage.ipynb"
      ;;
  "3")
      nbfile="03-InitPython-microprojet.ipynb"
      ;;
  *)
      exit
      ;;
  esac
set -x
jupyter-nbconvert $nbfile --to slides --post serve $2 --allow-errors --ServePostProcessor.port=$port
