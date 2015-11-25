#!/bin/bash

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
