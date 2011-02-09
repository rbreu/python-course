#!/usr/bin/env python

zahl = raw_input("Eine Zahl: ")

try:
    ergebnis = float(zahl) ** 2
except ValueError:
    print "Das ist keine Zahl."
else:
    print "Das Quadrat ist:", ergebnis
