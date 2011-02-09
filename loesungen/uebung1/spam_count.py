#!/usr/bin/env python

import sys

f = open(sys.argv[1], "r")
content = f.read()
f.close()

print "Spam count:", content.count("Spam")


# Die obige Version ist genau genommen etwas unsauber, da bei Lesefehlern
# die Datei nicht wieder geschlossen wird. Das Einlesen mit korrekter
# Ausnahmebehandlung saehe so aus:

f = open(sys.argv[1], "r")

try:
    content = f.read()
except IOError, e:
    "Lesefehler: ", e
finally:
    f.close()


# Ab Python 2.5 geht das etwas kuerzer (Vorgriff auf naechste Vorlesung):

#from __future__ import with_statement
#
#with open(sys.argv[1], "r") as f:
#    content = f.read()
