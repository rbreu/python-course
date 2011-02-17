#!/usr/bin/env python

mysum = 0

for i in range(10):

    # raw_input liefert Strings.
    # Zum Rechnen muessen wir das in ein Float konvertieren:
    #
    # raw_input returns strings
    # to do arithmetics we have to convert those into floats:
    number = float(raw_input("Gib eine Zahl ein / Enter a number: "))
    mysum += number

print "Die Summe ist / The sum is:", mysum
