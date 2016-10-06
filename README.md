# Contenu

Ce dépôt contient le matériel utilisé dans une formation d'initiation au langage Python, en particulier quatre notebooks jupyter qui correspondent aux quatre parties du cours :

- [Les généralités](http://nbviewer.jupyter.org/github/fitzinger/formation-python/blob/master/00-InitPython-generalites.ipynb)
- [Le langage 1/2](http://nbviewer.jupyter.org/github/fitzinger/formation-python/blob/master/01-InitPython-langage.ipynb)
- [Le langage 2/2](http://nbviewer.jupyter.org/github/fitzinger/formation-python/blob/master/02-InitPython-langage.ipynb)
- [Un microprojet](http://nbviewer.jupyter.org/github/fitzinger/formation-python/blob/master/03-InitPython-microprojet.ipynb)

# Notice d'utilisation des notebooks Python

## Installation de Jupyter

L'idéal est d'utiliser [Anaconda](http://jupyter.readthedocs.org/en/latest/install.html) téléchargeable [ici](https://www.continuum.io/downloads).
Anaconda est une suite assez complète et facile à utiliser. Outre les notebooks Jupyter, Anaconda contient entre autres :

- l'IDE [Spyder](https://github.com/spyder-ide/spyder)
- les deux versions Python 2 et Python 3
- le gestionnaire de paquets Python ``conda``

> Attention: certaines versions récentes d'Anaconda utilisent python3 par défaut. Le code présent dans les notebooks de cette formation n'est pas compatible avec python3.

Pour installer [Jupyter](https://pypi.python.org/pypi/jupyter) sur une distribution
linux qui ne le propose pas dans son gestionnaire de paquets, il faut utiliser [``pip``](https://pypi.python.org/pypi/pip) :

    sudo pip install jupyter

Pour l'IDE [Spyder](https://pypi.python.org/pypi/spyder), on peut faire de même:

    sudo pip install spyder

## Lancement d'un serveur Jupyter

- Soit via l'utilitaire ``Launcher`` d'Anaconda
- Soit en ligne de commande, par exemple depuis le répertoire de travail des notebooks avec la commande:

```
jupyter-notebook
```

Normalement, cette commande ouvre directement une page dans le navigateur par défaut sur [http://localhost:8888/tree](http://localhost:8888/tree).
Sur cette page, il suffit de cliquer sur le nom du notebook pour l'éditer et l'exécuter.

## Conversion du notebook Jupyter

En document pdf :

	jupyter-nbconvert 00-InitPython-generalites.ipynb --to pdf
	
Vers le mode diaporama en l'ouvrant dans un navigateur:

	jupyter-nbconvert 00-InitPython-generalites.ipynb --to slides --post serve
	
Lancer le diaporama en utilisant un port différent du port par défaut (afin d'avoir plusieurs diaporamas ouverts) :

	jupyter-nbconvert 00-InitPython-generalites.ipynb --to slides --post serve --ServePostProcessor.port=8001 
	
Lancer le diaporama après avoir exécuté toutes les cellules du notebook :

	jupyter-nbconvert 00-InitPython-generalites.ipynb --to slides --post serve --execute


> **Utile :** Insertion d'un bouton de rendu "diaporama" *(live reveal)* dans l'interface d'édition du notebook en installant [RISE](https://github.com/damianavila/RISE).

D'autres exemples de conversion avec

	jupyter-nbconvert -h
    
## Liens utiles

- [Doc Markdown](https://guides.github.com/features/mastering-markdown)
