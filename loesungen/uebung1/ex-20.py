#!/usr/bin/env python

from random import randint

# Programmeinstellungen, die konstant bleiben, gerne als globale
# Variablen am Anfgan der Datei definieren. Durch Grossschreibung
# als Konstanten kennzeichnen.
#
# Program configurations that remain constant preferably as global
# variables at top of the file. Mark as constatn by using ALL CAPITALS.

HIGHSCORE = "ex-20-highscore.txttt"


# Laengere Programme in sinnvolle Funktionen gliedern!
#
# Break longer programs into functions!

def zahlenraten():
    """
    Ein Spieldurchlauf Zahlenraten.

    Es wird eine Zufallszahl generiert und der Benutzer solange gefragt,
    bis er die Zahl geraten hat.

    Gibt die Anzahl der benoetigten Versuche zurueck.


    One round of high/low.

    Generates a random number and ask the user until they guess the
    number.

    Returns the number of guesses.
    """
    
    zahl = randint(1, 100)
    versuche = 1

    while True:
        try:
            eingabe = int(raw_input("Rate eine Zahl / Guess a number: "))
        except ValueError:
            print "Das ist keine Zahl. / That's not a number."
            continue
        if eingabe == zahl:
            print "Richtig/Correct! Du hast %i Versuche gebraucht." % versuche
            return versuche
        elif eingabe > zahl:
            print "Zu gross. / Too high."
        else:
            print "Zu klein. / Too low."

        versuche += 1


def highscore_speichern(versuche, name):
    """
    Fuege einen Eintrag zur Highscore-Liste hinzu.

    Append an entry to the high score list.
    """

    # Den alten Highscore als Liste einlesen:
    #
    # Read the old high score list:
    
    f = open(HIGHSCORE)

    try:
        highscore = f.readlines()
    except IOError:
        print "Could not read highscore, start new one."
        highscore = []
    finally:
        f.close()

    # Den neuen Eintrag hinzufuegen und die besten zehn
    # Eintraege abspeichern:
    #
    # Add the new entry and save the ten best entries:
        
    highscore.append("%i\t%s\n" % (versuche, name))
    highscore.sort()
    highscore = highscore[:10]

    f = open(HIGHSCORE, "w")
    try:
        f.writelines(highscore)
    except IOError, e:
        print "Could not save highscore:", e
    finally:
        f.close()


def highscore_ausgeben():
    """
    Gib Highscore aus.

    Print highscore to stdout.
    """

    print
    print "H I G H S C O R E"

    f = open(HIGHSCORE)
    try:
        print f.read()
    except IOError, e:
        "Could not read highscore:", e
    finally:
        f.close()

    print
    

if __name__ == "__main__":
    # Hauptschleife:
    #
    # Main loop:
    
    while True:
        name = raw_input("Dein Name / Your name: ")
        versuche = zahlenraten()
        highscore_speichern(versuche, name)
        highscore_ausgeben()
        weiter = raw_input("Weiter spielen / Another game? (y/n) ")
        if weiter.lower().startswith("n"):
            break 

        # Bei gut gewahlten Funktionen und Funktionsnamen liest sich
        # das fast wie Prosa. ;-)
        #
        # If you choose your functions and function names wisely,
        # this almost reads like prose. ;-)
