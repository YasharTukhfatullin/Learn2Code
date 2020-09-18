""" 
Inheritance is basically a way to form new classes using classes that have,
already been defined.
"""

"""
Inheritance is a "is a type-of" relatinonship
"""

from abc import ABC, abstractmethod
from math import math
# has an enclosed area
# Abstract classes inherit from ABC to start


class Shape(ABC):
    @abstractclassmethod
    def get_area(self):
        pass


# has corncers (called verticics)
# has
# they are shape


class Poylygon(Shape):
    def __init__(self, sides, verticies):
        self.sides = sides  # number of the sides
        self.verticies = verticies

    def get_verticies(self):
        return self.verticies

    def get_sides(self):
        return self.sides


class Traiangle(Poylygon):
    def __init__(self, verticies):
        super().__int__(3, verticies)

    def get_area(self):
        return abs((self.verticies[0][0] * (self.verticies[1][1] - self.verticies[2][2] + self.verticies[1][0] * (self.verticies[2][1] - self.verticies[0][1] + self.verticies[2][0] * (self.verticies[0][1] - self.verticies[1][1])))/2)
