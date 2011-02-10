#!/usr/bin/env python

# Von object ableiten ist wichtig, damit Properties funktionieren:
#
# Inheriting from object is important for properties to work:

class Konto(object):
    """
    Konto-Klasse.

    Banc account class.
    """

    # Zinssatz ist fuer alle Konten gleich, also Klassenattribut:
    #
    # interest rate is the same for all accounts, thus a class attribute:

    zinssatz = 0.03
    
    def __init__(self, nummer, inhaber, stand=0.0):
        # Kontonummber und Inhaber sind je Konto verschieden, also
        # Objektattribute:
        #
        # Account number and holder are different per account, thus
        # object attributes:
        self.nummer = int(nummer)
        self.inhaber = str(inhaber)

        # Wir wollen den Kontostand ueber Getter und Setter aendern,
        # deswegen markieren wir das Attribut mit einem Unterstrich
        # als "private" Variable:
        #
        # We want to use getters and setters on the account balance,
        # thus we mark the attribute as "private" via a leading
        # underscore:
        self._stand = float(stand)


    def __str__(self):
        return "%i %s %.2f" % (self.nummer, self.inhaber, self._stand)


    def set_stand(self, new):

        if new < 0:
            raise ValueError("Kontostand zu niedrig.")
        else:
            self._stand = new


    def get_stand(self):
        return self._stand


    stand = property(get_stand, set_stand)
    # Jetzt koennen wir auf das Objektattribut stand zugreifen wie auf
    # ein normales Attribut, jedoch werden automatisch die Getter und
    # Setter verwendet
    #
    # Now we can acces the object attritute for the account balance
    # like an ordinary attrigute, but behinde the scenes the getter
    # and setter methods will be used
    

    # Zinssatz ausgeben ist fuer alle Objekte gleich, deswegen
    # Klassenmethode:
    #
    # Displaying the Interest rate is the same for all objects,
    # thus a class method:
    @classmethod
    def get_zinssatz(cls):
        return "Der Zinssatz betraegt %s" % cls.zinssatz


    def berechne_zinsen(self):
        return self.stand * self.__class__.zinssatz



if __name__ == "__main__":
    k = Konto(1234, "Rebecca Breu", 1000.0)
    print k
    k.stand = k.stand - 50
    print k
    print k.get_zinssatz()
    print "Zinsen:", k.berechne_zinsen()
    k.stand = k.stand - 1200
    print k
