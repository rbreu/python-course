#!/usr/bin/env python

import sys

with open("ex-15-in.txt", "r") as infile:
    with open("ex-15-out.txt", "w") as outfile:

        # Wir koennen direkt ueber Fileobjekte iterieren und erhalten
        # die einzelnen Zeilen:
        #
        # We can directly iterate over file objects and get the lines:
        for line in infile:
            numbers = line.strip().split(":")

            # Mit strip werden wir Zeilenubrueche und Leerzeichen am
            # Anfang und Ende der Zeile los.  split trennt die Zeile
            # am Doppelpunkt und liefert eine Liste von Strings
            # zurueck, welche keinen Doppelpunkt mehr enthalten.
            #
            # With strip we get rid of line breaks and spaces at the
            # beginning and end of a line.  split divides the line at
            # the colon and returns a list of strings which don't
            # contain a colon.

            linesum = 0.0
            for number in numbers:
                linesum += float(number)

            # Profi-Variante zum Berechnen der Summe (Vorgriff auf
            # naechste Vorlesung):
            #
            # Expert variant to calculate the sum (lookahead to next
            # lecture):
                
            # linesum = map(float, numbers).sum()
    
            numbers.append(str(linesum))
            outfile.write(":".join(numbers) + "\n")

            # join macht das Umgekehrte wie split: Eine Liste von
            # Strings wird zu einem String zusammengefuegt mit dem
            # Trennzeichen : Nicht vergessen, den Zeilenumbruch
            # anzuhaengen! Das "\n" wandelt Python automatisch in den
            # Zeilenumbruch um, den das Betriebssystem benutzt ("\n",
            # "\r", "\r\n", ...)
            #
            # join is the reverse to split: a list of strings gets
            # concatenated with a colon inbetween.  Don't forget to
            # add the line break! The "\n" gets automatically conveted
            # to the correct line break for the operatin system ("\n",
            # "\r", "\r\n", ...)


