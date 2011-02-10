#!/usr/bin/env python

# raw_input liest Strings von Tastatur ein:
#
# raw_input reads strings from keyboard input:
vorname = raw_input("Dein Vorname? / Your given name?")
nachname = raw_input("Dein Nachname? / Your family name?")

print "Langes Leben und Friede / Live long and prosper", vorname, nachname

# : gibt ein Intervall an, negative Indizes zaehlen vom Ende des Strings:
#
# : denotes an interval, negative indices count from the end of the string:
print vorname[1:5], nachname[-2]

# Einige Mothoden auf Strings:
#
# Some string methods:
print vorname.upper(), nachname.upper()
print "Name endet mit mann? / Name ends with mann?", nachname.endswith("mann")
print vorname.swapcase()

# Zwei Strings koennen mit + aneinander gehaengt werden
# Das liefert einen neuen String, auf dem wie die count-Methode aufrufen:
#
# Two strings can be concatenated with +
# This yields a new string, on which we can call the count method:
print "Anzahl der 'e's / Number of 'e's:", (nachname+vorname).count("e")
