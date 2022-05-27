"""
In this exercise, we’ll practice doing such unraveling. Write a function that 
takes a list of lists (just one element deep) and returns a flat, 
one-dimensional version of the list.
"""

def flatten(lst):
    return [item for sub_lst in lst for item in sub_lst]

print(flatten([[1,2],[3,4]]))

