#!/usr/bin/env python

summe = 0

while True:
    # Achtung, hier noch nicht in ein Float umwandeln,
    # da der Benutzer "ende" eingeben darf:
    zahl = raw_input("Gibt eine Zahl ein / Enter a number: ")
    if zahl == "ende":
        break
    
    summe += float(zahl)

print "Die Summe ist / The sum is:", summe
