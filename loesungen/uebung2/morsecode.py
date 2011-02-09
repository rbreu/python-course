#!/usr/bin/env python

MORSE = { "A": ".-",
          "B": "-...",
          "C": "-.-.",
          "D": "-..",
          "E": ".",
          "F": "..-.",
          "G": "--.",
          "H": "....",
          "I": "..",
          "J": ".---",
          "K": "-.-",
          "L": ".-..",
          "M": "--",
          "N": "-.",
          "O": "---",
          "P": ".--.",
          "Q": "--.-",
          "R": ".-.",
          "S": "...",
          "T": "-",
          "U": "..-",
          "V": "...-",
          "W": ".--",
          "X": "-..-",
          "Y": "-.--",
          "Z": "--..",
          " ": "   "}


def letters2morse(s):
    morse = ""
    for char in s.upper():
        try:
            morse += MORSE[char] + "  "
        except KeyError:
            print "Ignoriere unbekanntes Zeichen:", char

    return morse


print letters2morse("Rebecca")
print letters2morse("Hallo Welt")
print letters2morse("Hallo! Welt!")



# Eine etwas schoenere Variante, den String zusammenzubauen mit join,
# hier hat man keine ueberfluessigen Leerzeichen am Ende des Strings:

def letters2morse2(s):
    morse = []
    for char in s.upper():
        try:
            morse.append(MORSE[char])
        except KeyError:
            print "Ignoriere unbekanntes Zeichen:", char

    return "  ".join(morse)

