#!/usr/bin/env python

from math import sqrt

class Punkt(object):
    """
    Ein Punkt in einem zweidimensionen Raum.
    Darstellung der Koordinaten in karthesischen Koordinaten (x, y).
    """

    def __init__(self, x, y):
        """x, y: Karthesische Koordinaten."""
        
        self.x = x
        self.y = y

    def __str__(self):
        # Verhalten bei print, str(...)
        return "(%f, %f)" % (self.x, self.y)

    def __eq__(self, other):
        # Verhalten bei ==
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other):
        # Verhalten bei +
        return Punkt(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        # Verhalten bei *
        return self.x * other.x + self.y * other.y

    # Merke: Funktionen __xxx__ bestimmen das Verhalten von Objekten
    # bei Standard-Operationen.

    def norm(self):
        """Gibt die euklidische Norm zurueck."""
        return sqrt(self * self)


if __name__ == "__main__":
    p1 = Punkt(4, 2)
    p2 = Punkt(4, 2)
    p3 = Punkt(1, 2)

    print p1, p2
    print p1 == p2
    print p1 is p2  # Vergleiche auf Objektidentitaet
    print p2 + p3
    print p2 * p3
    print p1.norm()
