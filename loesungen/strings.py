#!/usr/bin/env python

vorname = raw_input("Dein Vorname? ")
nachname = raw_input("Dein Nachname? ")

print "Langes Leben und Friede", vorname, nachname

print vorname[1:5], nachname[-2]
print vorname.upper(), nachname.upper()
print "Name endet mit mann?", nachname.endswith("mann")
print vorname.swapcase()
print "Anzahl der 'e's:", (nachname+vorname).count("e")
