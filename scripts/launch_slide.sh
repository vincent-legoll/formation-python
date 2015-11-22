#!/bin/bash

case $1 in
  "0")
      jupyter-nbconvert 00-InitPython-generalites.ipynb --to slides --post serve --ServePostProcessor.port=8000
      ;;
  "1")
      jupyter-nbconvert 01-InitPython-langage.ipynb --to slides --post serve --ServePostProcessor.port=8001
      ;;
  "2")
      jupyter-nbconvert 02-InitPython-langage.ipynb --to slides --post serve --ServePostProcessor.port=8002
      ;;
  esac
