"""
Define a class, Circle, that takes two arguments when defined: a sequence and
a number. The idea is that the object will then return elements the defined 
number of times. If the number is greater than the number of elements, then 
the sequence repeats as necessary. You should define the class such that it 
uses a helper (which I call CircleIterator).
"""


class Circle:
    def __init__(self, seq, num):
        self.seq = seq
        self.num = num
        
    def __iter__(self):
        return CircleIterator(self.seq, self.num)
    
    
class CircleIterator:
    def __init__(self, seq, num):
        self.seq = seq
        self.num = num
        self.count = 0
        
    def __next__(self):
        if self.count >= self.num:
            raise StopIteration
            
        value = self.seq[self.count % len(self.seq)]
        self.count += 1
        return value
    
c = Circle('abc', 5)
print(list(c))   
