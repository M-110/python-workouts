"""
This challenge asks you to redefine the mysum function we defined in chapter 1, 
such that it can take any number of arguments. The arguments must all be of the 
same type and know how to respond to the + operator. (Thus, the function should 
work with numbers, strings, lists, and tuples, but not with sets and dicts.)

The result should be a new, longer sequence of the type provided by the 
parameters. Thus, the result of mysum('abc', 'def') will be the string abcdef, 
and the result of mysum([1,2,3], [4,5,6]) will be the six-element list 
[1,2,3,4,5,6]. Of course, it should also still return the integer 6 if we 
invoke mysum(1,2,3).
"""

from functools import reduce
from operator import add


def mysum(num, *nums):
    return reduce(add, num + nums)

# alternative, no imports

def mysum2(num, *nums):
    base = num[0]
    for x in (num + nums)[1:]:
        base += x
    return base


# alternative, list comprehension

def mysum3(*sequences):
    return [item for sequence in sequences for item in sequence]
