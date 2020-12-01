from Point import Point
from math import *
PI = 3.14159
class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):        # "Circle(x, y, radius)"
        return "Circle({1}, {2}, {3})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Nie można porównać okręgu z czymś innym niż okrąg")
        else:
            return self.pt.x == other.pt.x and self.pt.y == other.pt.y and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self): return PI * self.radius * self.radius
           # pole powierzchni

    def move(self, x, y):    # przesuniecie o (x, y)
        self.pt.x += x
        self.pt.y += y
        return Circle(self.pt.x, self.pt.y, self.radius)

    def cover(self, other): # najmniejszy okrąg pokrywający oba
        if type(other) != Circle:
            raise ValueError("Podaj wartość o typie: Circle")
        else:
            covering_circle = self if self.radius > other.radius else other
            center_x = (self.pt.x + other.pt.x) // 2
            center_y = (self.pt.y + other.pt.y) // 2
            equation = round(
            sqrt(pow(covering_circle.pt.x - center_x, 2) + pow(covering_circle.pt.y - center_y, 2)), 2)
            
            covering_circle.pt = Point(center_x, center_y)
            covering_circle.radius += equation
            return covering_circle
