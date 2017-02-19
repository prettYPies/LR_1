# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 22:23:32 2017

@author: joe27
"""

text = input("Введите предложение: ")

hist = {}
for symbol in text:
    hist[symbol] = hist.get(symbol, 0) + 1

print(hist)

for fkey in hist.keys():
    if (hist[fkey] == 1):
        print(fkey, " ", sep='', end='', flush=True)    