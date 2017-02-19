# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:43:49 2017

@author: joe27
"""
import sys

def inputMoney(nom, sSum):
    k = sSum // nom
    if (nom == 1000):
        s = '1000'
    if (nom == 500):
        s = '500'
    if (nom == 100):
        s = '100'
    if (nom == 50):
        s = '50'
    if (nom == 10):
        s = '10'
    if ((money[s]) - k >= 0):
        outMoney[s] = k
        sSum = sSum - k*nom
    else:
        outMoney[s] = k
        sSum = sSum - (money[s])*nom
    return sSum
    

money = {'1000': 7, '500': 9, '100': 8, '50': 7, '10': 5}
print(money)

outMoney = {}
k = 0
inSum = int(input("Введите нужную сумму: "))
if (inSum % 10 != 0):
    print("Операция не может быть выполнена!")
    sys.exit([0])
inSum = inputMoney (1000, inSum)
inSum = inputMoney (500, inSum)
inSum = inputMoney (100, inSum)
inSum = inputMoney (50, inSum)
inSum = inputMoney (10, inSum)

s = 0
if (inSum != 0):
    print ("Операция не может быть выполнена!")
    sys.exit([0])
else:
    for i in outMoney.keys():
        if outMoney[i] != 0:
            if (s == 1):
                print('+ ', i, '*', outMoney[i], " ", sep='', end='', flush=True)
            if (s == 0):
                print(i, '*', outMoney[i], " ", sep='', end='', flush=True)
                s += 1
            
        
        