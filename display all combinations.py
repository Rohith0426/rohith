# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:53:50 2020

@author: rohith
"""
import itertools      
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))