#!/usr/bin/env python

number = raw_input("Eine Zahl / Some number: ")

try:
    result = float(number) ** 2
except ValueError:
    print "Das ist keine Zahl. / This is not a number."
else:
    print "Das Quadrat ist / The number squared is:", result


# Statt des else-Zweiges kann man das print natuerlich auch einfach
# so unter den try-except-Block schreiben.
#
# Instead of the else branch we could just write the print statement
# after the try-except block.
