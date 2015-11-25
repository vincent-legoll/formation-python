# -*- coding: utf-8 -*-

def chevalier_ret(repetitions, cri=False):
    ret = 'ni !\n'
    if cri:
        ret = 'NI !\n'
    return ret * repetitions

print chevalier_ret(3, True)
