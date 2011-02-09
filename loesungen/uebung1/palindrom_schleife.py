#!/usr/bin/env python

def is_palindrome(s):
    for (i, char) in enumerate(s):
        if char != s[-i-1]:
            return False
    else:
        return True

while True:
    try:
        eingabe = raw_input("Ein String: ")
    except (KeyboardInterrupt, EOFError):
        print   # print ohne Parameter ergibt eine Leerzeile
        beenden = raw_input("Wirklich beenden? (y/N) ")
        if beenden.lower().startswith("y"):
            # durch lower und startswith ist es egal, ob er benutzer
            # Y, y, YES, yes, Yes, ... eingibt
            break
        else:
            continue

    print "Palindrom?", is_palindrome(eingabe)



# Statt die Palindrom-Funktion nochmal zu schreiben, koennte man den Code
# der anderen Palindrom-Aufgabe importieren und die dortige Funktion
# wiederverwenden:

# import palindrom
# palindrom.is_palindrome(...)

# Dazu waere es nueztlich, wenn das Programm der anderen Aufgabe mit
# if __name__ == "__main__":
# arbeitet


