"""
Write a function, called how_many_different_numbers, that takes a single list 
of integers and returns the number of different integers it contains.
"""

numbers = [1, 2, 3, 1, 2, 3, 4, 1]

def how_many_different_numbers(nums):
    return len(set(nums))

assert(how_many_different_numbers(numbers) == 4)



