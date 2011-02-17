#!/usr/bin/env python

# Von object ableiten ist wichtig, damit Properties funktionieren:
#
# Inheriting from object is important for properties to work:

class Account(object):
    """
    Konto-Klasse.

    Banc account class.
    """

    # Zinssatz ist fuer alle Konten gleich, also Klassenattribut:
    #
    # interest rate is the same for all accounts, thus a class attribute:

    interest = 0.03
    
    def __init__(self, number, holder, balance=0.0):
        # Kontonummber und Inhaber sind je Konto verschieden, also
        # Objektattribute:
        #
        # Account number and holder are different per account, thus
        # object attributes:
        self.number = int(number)
        self.holder = str(holder)

        # Wir wollen den Kontostand ueber Getter und Setter aendern,
        # deswegen markieren wir das Attribut mit einem Unterstrich
        # als "private" Variable:
        #
        # We want to use getters and setters on the account balance,
        # thus we mark the attribute as "private" via a leading
        # underscore:
        self._balance = float(balance)


    def __str__(self):
        return "%i %s %.2f" % (self.number, self.holder, self._balance)


    def set_balance(self, new):

        if new < 0:
            raise ValueError("Balance too low.")
        else:
            self._balance = new


    def get_balance(self):
        return self._balance


    balance = property(get_balance, set_balance)
    # Jetzt koennen wir auf das Objektattribut balance zugreifen wie auf
    # ein normales Attribut, jedoch werden automatisch die Getter und
    # Setter verwendet
    #
    # Now we can acces the object attritute for the account balance
    # like an ordinary attrigute, but behinde the scenes the getter
    # and setter methods will be used
    

    # Zinssatz ausgeben ist fuer alle Objekte gleich, deswegen
    # Klassenmethode:
    #
    # Displaying the interest rate is the same for all objects,
    # thus a class method:
    @classmethod
    def get_interest(cls):
        return "The interest rate is %s" % cls.interest


    def calculate_interest(self):
        return self.balance * self.__class__.interest



if __name__ == "__main__":
    k = Account(1234, "Rebecca Breu", 1000.0)
    print k
    k.balance = k.balance - 50
    print k
    print k.get_interest()
    print "Interest:", k.calculate_interest()
    k.balance = k.balance - 1200
    print k
