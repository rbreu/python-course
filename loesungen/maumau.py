#!/usr/bin/env python

import random

class WinException(Exception):
    pass

class TalonEmptyException(Exception):
    pass


class Karte:
    def __init__(self, farbe, wert):
        self.farbe = farbe
        self.wert = wert

    def __str__(self):
        return "%s %s" % (self.farbe, self.wert)

    def __repr__(self):
        return "%s %s" % (self.farbe, self.wert)
            
    def kompatibel(self, other):
        """Kann man die Karten aufeinander legen?"""
        return (self.farbe == other.farbe) or (self.wert == other.wert)


class Deck32(list):
    """Ein gemischtes Skatblatt."""
    WERTE = ["7", "8", "9", "10", "Bube", "Dame", "Koenig", "As"]
    FARBEN = ["Karo", "Herz", "Pik", "Kreuz"]

    def __init__(self):
        karten = []

        for farbe in self.FARBEN:
            for wert in self.WERTE:
                karten.append(Karte(farbe, wert))

        random.shuffle(karten)

        list.__init__(self, karten)


class Spieler:
    def __init__(self, name, talon):
        self.name = name
        self.karten = [talon.pop() for i in range(6)]


class ComputerSpieler(Spieler):

    def suche_karte(self, ablage):
        """Suche Karte, die auf die Ablage passt."""

        for karte in self.karten:
            if karte.kompatibel(ablage[-1]):
                return karte
      

    def ziehe(self, ablage, talon):
        """Ein Spielzug."""


        karte = self.suche_karte(ablage)

        if karte: #karte gefunden
            print "%s spielt %s" % (self.name, karte)
            self.karten.remove(karte)
            ablage.append(karte)
            if not self.karten:
                raise WinException
        else: #keine passende Karte gefunden
            print "%s zieht eine Karte." % self.name
            try:
                self.karten.append(talon.pop())
            except:
                raise TalonEmptyException()


talon = Deck32()
ablage = [talon.pop()]

spieler = [ComputerSpieler("Computer1", talon), 
           ComputerSpieler("Computer2", talon)]

while True:
    for s in spieler:
        print "Ablage:", ablage[-1]
        s.ziehe(ablage, talon)


                                  
