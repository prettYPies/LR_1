# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 22:28:36 2017

@author: joe27
"""
link = []
link = input("Введите ссылку:").split('.')
leng = len(link)
result = []
if (link[0] == "www"):
    result.append("http://")
    result.append(link)
    if (link[leng-1] != "com"):
        result.append(".com")
print (result)

