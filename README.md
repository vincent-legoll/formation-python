# Petite notice d'utilisation des Notebooks Python

## Installation de Jupyter

L'idéal est d'utiliser [Anaconda](http://jupyter.readthedocs.org/en/latest/install.html)
que pouvez télécharger [ici](https://www.continuum.io/downloads).
Anaconda est une suite assez complète et facile à utiliser. Outre les notebook Jupyter, Anaconda contient entre autre :

- l'IDE [Spyder](https://github.com/spyder-ide/spyder)
- les deux versions Python 2 et Python 3
- le gestionnaire de paquets Python ``conda``

Attention: certaines versions récentes d'anaconda utilisent python3 par défaut,
le code présent dans les notebook de cette formations n'est pas compatible avec python3.

Pour installer [Jupyter](https://pypi.python.org/pypi/jupyter) sur une distribution
linux qui ne le propose pas dans son gestionnaire de paquets, il faut utiliser [``pip``](https://pypi.python.org/pypi/pip) :

    sudo pip install jupyter

Pour l'IDE [Spyder](https://pypi.python.org/pypi/spyder), on peut faire de même:

    sudo pip install spyder

## Lancement d'un serveur Jupyter

- Soit via l'utilitaire ``Launcher`` d'Anaconda
- Soit en ligne de commande, par exemple depuis le répertoire de travail des notebooks avec la commande:

	jupyter-notebook

Normalement, cette commande ouvre directement une page dans le navigateur par défaut sur [http://localhost:8888/tree](http://localhost:8888/tree)

Sur cette page, il suffit de cliquer sur le nom du notebook pour l'éditer et l'exécuter.

## Commandes de conversion du notebook

En document pdf :

	jupyter-nbconvert InitiationPython.ipynb --to pdf
	
Vers le mode diaporama en l'ouvrant dans un navigateur:

	jupyter-nbconvert InitiationPython.ipynb --to slides --post serve
	
Lancer le diaporama en utilisant un port différent du port par défaut (afin d'avoir plusieurs diaporamas ouverts) :

	jupyter-nbconvert 01-InitPython-langage.ipynb --to slides --post serve --ServePostProcessor.port=8001 
	
Lancer le diaporama après avoir exécuté toutes les cellules du notebook :

	jupyter-nbconvert InitiationPython.ipynb --to slides --post serve --execute


> **Utile :** l'insertion d'un bouton de rendu "diaporama" *(live reveal)* dans l'interface d'édition du notebook en installant [RISE](https://github.com/damianavila/RISE).

Autre manière de lancer un slideshow :

	jupyter-nbconvert InitiationPython.ipynb --to slides

puis

	python -m SimpleHTTPServer 8000
	
et aller à l'url [http://localhost:8000/0InitiationPython.ipynb.slides.html#/](http://localhost:8000/0InitiationPython.ipynb.slides.html#/) dans un navigateur.

D'autres exemples de conversion avec

	jupyter-nbconvert -h
    
## Liens utiles

- [Doc Markdown](https://guides.github.com/features/mastering-markdown)
