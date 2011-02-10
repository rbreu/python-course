#!/usr/bin/env python

import sys

infile = open("ex-15-in.txt", "r")
outfile = open("ex-15-out.txt", "w")

# Wir koennen direkt ueber Fileobjekte iterieren und erhalten die
# einzelnen Zeilen:
#
# We can directly iterate over file objects and get the lines:
for zeile in infile:
    zahlen = zeile.strip().split(":")

    # Mit strip werden wir Zeilenubrueche und Leerzeichen am Anfang und
    # Ende der Zeile los.
    # split trennt die Zeile am Doppelpunkt und liefert eine Liste von
    # Strings zurueck, welche keinen Doppelpunkt mehr enthalten.
    #
    # With strip we get rid of line breaks and spaces at the beginning
    # and end of a line.
    # split divides the line at the colon and returns a list of strings
    # which don't contain a colon.

    summe = 0.0
    for zahl in zahlen:
        summe += float(zahl)

    # Profi-Variante zum Berechnen der Summe (Vorgriff auf naechste Vorlesung):
    #
    # Expert variant to calculate the sum (lookahead to next lecture):

    # summe = map(float, zahlen).sum()
    
    zahlen.append(str(summe))
    outfile.write(":".join(zahlen) + "\n")

    # join macht das Umgekehrte wie split: Eine Liste von Strings wird
    # zu einem String zusammengefuegt mit dem Trennzeichen :
    # Nicht vergessen, den Zeilenumbruch anzuhaengen! Das "\n" wandelt
    # Python automatisch in den Zeilenumbruch um, den das Betriebssystem
    # benutzt ("\n", "\r", "\r\n", ...)
    #
    # join is the reverse to split: a list of strings gets concatenated
    # with a colon inbetween.
    # Don't forget to add the line break! The "\n" gets automatically
    # conveted to the correct line break for the operatin system
    # ("\n", "\r", "\r\n", ...)


infile.close()
outfile.close()


# Auch hier gilt: Die obige Version ist etwas unsauber, da bei Lesefehlern,
# Programmierfehlern etc. die Dateien nicht wieder geschlossen werden.
# Korrekterweise die gesamte for-Schleife in einen try-except-Block
# einschliessen:
#
# And again: The above solution is not quite correct, since the files
# aren't closed properly should read errors or programming erros occur.
# For a proper solution, include the whole for loop in a try-except block:

# try:
#     for ...
#
# except IOError, e:
#     print "Lese- oder Schreibfehler", e
# except ValueError, e:
#     print "Falsche Daten in der Eingabedatei"
# finally:
#     infile.close()
#     outfile.close()
