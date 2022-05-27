"""
Create your own implimenation of itertool's chain
"""

def my_chain(*iterables):
    return (element for iterable in iterables for element in iterable)

chain = my_chain('abc', [1,2,3], {'a':1, 'b':2})

for e in chain:
    print(e)