#!/usr/bin/env python

import sys

f = open(sys.argv[1], "r")
content = f.read()
f.close()

print "Spam count:", content.count("Spam")


# Die obige Version ist genau genommen etwas unsauber, da bei Lesefehlern
# die Datei nicht wieder geschlossen wird. Das Einlesen mit korrekter
# Ausnahmebehandlung saehe so aus:
#
# The solution above is not a good one, since the file isn't closed
# properly should a read error occur. Reading with correct exception
# handling would look like this:

f = open(sys.argv[1], "r")

try:
    content = f.read()
except IOError, e:
    "Lesefehler: ", e
finally:
    f.close()


# Ab Python 2.5 geht das etwas kuerzer (Vorgriff auf naechste Vorlesung):
#
# For Python >= 2.5 the following is more comfortable (lookahead to next
# lecture):

#with open(sys.argv[1], "r") as f:
#    content = f.read()
