# -*- coding: utf-8 -*-
"""
Specifically, write a new module called “menu” (in the file menu.py). The 
module should define a function, also called menu. The function takes any 
number of key-value pairs as arguments. Each value should be a callable, a 
fancy name for a function or class in Python.

When the function is invoked, the user is asked to enter some input. If the 
user enters a string that matches one of the keyword arguments, the function 
associated with that keyword will be invoked, and its return value will be 
returned to menu’s caller. If the user enters a string that’s not one of the 
keyword arguments, they’ll be given an error message and asked to try again.
"""


def menu(**funcs):
    while (user_input := input('>>')) not in funcs:
        print(f'Error! Functions avaliable: {", ".join(funcs.keys())}')
    print(f'Result is: {funcs[user_input]()!r}')


def func_a():
    return 'This was the a function'


def func_b():
    return 'This was the b function'

    
menu(a=func_a, b=func_b)
