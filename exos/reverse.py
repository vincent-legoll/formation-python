# -*- coding: utf-8 -*-

L = "Dans le Python, tout est bon.".split()

# La solution simple et élégante :
print L[::-1]

# Explications:
# Pas de bornes => valeurs par défaut => on prend tout
# Le pas est de -1 => à l'envers

# La version explicite :
print L[-1:-len(l)-1:-1]

# Explications:
# On commence à la dernière place
# On s'arrête à la première, exprimée en indices négatifs
# Le pas est de -1 => à l'envers
