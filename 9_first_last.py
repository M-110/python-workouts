"""
Write a function, firstlast, that takes a sequence (string, list, or tuple) 
and returns the first and last elements of that sequence, in a two-element 
sequence of the same type. So firstlast('abc') will return the string ac, 
while firstlast([1,2,3,4]) will return the list [1,4].
"""

# outputs as list only

def first_last(seq):
    return [seq[0],seq[-1]]


# alternative version which preserves sequence type
    
def first_last2(seq):
    return seq[:1] + seq[-1:]

assert(first_last([1,2,3,4]) == [1,4])
assert(first_last((1,2,3,4)) == [1,4])
assert(first_last('1234') == ['1','4'])

assert(first_last2([1,2,3,4]) == [1,4])
assert(first_last2((1,2,3,4)) == (1,4))
assert(first_last2('1234') == '14')


