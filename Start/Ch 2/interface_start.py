# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

# Interfaces are not part of Python language
# An interface is a blueprint or contract that defines a set of 
# method signatures (what a class can do) without providing any 
# implementation details (how it does it), forcing any class that 
# implements it to provide its own concrete versions of those methods

from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

# All the methods from this class must be abstract to be an interface.
class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f"{{'Circle': {str(self.calcArea())}}}"

c = Circle(10)
print(c.calcArea())
print(c.toJSON())