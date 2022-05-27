"""
For this exercise, write a function (join_numbers) that takes a range of 
integers. The function should return those numbers as a string, with commas 
between the numbers. That is, given range(15) as input, the function should 
return this string: "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14"
"""

def join_numbers(num_range):
    return ','.join(str(num) for num in num_range)

print(join_numbers(range(15)))
