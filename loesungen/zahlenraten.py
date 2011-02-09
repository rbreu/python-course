#!/usr/bin/env python

from random import randint

HIGHSCORE = "zahlenraten_highscore.txt"

def runde():
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
    try:
        f = open(HIGHSCORE)
        highscore = f.readlines()
        f.close()
    except IOError:
        highscore = []
        
    highscore.append("%i\t%s\n" % (versuche, name))
    highscore.sort()
    f = open(HIGHSCORE, "w")
    f.writelines(highscore)
    f.close()


def highscore_ausgeben():
    f = open(HIGHSCORE)
    print "H I G H S C O R E"
    print f.read()
    f.close()
  

#Hauptschleife:
while True:
    versuche = runde()
    name = raw_input("Dein Name: ")
    highscore_speichern(versuche, name)
    highscore_ausgeben()
    weiter = raw_input("Weiter spielen? (y/n)")
    if weiter.lower().startswith("n"):
        break 
