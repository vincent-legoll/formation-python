# Plan de la formation

## Généralités

- Prise en main des notebooks **[MB: OK]**
- Généralités sur le langage Python
	- La programmation, qu'est-ce que c'est ? **[VL: OK]**
	- Le langage Python **[MB: OK]**
	- Historique **[VL: OK]**
	- Philosophie -> à déplacer ?
	- Qu'est-ce qu'un langage interprété ? **[VL: OK]**
	- Quelques interpréteurs Python **[VL: OK]**
	- Exécution d'un programme Python
		- console Python **[MB: OK]**
		- console système **[MB: OK]**
		- console iPython **[MB: OK]**
		- IDEs pour Python **[MB: OK]**
	- Applications
	- Intérêt scientifique/package **[MB]**
	- Documentation **[VL: OK]**


> Notebook : [00-InitPython-generalites.ipynb] (ce notebook)

## Le langage [1/2]

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
il y a un truc bizarre dans le commentaire final

> Notebook : [[01-InitPython-langage-1.ipynb]](http://localhost:8888/notebooks/01-InitPython-langage-1.ipynb)

## Le langage [2/2]

### Opérateurs

- bit à bit 
- arithmétiques **[MB: OK]**
- logiques **[MB: OK]**
- comparaison **[VL]**
- assignation **[VL]**
- Compatibilité de type, coercition de type **[MB]**
- priorité des opérateurs **[VL]**


### Strutures de contrôle

- mise en page **[VL: OK]**
- pass **[VL: OK]**
- tests: if / elif / else **[MB: OK]**
- boucles **[VL: OK]**
	* for elt in liste
	* for idx in range(len(liste))
	* while
	* break
	* continue

### Fonctions
  * avec/sans return **[MB: OK]**
  * avec/sans arguments **[MB: OK]**
  * valeurs par defaut **[MB: OK]**
  * arguments (*args, **kwargs) **[MB: OK]**
  * Espace de nommage, portée des variables **[MB: OK]**
  * fonctions built-in **[MB]**
  * lambda **[VL]**
  * compréhensions de listes **[MB]**

### Erreurs et exceptions
- try/catch **[VL]**
- ``with``


- surcharge d'opérateurs

### Classes

### Modules

> Notebook : [[01-InitPython-langage-2.ipynb]](http://localhost:8888/notebooks/01-InitPython-langage-2.ipynb)

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
	
D'autres exemples de conversion avec

	jupyter-nbconvert -h
    
## Liens utiles

- [Doc Markdown](https://guides.github.com/features/mastering-markdown)
