#!/usr/bin/env python

import random

class WinException(Exception):
    pass

class PileEmptyException(Exception):
    pass


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "%s %s" % (self.suit, self.rank)

    def __repr__(self):
        return "%s %s" % (self.suit, self.rank)
            
    def is_compatible(self, other):
        """
        Kann man die Karten aufeinander legen?

        Can you play one card onto another?
        
        """
        return (self.suit == other.suit) or (self.rank == other.rank)


class DeckUNO(list):
    """

    Ein UNO-Deck.

    A UNO Deck.
    """


    RANKS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    SUITS = ["Red", "Yellow", "Green", "Blue"]

    # Durch Ableiten und umdefinieren der beiden obigen Klassenattribute
    # kann man leicht weitere Karten-Decks erhalten, z.B. ein Skat-Blatt
    # fuer Mau-Mau
    #
    # By inheriting from this class and overwriting the above attributes,
    # you can easily obaint different card decks, e.g. a Skat deck
    # for the German variant Mau-Mau
    

    def __init__(self):
        cards = []

        for suit in self.SUITS:
            for rank in self.RANKS:
                cards.append(Card(suit, rank))

        # Fuer Profis eine kuerzere Variante:
        #
        # A shorter version for experts:
                
        # cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

        # or, using the itertools module:
        # cards = [ Card(s, r) for s, r in itertools.product(SUITS, RANKS) ]

        random.shuffle(cards)

        list.__init__(self, cards)


class Player:
    """
    Abstrakter Spieler.
    In abgeleiteten Klassen muss die Methode ziehe(self, played_cards, pile)
    implementiert werden, welche None zurueckgibt.

    Abstract player.
    In child classes, the method ziehe (draw) needs to be overwritten.
    """
    
    def __init__(self, name, pile):
        self.name = name
        self.cards = [pile.pop() for i in range(6)]


    def move(self, played_cards, pile):
        # Ein Spielzug. Diese Methode muss in abgeleiten Klassen
        # implementiert werden!
        #
        # One move. This methods needs to be overwritten in child
        # classes!
        raise NotImplementedError()
    


class ComputerPlayer(Player):
    """
    Computerspieler mit einfacher kuenstlicher Intelligenz.

    Computer player with simple artificial intelligence.
    """

    def find_card(self, played_cards):
        """
        Suche Karte, die auf die Ablage passt.

        Search a card which can be played onto the pile of played cards.
        """

        for card in self.cards:
            if card.is_compatible(played_cards[-1]):
                return card
      

    def move(self, played_cards, pile):
        """
        Ein Spielzug.

        One move.
        """

        card = self.find_card(played_cards)

        if card: #karte gefunden / found a playable card
            print "%s spielt/plays %s" % (self.name, card)
            self.cards.remove(card)
            played_cards.append(card)
            if not self.cards:
                raise WinException
        else: #keine passende Karte gefunden / no playable card
            print "%s zieht eine Karte / draws a card" % self.name
            try:
                self.cards.append(pile.pop())
            except:
                raise PileEmptyException()



if __name__ == "__main__":
    pile = DeckUNO()
    played_cards = [pile.pop()]

    spieler = [ComputerPlayer("Computer1", pile), 
               ComputerPlayer("Computer2", pile)]

    while True:
        for s in spieler:
            print "Played Card:", played_cards[-1]
            s.move(played_cards, pile)

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
