# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:12:10 2017

@author: joe27
"""

def get_frames(signal, size, overlap):
    signal = [x for x in range(0, size)]
    count = int(input("Введите размер фрейма:"))
    step = count * overlap
    i = 0
    while i < len(signal):
        yield (signal[i:i + count])
        i += int(step)


signal = []
for frame in get_frames(signal, size=1024, overlap=0.7):
    print(frame)