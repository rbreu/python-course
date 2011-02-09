#!/usr/bin/env python

summe = 0

for i in range(10):

    # raw_input liefert Strings.
    # Zum Rechnen muessen wir das in ein Float konvertieren:
    zahl = float(raw_input("Gib eine Zahl ein: "))
    summe += zahl

print "Die Summe ist:", summe
