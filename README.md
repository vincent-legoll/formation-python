# Questions à discuter :

- Qu'est-ce qui manque ?
- Mise en forme des slides (rappel du titre comme le fait MB : à virer ?)
- Procédure pour extraire les fichiers à distribuer à partir du dernier commit

# Plan de la formation

## Généralités

> Notebook : [00-InitPython-generalites.ipynb] (ce notebook)

- Prise en main des notebooks **[MB: OK]**
- Généralités sur le langage Python
	- La programmation, qu'est-ce que c'est ? **[VL: OK]**
	- Le langage Python **[MB: OK]**
	- Historique **[VL: OK]**
	- Philosophie déplacée **[VL: OK]**
	- Qu'est-ce qu'un langage interprété ? **[VL: OK][MB: OK]**
	- Quelques interpréteurs Python **[VL: OK][MB: OK]**
	- Exécution d'un programme Python
		- console Python **[MB: OK]**
		- console système **[MB: OK]**
		- console iPython **[MB: OK]**
		- IDEs pour Python **[MB: OK]**
	- Applications **[MB: OK]**
	- Intérêt scientifique/package **[MB: OK]**
	- Documentation **[VL: OK][MB: OK]**

## Le langage [1/2]

> Notebook : [[01-InitPython-langage.ipynb]](http://localhost:8888/notebooks/01-InitPython-langage.ipynb)

### Variables **[VL: OK]**
### Python 2/Python 3 **[VL: OK]**
### Types de données
- Types de base
	- None **[VL: OK]**
	- Booléens **[MB: OK]**
	- Numériques **[MB: OK]**
		- entiers
		- flottants
		- complexes	
- Séquences
	- Chaines de caractères **[VL]**
	- listes ``list()`` **[MB: OK]**
	- tuples ``tuple()`` **[MB: OK]**
- Conteneurs
	- Dictionnaires ``dict()`` **[VL: OK]**
	- Ensembles ``set()`` **[VL: OK]**
	- Littéraux ``{}``, méthodes ``dict()``, etc... **[VL: OK]**
	
### Fichiers **[MB: OK]**

## Le langage [2/2]

> Notebook : [[02-InitPython-langage.ipynb]](http://localhost:8888/notebooks/02-InitPython-langage.ipynb)

### Opérateurs

- bit à bit 
- arithmétiques **[MB: OK]**
- logiques **[MB: OK]**
- comparaison **[VL: OK]**
- assignation **[VL: OK]**
- Compatibilité de type, coercition de type **[MB]** **[VL: OK]**
- priorité des opérateurs **[VL: OK]**


### Strutures de contrôle

- mise en page **[VL: OK]**
- pass **[VL: OK]**
- tests: if / elif / else **[MB: OK]**
- boucles **[VL: OK]**
	* for elt in liste **[VL: OK]**
	* for idx in range(len(liste)) **[VL: OK]**
	* while **[VL: OK]**
	* break **[VL: OK]**
	* continue **[VL: OK]**

### Fonctions
  * avec/sans return **[MB: OK]**
  * avec/sans arguments **[MB: OK]**
  * valeurs par defaut **[MB: OK]**
  * arguments (*args, **kwargs) **[MB: OK]**
  * Espace de nommage, portée des variables **[MB: OK]**
  * fonctions built-in **[MB]**
  * lambda **[VL]**
  * compréhensions de listes **[MB]**

### Erreurs et exceptions **[VL: OK]**
- try/catch **[VL: OK]**
- ``with`` **[VL: OK]**


- surcharge d'opérateurs

### Classes

### Modules


## Micro-projet

> Notebook : [02-InitPython-microprojet.ipynb]

## Conclusion

- zen de Python


# Petite notice d'utilisation des Notebooks Python


## Installation de Jupyter

L'idéal est d'utiliser [Anaconda](http://jupyter.readthedocs.org/en/latest/install.html)

## Lancement d'un serveur Jupyter

Par exemple depuis le répertoire de travail des notebooks avec la commande:

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
