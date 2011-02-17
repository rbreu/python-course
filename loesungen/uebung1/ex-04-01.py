#!/usr/bin/env python

mysum = 0

for i in range(10):
    number = float(raw_input("Gib eine Zahl ein / Enter a number: "))
    mysum += number
    if mysum > 42:
        break  # for-Schleife verlassen / leave the for loop

print "Die Summe ist / The sum is:", mysum

