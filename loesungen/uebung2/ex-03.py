#!/usr/bin/env python

from math import sqrt

class Punkt(object):
    """
    Ein Punkt in einem zweidimensionen Raum.
    Darstellung der Koordinaten in karthesischen Koordinaten (x, y).

    A point in two-dimensional space.
    Notation of the coordinates in Carthesian coordinates (x, y).
    """

    def __init__(self, x, y):
        """
        x, y: Karthesische Koordinaten.

        x, y: Carthesian coordinates.
        """
        
        self.x = x
        self.y = y

    def __str__(self):
        # Verhalten bei print, str(...)
        #
        # Behaviour during print, str(...)
        return "(%f, %f)" % (self.x, self.y)

    def __eq__(self, other):
        # Verhalten bei ==
        #
        # Behaviour during ==
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other):
        # Verhalten bei +
        #
        # Behaviour during +
        return Punkt(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        # Verhalten bei *
        #
        # Behaviour during *
        return self.x * other.x + self.y * other.y

    # Merke: Methoden __xxx__ bestimmen das Verhalten von Objekten
    # bei Standard-Operationen.
    #
    # Note: methods __xxx__ determin the object's behaviour during
    # basic operations.

    def norm(self):
        """Gibt die euklidische Norm zurueck."""
        return sqrt(self * self)


if __name__ == "__main__":
    p1 = Punkt(4, 2)
    p2 = Punkt(4, 2)
    p3 = Punkt(1, 2)

    print p1, p2
    print p1 == p2
    print p1 is p2  # Vergleiche Objektidentitaet / Compare object identity
    print p2 + p3
    print p2 * p3
    print p1.norm()
