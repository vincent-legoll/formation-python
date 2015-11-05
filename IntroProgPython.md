Introduction à la Programmation Python

1. Programmation
================

Qu'est-ce que c'est ?

- maths, formules, logique, algorithmes => recettes de cuisine !

- on parle à l'ordinateur pour lui demander de faire quelque chose
  langage: au sens linguistique: syntaxe et orthographe, vocabulaire
  texte structuré : suites logiques de phrases organisées pour exprimmer
  la recette

2. Historique
=============

Guido van Rossum (hollandais), a créé ce langage en 1991
qui travaille maintenant chez dropbox après 7 ans chez google

PEP 20 (The Zen of Python)

interpréteurs
-------------

- CPython
- Jython => Java byte code
- IronPython => .NET
- Pyjamas => JavaScript
- Shed Skin => C++
- Cython and Pyrex => C
- Pypy / RPython => C, Java bytecode CLR

science
-------

- NumPy
- SciPy
- Matplotlib
- BioPython

3. Contexte
===========

https://en.wikipedia.org/wiki/List_of_Python_software

4. Documentation
================

- python.org (doc, faq, stdlib, tuto, etc...)
- stackoverflow

5. Langage Python et sa Syntaxe
===============================

variables
---------

- assignation: '='
- pas de type: c'est la donnée qui est typée, pas la variable qui la référence

- copie ou référence
- modifiable ou non
- del()

types de données
----------------

- None
- booléens: logique vrai/faux
- numériques: entiers, flottants (précision, flou, arrondis, approximations), complexes
  * limites en info != maths, les nombres ne sont pas infinis (sys.maxint)
  * 1 == 1L == 1.0 == complex(1,0) et pourtant id(1) != id(1.0), la comparaison n'est pas l'identité
- séquences:
  * list()
  * tuple()
  * chaines de caractères: str()
  * indexing, negative indexes, slicing
- dict()
- ensembles: set()
- littéraux {}, methodes dict(), etc...
- fichiers: open(), close()

chaines
-------

- multiligne, "'" vs '"'
- formattage : %

opérateurs
----------

- binaires |^&
- logiques and or not cmp() > < ==
- arithmétiques +, -, *, /, **, and %
- assignation += -= /=
- compatibilité de type, coercission de type
  1 + '1' => TypeError: unsupported operand type(s) for +: 'int' and 'str'
  str(1) + '1' => '11'
  1 + int('1') => 2
  int(str(1) + '1') => 11

structures de contrôle
----------------------

- pass
- tests: if / elif / else
- boucles
  * for elt in liste
  * for idx in range(len(liste))
  * while
  * break
  * continue
- fonctions
  * arguments
  * valeurs par defaut
- with
- exceptions, try /catch

mise en page
------------

- indentation
- blocs de code
- caractères blancs (tabs vs spaces)
- ":"

commentaires
------------

- rendre le code plus compréhensible
- lisibilité (avec les espaces entre les expressions, etc...)

builtins
--------

- print()
- range()
- input()
- min(), max()
- sorted(), reversed()

modules
-------

- import
- packages

OOP
---

- classes
- instances
- self
- '==' vs id() vs hash()

stdlib - details
----------------

- string (find, count, split, join, strip, upper, replace)
- math (log, sqrt, cos, pi, e)
- os (listdir, getcwd, getenv, chdir, environ)
- os.path (exists, getsize, isdir, join)
- sys (sys.argv, sys.exit)

stdlib - à creuser
------------------

- re
- random
- pickle
- time, datetime
- compression: zlib, etc...
- crypto: md5
- argparse
- subprocess
- réseau: email, urllib
- xml
- unittest
- debugger: pdb
- profiler
- formatter

plus loin encore
----------------

- pypi: 66K packages - "pip install --user"
- numpy: calcul numérique
- matplotlib: graphiques à la matlab ou mathematica
- sympy: mathématiques symboliques
- scipy: ensemble de logiciels pour scientifiques (numpy, matplotlib, etc...)
- opencv: computer vision - traitement d'images en temlps réel
- pyopencl, pycuda, etc...: calculs GPGPU
- beaucoup de librairies C, C++ ou autres sont accessibles en python

6. Bonnes Pratiques
===================

- IDE: pydev
- Source control / version control
- meld
- pep8
- pylint
- tox
- virtualenv

7. Monty Python
===============

Et maintenant quelque chose de complètement différent
Le sens de la vie
Wanda
Brazil
Perroquet mort
Chevalier qui dit "Ni"

8. Exercices
============

numeric
-------

def ttc(liste):
    return sum(liste) * 1.186

chaines de caractères
---------------------

- majuscules / minuscules: toupper(), tolower(), inverse_maj(), capitalize()
- remplace()

listes
------

- reverse()
- odd_indices([1,2,3,4,5]) => [2,4]
- odds([1,2,3,4,5]) => [1,3,5]

maps
----

- animal_count(['coq', 'chien', 'coq', 'chat', 'chat', 'vache', 'coq', 'chien']) =>
  {'coq': 3, 'chien': 2, 'chat': 2, 'vache': 1}

sys.argv
--------

- hello(things=sys.argv)

fichiers
--------

- animal_count_from_file(fn) => {'dodo': 1, 'dragon': 1}

dates
-----

- le jour J du mois M est le combientième jour de l'année A
- le premier samedi du mois M de l'année A
- quel jour J est l'avant-dernier jeudi du mois M
- combien de jours reste-t-il jusqu'à mon prochain anniversaire

algorithmes
-----------

- sorting

9. Questions pièges
===================

- id(1) != id('1')
- [] += 1 vs .append()
- http://docs.python-guide.org/en/latest/writing/gotchas

10. References
=============

- pydev
- docs.python.org
- wikipedia
- http://stackoverflow.com
- https://fr.wikipedia.org/wiki/Python_(langage)
- scipy.org
