# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:58:44 2017

@author: joe27
"""

def frange(start, end, step):
    l = []
    k = start
    while k < end-step:
        l.append(round(k,1))
        k = k + step
    return l

for x in frange(1, 5, 0.1):
    print(x, "    ", sep='', end='', flush=True)
