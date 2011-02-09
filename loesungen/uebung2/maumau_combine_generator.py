#!/usr/bin/env python

from maumau import Karte, Deck32


# Ein sehr flexibler Generator, mit dem nicht nur Kartendecks
# generiert werden koennen:
def combine(a, b, fkt=None):
    for i in a:
        for j in b:
            if fkt:
                yield fkt(i, j)
            else:
                yield (i, j)


# Ohne den dritten Parametern bekaemen wir eine Liste von Tupeln:
print list(combine(Deck32.FARBEN, Deck32.WERTE))
print

# Wir moechten aber eine Liste von Kartenobjekten. Wir geben also
# die Funktion, die mit den Tupeln als Parametern aufgerufen werden
# soll, als dritten Parameter:
print list(combine(Deck32.FARBEN, Deck32.WERTE, Karte))

# Karte ist zwar keine Funktion, aber es ist "callable", d.h.
# Karte(i, j) funktioniert.


# Eine andere Anwendung dieses Generators: Das kleine Einmaleins:
from operator import mul

for item in combine(range(1, 11), range(1, 11), mul):
    print item
