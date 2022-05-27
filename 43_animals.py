"""
For the purposes of these exercises, you are the director of IT at a zoo. 
The zoo contains several different kinds of animals, and for budget reasons, 
some of those animals have to be housed alongside other animals.

We will represent the animals as Python objects, with each species defined as 
a distinct class. All objects of a particular class will have the same species 
and number of legs, but the color will vary from one instance to another. 

"""

class Species:
    def __init__(self, species, color, legs):
        self.species =  species
        self.color = color
        self.number_of_legs = legs
        
    def __repr__(self):
        return f'Species({self.species}, {self.color!r}, {self.number_of_legs})'
    
    def __str__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'
        

class Sheep(Species):
    def __init__(self, color):
        super().__init__("sheep", color, 4)
        
        
class Wolf(Species):
    def __init__(self, color):
        super().__init__("wolf", color, 4)
        
        
class Snake(Species):
    def __init__(self, color):
        super().__init__("snake", color, 0)
        
        
class Parrot(Species):
    def __init__(self, color):
        super().__init__("parrot", color, 2)
        
        
s = Sheep('White')
w = Wolf('Grey')
n = Snake('Black')
p = Parrot('Orange')

print(s)
print(w)
print(n)
print(p)
        
