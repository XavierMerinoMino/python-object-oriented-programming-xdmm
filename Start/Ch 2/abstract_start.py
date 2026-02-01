# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints

# abc: provides the infrastructure for defining Abstract Base Classes (ABCs)
# ABC: A helper base class used to declare a class as an abstract base class. 
# Inheriting from this class is the modern and simplest way to create an ABC.
# abstractmethod: decorator used within an ABC to mark methods that must be 
# implemented by any concrete subclass.
from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

    @abstractmethod
    def calcPerimeter(self):
        pass

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    
    def calcPerimeter(self):
        return 2 * 3.14 * self.radius

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side
    
    def calcPerimeter(self):
        return self.side * 4

# g = GraphicShape()

c = Circle(10)
print(f"Perimeter: {c.calcPerimeter():.4f}")
print(f"Area: {c.calcArea():.4f}")
# print(c.calcArea())
s = Square(12)
# print(s.calcArea())
print(f"Perimeter: {s.calcPerimeter()}")
print(f"Area: {s.calcArea():.4f}")
