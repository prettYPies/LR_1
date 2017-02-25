# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:59:41 2017

@author: joe27
"""
import copy

def extra_enumerate(l):
    s = 0
    i = 0
    x = copy.deepcopy(l)
    for ex in l:
        s = s + ex        
        x[i] = s
        i+=1
    s = sum(l)
    fL = copy.deepcopy(x)
    i = 0
    for ex in fL:
        fL[i] = round(ex / s,1)
        i = i+1   
    return zip(l,l,x,fL)
    

x = [1,3,4,2]
for i, elem, cum, frac in extra_enumerate(x):
    print("(", elem, ",", cum,",",frac,")" " ", sep='', end='', flush=True)