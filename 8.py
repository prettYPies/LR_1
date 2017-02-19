# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 13:08:41 2017

@author: joe27
"""
import random

s = 0
n = random.randint(1, 10000)
print("Количество элементов массива: ", n)
A = [random.randrange(20, 100) for i in range(n)] 
for x in range(1,14):
    if n >= 2**x:
        s = abs(2**(x+1) - n)
    else:
        print("Ближайшая степень двойки: ", 2**x, "\nНе хватает элементов: ", s)
        break
A.append([0] * s)
print(A)