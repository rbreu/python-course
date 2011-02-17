#!/usr/bin/env python

def nothing():
    print "Ich gebe nichts zurueck. / I don't return anything."

a = nothing()
print a

# Funktionen ohne return geben automatisch None zurueck. Das ist ein Objekt
# wie jedes andere auch, daher kann man es Variablen zuweisen und ausgeben
# lassen.
#
# Functions without return automatically return None. That is an ordinary
# Python object, thus we can assign and display it like any other object.
