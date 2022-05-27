"""
In this exercise, write a generator function whose argument must be iterable. 
With each iteration, the generator will return a two-element tuple. The first 
element in the tuple will be an integer indicating how many seconds have 
passed since the previous iteration. The tuple’s second element will be the 
next item from the passed argument.
"""

from time import perf_counter, sleep


def elapsed_since(x):
    prev_time = perf_counter()
    for element in x:
        delta = perf_counter() - prev_time
        prev_time = perf_counter()
        yield (round(delta,3), element)
    
        
a = elapsed_since('abc')

print(next(a))
sleep(1)
print(next(a))
sleep(1)
print(next(a))

            