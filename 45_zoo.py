"""
Finally, the time has come to create our Zoo object. It will contain cage 
objects, and they in turn will contain animals. Our Zoo class will need to 
support the following operations:

Given a zoo z, we should be able to print all of the cages 
(with their ID numbers) and the animals inside simply by invoking print(z).

We should be able to get the animals with a particular color by invoking 
the method z.animals_by_color. For example, we can get all of the black 
animals by invoking z.animals_by_color('black'). The result should be a list 
of Animal objects.

We should be able to get the animals with a particular number of legs by
 invoking the method z.animals_by_legs. For example, we can get all of the 
 four-legged animals by invoking z.animals_by_legs(4). The result should be a 
 list of Animal objects.

Finally, we have a potential donor to our zoo who wants to provide socks for
 all of the animals. Thus, we need to be able to invoke z.number_of_legs() and
 get a count of the total number of legs for all animals in our zoo.
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
    
    
class Zoo:
    def __init__(self):
        self.cages = []
        
    def __repr__(self):
        text = []
        for cage in self.cages:
            text.append(f'Cage #{cage.cage_id}:')
            for animal in cage.caged_animals:
                text.append('\t' + str(animal))
        return '\n'.join(text)
        
        
        
    def add_cages(self, *cages):
        self.cages += cages
        
    def animals_by_color(self, color):
        return [animal for cage in self.cages for animal in cage.caged_animals 
                   if animal.color == color]   
    
    def animals_by_legs(self, legs):
        return [animal for cage in self.cages for animal in cage.caged_animals 
                   if animal.number_of_legs == legs]  
    
    def number_of_legs(self):
        return sum(animal.number_of_legs for cage in self.cages 
                   for animal in cage.caged_animals)
    
    
    
        
        
s = Sheep('White')
w = Wolf('Grey')
n = Snake('Black')
p = Parrot('Orange')
p2 = Parrot('Brown')
n2 = Snake('Purple')
w2 = Wolf('White')
w3 = Wolf('Purple')
p3 = Parrot('Purple')

cage_1 = Cage(1)
cage_2 = Cage(2)
cage_3 = Cage(3)

cage_1.add_animals(s, w)
cage_2.add_animals(n, n2, p, p2)
cage_2.add_animals(w)
cage_3.add_animals(w2, w3, p3)

z = Zoo()
z.add_cages(cage_1, cage_2, cage_3)

print(z)
print(z.animals_by_color('Purple'))
print(z.animals_by_legs(4))
print(z.number_of_legs())


