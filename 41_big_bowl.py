"""
Implement BigBowl for this exercise, such that the only difference between it 
and the Bowl class we created earlier is that it can have five scoops, rather 
than three. And yes, this means that you should use inheritance to achieve 
this goal.
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
    
class BigBowl(Bowl):
    max_scoops = 5
    
s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')
 
bb = BigBowl()
bb.add_scoops(s1, s2)
bb.add_scoops(s3)
bb.add_scoops(s4, s5)
print(bb)
    