"""
In this exercise, we’re going to see a small-scale version of that. In the 
previous exercise, we created a Scoop class that represents one scoop of ice 
cream. If we’re really going to model the real world, though, we should have 
another object into which we can put the scoops. I thus want you to create a 
Bowl class, representing a bowl into which we can put our ice cream.
"""

class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
        
    def __repr__(self):
        return f'Scoop({self.flavor!r})'
    
    def __str__(self):
        return self.flavor
    
        
        
class Bowl:
    def __init__(self):
        self.scoops = []
        
    def add_scoops(self, *scoops):
        for scoop in scoops:
            self.scoops.append(scoop)
            
    def __repr__(self):
        return 'Bowl()'
    
    def __str__(self):
        return str(self.scoops)
            
s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
 
b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b)