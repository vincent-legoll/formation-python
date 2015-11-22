# -*- coding: utf-8 -*-

mystere = ["Gur Mra bs Clguba, ol Gvz Crgref\n\n",
           "Ornhgvshy vf orggre guna htyl.\n",
           "Rkcyvpvg vf orggre guna vzcyvpvg.\n"]

f = open('coded.txt', mode='w')
f.writelines(mystere)
f.close()
f = open('coded.txt', mode='r')
coded = f.read()
f.close()
f = open('decoded.txt', mode='w')
decoded = coded.decode('rot13')
f.write(decoded)
f.close()
