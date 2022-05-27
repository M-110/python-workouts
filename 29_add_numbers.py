"""
In the previous exercise, we took a sequence of numbers and turned it into a 
sequence of strings. This time, we’ll do the opposite--take a sequence of 
strings, turn them into numbers, and then sum them. But we’re going to make it 
a bit more complicated, because we’re going to filter out those strings that 
can’t be turned into integers.
"""

def sum_numbers(num_string):
    return sum(int(num) for num in num_string.split() if num.isdigit())

print(sum_numbers("10 abc 20 de44 30 55fg 40"))

