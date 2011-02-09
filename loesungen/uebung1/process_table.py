#!/usr/bin/env python

import sys

infile = open("table_data.txt", "r")
outfile = open("table_data_out.txt", "w")

# Wir koennen direkt ueber Fileobjekte iterieren und erhalten die
# einzelnen Zeilen:
for zeile in infile:
    zahlen = zeile.strip().split(":")

    # Mit strip werden wir Zeilenubrueche und Leerzeichen am Anfang und
    # Ende der Zeile los.

    # split trennt die Zeile am Doppelpunkt und liefert eine Liste von
    # Strings zurueck, welche keinen Doppelpunkt mehr enthalten.

    summe = 0.0
    for zahl in zahlen:
        summe += float(zahl)

    #Profi-Variante zum Berechnen der Summe (Vorgriff auf naechste Vorlesung):
    #summe = map(float, zahlen).sum()

    zahlen.append(str(summe))
    outfile.write(":".join(zahlen) + "\n")

    # join macht das Umgekehrte wie split: Eine Liste von Strings wird
    # zu einem String zusammengefuegt mit dem Trennzeichen :

    # Nicht vergessen, den Zeilenumbruch anzuhaengen! Das "\n" wandelt
    # Python automatisch in den Zeilenumbruch um, den das Betriebssystem
    # benutzt ("\n", "\r", "\r\n", ...)


infile.close()
outfile.close()


# Auch hier gilt: Die obige Version ist etwas unsauber, da bei Lesefehlern,
# Programmierfehlern etc. die Dateien nicht wieder geschlossen werden.
# Korrekterweise die gesamte for-Schleife in einen try-except-Block
# einschliessen:
#
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
