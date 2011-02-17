#!/usr/bin/env python

from random import randint

# Programmeinstellungen, die konstant bleiben, gerne als globale
# Variablen am Anfgan der Datei definieren. Durch Grossschreibung
# als Konstanten kennzeichnen.
#
# Program configurations that remain constant preferably as global
# variables at top of the file. Mark as constatn by using ALL CAPITALS.

HIGHSCORE = "ex-20-highscore.txt"


# Laengere Programme in sinnvolle Funktionen gliedern!
#
# Break longer programs into functions!

def highlow():
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
    
    number = randint(1, 100)
    tries = 1

    while True:
        try:
            user_input = int(raw_input("Rate eine Zahl / Guess a number: "))
        except ValueError:
            print "Das ist keine Zahl. / That's not a number."
            continue
        if user_input == number:
            print "Richtig/Correct! Du hast %i Versuche gebraucht." % tries
            return tries
        elif user_input > number:
            print "Zu gross. / Too high."
        else:
            print "Zu klein. / Too low."

        tries += 1


def save_highscore(tries, name):
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
        
    highscore.append("%i\t%s\n" % (tries, name))
    highscore.sort()
    highscore = highscore[:10]

    with open(HIGHSCORE, "w") as f:
        f.writelines(highscore)


def print_highscore():
    """
    Gib Highscore aus.

    Print highscore to stdout.
    """

    print
    print "H I G H S C O R E"

    with open(HIGHSCORE) as f:
        print f.read()

    print
    

if __name__ == "__main__":
    # Hauptschleife:
    #
    # Main loop:
    
    while True:
        name = raw_input("Dein Name / Your name: ")
        tries = highlow()
        save_highscore(tries, name)
        print_highscore()
        another = raw_input("Weiter spielen / Another game? (y/n) ")
        if another.lower().startswith("n"):
            break 

        # Bei gut gewahlten Funktionen und Funktionsnamen liest sich
        # das fast wie Prosa. ;-)
        #
        # If you choose your functions and function names wisely,
        # this almost reads like prose. ;-)
