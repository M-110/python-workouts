"""
That is, you can add as many scoops in each call to Bowl.add_scoops as you 
want, and you can call that method as many times as you want--but only the 
first three scoops will actually be added. Any additional scoops will be 
ignored.
"""

class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
        
    def __repr__(self):
        return f'Scoop({self.flavor!r})'
    
    def __str__(self):
        return self.flavor
    
        
        
class Bowl:
    max_scoops = 3
    def __init__(self):
        self.scoops = []
        
    def add_scoops(self, *scoops):
        for scoop in scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(scoop)
            
    def __repr__(self):
        return 'Bowl()'
    
    def __str__(self):
        return str(self.scoops)
    
s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')
 
b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s4, s5)
print(b)