# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 14:09:07 2017

@author: joe27
"""
import re

password = input("Введите пароль: ")
result=[]
n = 0
k = 0
if len(password) >= 6:
    n += 1
result = re.findall(r'\d', password)
if len(result) >= 1:
    n += 1
if password.islower() == False:
    n += 1
if password.isupper() == False:
    n += 1
    
for val in password:
    if 33 <= ord(val) <= 47 or 58 <= ord(val) <= 64 or 91 <= ord(val) <= 96 or 123 <= ord(val) <= 126:
        k += 1

if (k >= 1):
    n += 1

if n == 5:
    print ("Пароль надёжный!")
else:
    if n > 3:
        print ("Пароль не очень надёжный!")
    else:
        print ("Пароль не надёжный!")
        