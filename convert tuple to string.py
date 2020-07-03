# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:53:50 2020

@author: rohith
"""
from collections import defaultdict, Counter
str1 = 'w3resource' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)