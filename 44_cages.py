"""
For this exercise, create a Cage class, into which you can put one or 
more animals
"""

class Species:
    def __init__(self, species, color, legs):
        self.species =  species
        self.color = color
        self.number_of_legs = legs
        
    def __repr__(self):
        return f'Species({self.species}, {self.color!r}, {self.number_of_legs})'
    
    def __str__(self):
        return f'{self.color} {self.species}'
        

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
        
        
class Cage:
    def __init__(self, cage_id):
        self.cage_id = cage_id
        self.caged_animals = []
    
    def add_animals(self, *animals):
        self.caged_animals += animals
        
    def __repr__(self):
        return f'Cage #{self.cage_id}: {", ".join(str(animal) for animal in self.caged_animals)}'
    
        
        
s = Sheep('White')
w = Wolf('Grey')
n = Snake('Black')
p = Parrot('Orange')
p2 = Parrot('Brown')
n2 = Snake('Purple')

cage_1 = Cage(1)
cage_2 = Cage(2)

cage_1.add_animals(s, w)
cage_2.add_animals(n, n2, p, p2)
cage_2.add_animals(w)

print(cage_1)
print(cage_2)

