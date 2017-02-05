# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 22:08:19 2017

@author: joe27
"""

i = 0
inText = input("Ваш текст: ")
splitText = inText.split()
print("Итоговая строка: ")
while i < len(splitText):
    s = splitText[i]
    if s[0].isupper() == True:
        splitText[i] = splitText[i].upper()
    print(splitText[i], " ", sep='', end='', flush=True),
    i+=1
    