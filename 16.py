# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:21:35 2017

@author: joe27
"""

import random
import datetime

comand = ['Shachtar', 'Barselona', 'Spartak', 'Manchester',
        'Zarya', 'Bavaria', 'Liverpool', 'Roma',
        'Milan', 'Sevilia', 'Dnepr', 'Real',
        'Arsenal', 'Borusia', 'Rubin', 'CSK']

random.shuffle(comand)

nDate = datetime.datetime.now()
nDate = nDate.replace(2017, 9, 14)

first_date = datetime.datetime(2017, 9, 20)
end_date = datetime.timedelta(days=14)
i = j = 0
print('Календарь:')
while first_date <= datetime.datetime(2018, 5, 2):
    first_date += end_date
    if j < len(comand):
        print(j+1, ". ", str(comand[i]), ' - ', str(comand[j-1])," [", first_date.day, '.', first_date.month, '.', first_date.year, ', 22:45 ]', " ", sep='', flush=True)
        i += 1
        j += 1
