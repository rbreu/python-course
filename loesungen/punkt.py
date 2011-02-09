#!/usr/bin/env python

from math import sqrt

class Punkt:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%f, %f)" % (self.x, self.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other):
        return Punkt(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def norm(self):
        return sqrt(self * self)


p1 = Punkt(4, 2)
p2 = Punkt(4, 2)
p3 = Punkt(1, 2)

print p1, p2
print p1 == p2
print p1 is p2
print p2 + p3
print p2 * p3
print p1.norm()
