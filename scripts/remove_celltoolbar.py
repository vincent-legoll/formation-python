# -*- coding: utf-8 -*-
"""Remove cell Toolbar from ipynb files"""

def process_nb(notebook):
    with open(notebook, 'rb') as in_file:
        data = in_file.readlines()
        print "File:", notebook
        try:
            data.remove('  "celltoolbar": "Slideshow",\n')
            print " > Line removed"
            line_removed = True
        except:
            print " > Line not removed !"
            line_removed = False
    if line_removed:
        with open(notebook, 'wb') as out_file:
            out_file.writelines(data)

notebooks = ('00-InitPython-generalites.ipynb',
             '01-InitPython-langage.ipynb',
             '02-InitPython-langage.ipynb',
             '03-InitPython-microprojet.ipynb')
            
for notebook in notebooks:
    process_nb(notebook)
