# -*- coding: utf-8 -*-
"""
In this exercise, you’ll define a class, Scoop, that represents a single scoop 
of ice cream. Each scoop should have a single attribute, flavor, a string that 
you can initialize when you create the instance of Scoop.

Once your class is created, write a function (create_scoops) that creates three 
instances of the Scoop class, each of which has a different flavor 
(figure 9.1). Put these three instances into a list called scoops 
(figure 9.2). Finally, iterate over your scoops list, printing the flavor of 
each scoop of ice cream you’ve created.
"""


class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
        

class Scoops:
    def __init__(self):
        self.scoops = [Scoop('chocolate'), Scoop('vanilla'), Scoop('persimmon')]
        

scoops = Scoops()

for scoop in scoops.scoops:
    print(scoop.flavor)        