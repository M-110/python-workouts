"""
For this exercise, I want you to write a function (calc) that expects a single 
argument--a string containing a simple math expression in prefix 
notation--with an operator and two numbers. Your program will parse the input 
and produce the appropriate output. For our purposes, it’s enough to handle 
the six basic arithmetic operations in Python: addition, subtraction, 
multiplication, division (/), modulus (%), and exponentiation (**). The normal 
Python math rules should work, such that division always results in a 
floating-point number. We’ll assume, for our purposes, that the argument will 
only contain one of our six operators and two valid numbers.
"""

import operator

operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow,
    }

def calc(s):
    op, a, b = s.split()
    return operators[op](float(a),float(b))

print(calc('+ 5 7'))

print(calc('% 9 4'))

print(calc('** 5 2'))