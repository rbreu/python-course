#!/usr/bin/env python

class Bunch:
    def __init__(self, **kwargs):
        for (key, value) in kwargs.items():
            setattr(self, key, value)


if __name__ == "__main__":
    punkt = Bunch(x=2, y=3)
    print punkt.x, punkt.y

    person = Bunch(vorname="Homer", nachname="Simpson", telefon=123456)
    print person.vorname, person.nachname, person.telefon
