#!/usr/bin/env python

# Von object ableiten ist wichtig, damit Properties funktionieren:

class Konto(object):
    """Konto-Klasse."""


    zinssatz = 0.03  # Fuer alle Konten gleich, also Klassenattribut

    def __init__(self, nummer, inhaber, stand=0.0):
        # Je Konto verschieden, also Objektattribute:
        self.nummer = int(nummer)
        self.inhaber = str(inhaber)

        # Wir wollen den Kontostand ueber Getter und Setter aendern,
        # deswegen markieren wir das Attribut mit einem Unterstrich
        # als "private" Variable:
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
    

    # Zinssatz ausgeben ist fuer alle Objekte gleich, deswegen
    # Klassenmethode:
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
