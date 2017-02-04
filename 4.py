# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 18:23:16 2017

@author: joe27
"""
i = 0; 
inText = input("Введите текст: ")
splitText = inText.split()
print(splitText)

def sortByLength(splitText):
        return len(splitText) # Ключом является длина каждой строки, сортируем по длине  
splitText.sort(key=sortByLength, reverse=True)

while i < len(splitText):
    print(splitText[i])
    i = i + 1