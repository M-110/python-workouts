"""
Create your own MyEnumerate class, such that someone can use it instead of 
enumerate. It will need to return a tuple with each iteration, with the first 
element in the tuple being the index (starting with 0) and the second element 
being the current element from the underlying data structure. Trying to use 
MyEnumerate with a noniterable argument will result in an error.
"""

class MyEnumerate:
    def __init__(self, data):
        self.data = data
        self.index = 0
        
    def __iter__(self):
        return MyEnumerate(self.data)
    
    def __next__(self):
        i = self.index
        self.index+=1
        try:
            return (i, self.data[i])
        except IndexError:
            raise StopIteration
    
dog = MyEnumerate('abc')

for i, c in dog:
    print(f'{i}: {c!r}')
for i, c in dog:
    print(f'{i}: {c!r}')
    
    
        