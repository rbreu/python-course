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
        except:
            print "Ignoriere:", char

    return morse


print letters2morse("Rebecca")
print letters2morse("Hallo Welt")
print letters2morse("Hallo! Welt!")
