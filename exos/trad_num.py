# -*- coding: utf-8 -*-

trad_num = {'un': 'one', 'deux': 'two', 'trois': 'three'}
print trad_num['deux']  # On teste Fr -> En
trad_num.update({valeur: cle for cle, valeur in trad_num.items()})
print trad_num
