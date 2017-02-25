# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 18:18:27 2017

@author: joe27
"""
def copyright(a):
    
    def _decorator(func):
        
        def _wrapper(s):
            func(s)
            for i in range(1,len(s)):
                s[i] = round(s[i] * a - s[i-1],2)
            print("\n")
            for sample in s:
                print(sample, " ", sep=' ', end='', flush=True)
            
        return _wrapper
    
    return _decorator

a = 0.97
@copyright(a)
def plot_signal(s):
    for sample in s:
        print(sample, " ", sep=' ', end='', flush=True)

    
s = [0,5,4,12,40,1,5]
plot_signal(s)