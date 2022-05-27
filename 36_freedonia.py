# -*- coding: utf-8 -*-
"""
Your job is to implement that Python module, freedonia.py. It should provide a 
function, calculate_tax, that takes three arguments: the amount of the 
purchase, the province in which the purchase took place, and the hour 
(an integer, from 0-24) at which it happened. The calculate_tax function 
should return the final price, as a float.
"""

TAX_DICT = {'Chico': .50,
            'Groucho': .70,
            'Harpo': .50,
            'Zeppo': .40}

def calculate_tax(price, province, hour):
    return TAX_DICT[province] * (hour / 24) * price

print(calculate_tax(500, 'Harpo', 12))



