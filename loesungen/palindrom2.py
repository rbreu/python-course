#!/usr/bin/env python

def palindrom(s):
    for (i, char) in enumerate(s):
        if char != s[-i-1]:
            return False
    else:
        return True


while True:
    try:
        eingabe = raw_input("Ein String: ")
    except (KeyboardInterrupt, EOFError):
        print
        beenden = raw_input("Wirklich beenden? (y/N) ")
        if beenden.lower().startswith("y"):
            break
        else:
            continue

    print "Palindrom?", palindrom(eingabe)


