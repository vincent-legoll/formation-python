# -*- coding: utf-8 -*-

def ttc(liste):
    return sum(liste) * 1.2

liste_prix_ht = [12, 56.20, 19.99, 0.40, 100]
print "%.02f" % ttc(liste_prix_ht)
