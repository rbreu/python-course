#!/usr/bin/env python

summe = 0

while True:
    zahl = raw_input("Gibt eine Zahl ein: ")
    if zahl == "ende":
        break
    summe += float(zahl)

print "Die Summe ist:", summe
