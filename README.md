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

	jupyter nbconvert InitiationPython.ipynb --to pdf
	
Vers le mode diaporama en l'ouvrant dans un navigateur:

	jupyter nbconvert InitiationPython.ipynb --to slides --post serve
	
> Encore mieux: l'insertion d'un bouton de rendu "diaporama" *(live reveal)* dans l'interface d'édition du notebook en installant [RISE](https://github.com/damianavila/RISE).
	
D'autres exemples de conversion avec

	jupyter nbconvert -h
    
## Liens utiles

- [Doc Markdown](https://guides.github.com/features/mastering-markdown)