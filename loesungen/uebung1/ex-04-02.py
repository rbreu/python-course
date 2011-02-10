#!/usr/bin/env python

summe = 0

for i in range(10):
    zahl = float(raw_input("Gib eine Zahl ein / Enter a number: "))
    if zahl >= 0:
        summe += zahl
    if summe > 42:
        break  # for-Schleife verlassen / leave the for loop

print "Die Summe ist / The sum is:", summe

