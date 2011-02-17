#!/usr/bin/env python

mysum = 0

while True:
    # Achtung, hier noch nicht in ein Float umwandeln,
    # da der Benutzer "ende" eingeben darf:
    number = raw_input("Gibt eine Zahl ein / Enter a number: ")
    if number == "quit":
        break
    
    mysum += float(number)

print "Die Summe ist / The sum is:", mysum
