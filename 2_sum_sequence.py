"""
The challenge here is to write a mysum function that does the same thing as 
the built-in sum function. However, instead of taking a single sequence as a 
parameter, it should take a variable number of arguments. Thus, although you 
might invoke sum([1,2,3]), you’d instead invoke mysum(1,2,3) or 
mysum(10,20,30,40,50).
"""

from functools import reduce
from operator import add


def mysum(*nums):
    total = 0
    for num in nums:
        total += num
    return total

def mysum2(*nums):
    return reduce(add, nums)


nums = [44,92,41,60,32,96,77]

assert(sum(nums) == mysum(*nums) and sum(nums) == mysum2(*nums))
