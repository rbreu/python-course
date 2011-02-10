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
        """
        Kann man die Karten aufeinander legen?

        Can you play one card onto another?
        
        """
        return (self.farbe == other.farbe) or (self.wert == other.wert)


class DeckUNO(list):
    """

    Ein UNO-Deck.

    A UNO Deck.
    """


    RANK = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    SUIT = ["Red", "Yellow", "Green", "Blue"]

    # Durch Ableiten und umdefinieren der beiden obigen Klassenattribute
    # kann man leicht weitere Karten-Decks erhalten, z.B. ein Skat-Blatt
    # fuer Mau-Mau
    #
    # By inheriting from this class and overwriting the above attributes,
    # you can easily obaint different card decks, e.g. a Skat deck
    # for the German variant Mau-Mau
    

    def __init__(self):
        karten = []

        for farbe in self.SUIT:
            for wert in self.RANK:
                karten.append(Karte(farbe, wert))

        # Fuer Profis eine kuerzere Variante:
        #
        # A shorter version for experts:
                
        # karten = [Karte(farbe, wert) for farbe in SUIT for wert in RANK]


        random.shuffle(karten)

        list.__init__(self, karten)


class Spieler:
    """
    Abstrakter Spieler.
    In abgeleiteten Klassen muss die Methode ziehe(self, ablage, talon)
    implementiert werden, welche None zurueckgibt.

    Abstract player.
    In child classes, the method ziehe (draw) needs to be overwritten.
    """
    
    def __init__(self, name, talon):
        self.name = name
        self.karten = [talon.pop() for i in range(6)]


    def ziehe(self, ablage, talon):
        # Diese Methode muss in abgeleiten Klassen implementiert werden!
        #
        # This methods needs to be overwritten in child classes!
        raise NotImplementedError()
    


class ComputerSpieler(Spieler):
    """
    Computerspieler mit einfacher kuenstlicher Intelligenz.

    Computer player with simple artificial intelligence.
    """

    def suche_karte(self, ablage):
        """
        Suche Karte, die auf die Ablage passt.

        Search a card which can be played onto the pile of played cards.
        """

        for karte in self.karten:
            if karte.kompatibel(ablage[-1]):
                return karte
      

    def ziehe(self, ablage, talon):
        """
        Ein Spielzug.

        One move.
        """

        karte = self.suche_karte(ablage)

        if karte: #karte gefunden / found a playable card
            print "%s spielt/plays %s" % (self.name, karte)
            self.karten.remove(karte)
            ablage.append(karte)
            if not self.karten:
                raise WinException
        else: #keine passende Karte gefunden / no playable card
            print "%s zieht eine Karte / draws a card" % self.name
            try:
                self.karten.append(talon.pop())
            except:
                raise TalonEmptyException()



if __name__ == "__main__":
    talon = DeckUNO()
    ablage = [talon.pop()]

    spieler = [ComputerSpieler("Computer1", talon), 
               ComputerSpieler("Computer2", talon)]

    while True:
        for s in spieler:
            print "Ablage:", ablage[-1]
            s.ziehe(ablage, talon)

    # Diese Hauptschleife laesst sich sehr einfach um weitere
    # Mitspieler erweitern.
    #
    # The main loops can easily be extended for more players


# Es koennen leicht verschiedene Typen von Karten, Kartendecks und Spielern
# in das Spiel eingefuegt werden, da die einzelnen Teile so unabhaengig
# wie moeglich voneinander gehalten sind.
#
# It is easy to extend the game by other Types of cards, decks and players,
# since the parts are kept as independent from each other as possible.
