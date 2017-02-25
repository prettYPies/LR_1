# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 17:53:00 2017

@author: joe27
"""

def non_empty(func):
    
    def _wrapper():
        # преобразуем каждый аргумент функции к строке
        mylist = func()
        mylist = [x for x in mylist if x]
        print (mylist)
        # вызовем исходную функцию со строковыми аргументами     
    return _wrapper


# декорируем функцию
@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']

get_pages()