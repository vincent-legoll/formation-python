#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Remove lines containing certain strings from a text file"""

from sys import argv
from latex import build_pdf, LatexBuildError
import os


def remove_line(file_name, bad_strings):
    """remove bad strings line from_filename"""

    with open(file_name, 'r') as in_file:
        data = in_file.readlines()
        newdata = [line for line in data
                   if not any(bad_string in line
                              for bad_string in bad_strings)]

    with open(file_name, 'w') as out_file:
        out_file.writelines(newdata)


def add_line(file_name, in_line, line_to_add):
    """Add a line after a given line in file_name"""

    with open(file_name, 'r') as in_file:
        data = in_file.readlines()
        newdata = []
        for line in data:
            newdata.append(line)
            if in_line in line:
                newdata.append(line_to_add)

    with open(file_name, 'w') as out_file:
        out_file.writelines(newdata)


def replace_string(file_name, old_string, new_string):
    """Replace old_string by new_string in file_name"""

    with open(file_name, 'r') as in_file:
        data = in_file.read()
        newdata = data.replace(old_string, new_string)

    with open(file_name, 'w') as out_file:
        out_file.write(newdata)


def escape_latex(tex_file_name):
    """Escape some characters in latex file"""

    with open(tex_file_name, 'r') as in_file:
        data = in_file.read()
        char_escape = {
                       '\\n\n': '\\verb \\n \\ \n',
                       '\\t\n': '\\verb \\t \\ \n',
                       '\\uXXXX': '\\verb \\uXXXX ~'
                       }
        newdata = data[:]
        for char, newchar in char_escape.iteritems():
            newdata = newdata.replace(char, newchar)

    with open(tex_file_name, 'w') as out_file:
        out_file.write(newdata)


def remove_from_latex(tex_file_name, block_start, block_end):
    """Remove block of lines that cannot be compiled with pdflatex"""

    with open(tex_file_name, 'r') as in_file:
        content = in_file.readlines()
        # Get index of line containing block_start
        iend = 0
        for (index, line) in enumerate(content):
            if block_start in line:
                istart = index
            elif block_end in line:
                iend = index
                break

        if iend:
            removed = content[istart:iend]
            print ">>> Warning! The following lines will be removed",\
                  "from {}:\n".format(tex_file_name)
            for line in removed:
                print "\t", line
            print "because they cannote be compiled with pdflatex."
            newcontent = content[:istart] + content[iend:]
        else:
            newcontent = content

    with open(tex_file_name, 'w') as out_file:
        out_file.writelines(newcontent)


def clean_latex_files(notebook_file_name):
    """Clean .tex, .log, .aux, out, pdf files corresponding to notebook"""

    extensions = (".tex", ".log", ".aux", ".out", ".synctex.gz", ".pdf")
    prefix = notebook_file_name.split('.ipynb')[0]
    print ">>>> Cleaning files"
    for extension in extensions:
        file_name = prefix + extension
        try:
            os.remove(file_name)
            print "\t", file_name
        except OSError:
            pass


def latex_to_pdf(tex_file_name):
    """Convert .tex file to pdf using tex module """

    pdf_file_name = tex_file_name.replace('.tex', '.pdf')
    print ">>> Converting {} to {}".format(tex_file_name, pdf_file_name)

    escape_latex(tex_file_name)  # Convert some characters to latex

    # Remove block containing chess and Japanese characters
    block_start = "Premièrement, des chaînes contenant"
    block_end = "Des chaînes dans lesquelles les séquences d'échappement"
    remove_from_latex(tex_file_name, block_start, block_end)

    # Require to work in current working dir because figure path are relative
    current_dir = os.getcwd()
    try:
        pdf = build_pdf(open(tex_file_name), texinputs=[current_dir, ''])
        pdf.save_to(pdf_file_name)
    except LatexBuildError as e:
        for err in e.get_errors():
            print u'Error in {0[filename]}, line {0[line]}: {0[error]}'\
                 .format(err)
            for msg in err['context'][1:]:
                print u'    {}'.format(msg.decode('utf-8'))
            print


if __name__ == '__main__':
    remove_line(argv[1])
    if argv[2]:
        bad_strings = argv[2]
    else:
        bad_strings = ['\caption{}', '\maketitle']
