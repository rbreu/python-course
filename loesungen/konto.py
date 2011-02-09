#!/usr/bin/env python

class Konto(object):

    zinssatz = 0.03

    def __init__(self, nummer, inhaber, stand=0.0):
        self.nummer = int(nummer)
        self.inhaber = str(inhaber)
        self.__stand = float(stand)

    def __str__(self):
        return "%i %s %.2f" % (self.nummer, self.inhaber, self.__stand)

    def set_stand(self, new):

        if new < 0:
            raise ValueError("Kontostand zu niedrig.")
        else:
            self.__stand = new

    def get_stand(self):
        return self.__stand

    stand = property(get_stand, set_stand)


    @classmethod
    def get_zinssatz(cls):
        return "Der Zinssatz betraegt %s" % cls.zinssatz

    def berechne_zinsen(self):
        return self.stand * self.__class__.zinssatz



k = Konto(1234, "Rebecca Breu", 1000.0)
print k
k.stand = k.stand - 50
print k
print k.get_zinssatz()
print "Zinsen:", k.berechne_zinsen()
k.stand = k.stand - 1200
print k
