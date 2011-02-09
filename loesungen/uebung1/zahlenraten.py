#!/usr/bin/env python

from random import randint

# Programmeinstellungen, die konstant bleiben, gerne als globale
# Variablen am Anfgan der Datei definieren. Durch Grossschreibung
# als Konstanten kennzeichnen.

HIGHSCORE = "zahlenraten_highscore.txttt"


# Laengere Programme in sinnvolle Funktionen gliedern!

def zahlenraten():
    """
    Ein Spieldurchlauf Zahlenraten.

    Es wird eine Zufallszahl generiert und der Benutzer solange gefragt,
    bis er die Zahl geraten hat.

    Gibt die Anzahl der benoetigten Versuche zurueck.
    """
    
    zahl = randint(1, 100)
    versuche = 1

    while True:
        try:
            eingabe = int(raw_input("Rate eine Zahl: "))
        except ValueError:
            print "Das ist keine Zahl."
            continue
        if eingabe == zahl:
            print "Richtig! Du hast %i Versuche gebraucht." % versuche
            return versuche
        elif eingabe > zahl:
            print "Zu gross."
        else:
            print "Zu klein."

        versuche += 1


def highscore_speichern(versuche, name):
    """Fuege einen Eintrag zur Highscore-Liste hinzu."""

    # Den alten Highscore als Liste einlesen:
    f = open(HIGHSCORE)

    try:
        highscore = f.readlines()
    except IOError:
        print "Could not read highscore, start new."
        highscore = []
    finally:
        f.close()

    # Den neuen Eintrag hinzufuegen und die besten zehn
    # Eintraege abspeichern:
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
    """Print highscore to stdout."""

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
    while True:
        name = raw_input("Dein Name: ")
        versuche = zahlenraten()
        highscore_speichern(versuche, name)
        highscore_ausgeben()
        weiter = raw_input("Weiter spielen? (y/n) ")
        if weiter.lower().startswith("n"):
            break 

        # Bei gut gewahlten Funktionen und Funktionsnamen liest sich
        # das fast wie Prosa. ;-)
