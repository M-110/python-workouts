# -*- coding: utf-8 -*-
"""
For this exercise, first create a dict of any size, in which the keys are 
unique and the values are also unique. (A key may appear as a value, or vice 
versa.)
"""

d = {'a':1, 'b':2, 'c':3}

def flip_dict(d):
    return {value: key for key, value in d.items()}

print(flip_dict(d))