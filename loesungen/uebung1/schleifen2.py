#!/usr/bin/env python

summe = 0

for i in range(10):
    zahl = float(raw_input("Gib eine Zahl ein: "))
    if zahl >= 0:
        summe += zahl
    if summe > 42:
        break  # for-Schleife verlassen

print "Die Summe ist:", summe

