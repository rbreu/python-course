#!/usr/bin/env python

zahl = raw_input("Eine Zahl: ")

try:
    ergebnis = float(zahl) ** 2
except ValueError:
    print "Das ist keine Zahl."
else:
    print "Das Quadrat ist:", ergebnis


# Statt des else-Zweiges kann man das print naturlich auch einfach
# so unter den try-except-Block schreiben.
