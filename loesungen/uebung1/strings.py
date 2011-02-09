#!/usr/bin/env python

# raw_input liest Strings von Tastatur ein:
vorname = raw_input("Dein Vorname? ")
nachname = raw_input("Dein Nachname? ")

print "Langes Leben und Friede", vorname, nachname

# : gibt ein Intervall an, negative Indizes zaehlen vom Ende des Strings:
print vorname[1:5], nachname[-2]

# Einige Mothoden auf Strings:
print vorname.upper(), nachname.upper()
print "Name endet mit mann?", nachname.endswith("mann")
print vorname.swapcase()

# Zwei Strings koennen mit + aneinander gehaengt werden
# Das liefert einen neuen String, auf dem wie die count-Methode aufrufen:
print "Anzahl der 'e's:", (nachname+vorname).count("e")
