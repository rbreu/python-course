#!/usr/bin/env python

def is_palindrome(s):
    for (i, char) in enumerate(s):
        if char != s[-i-1]:
            return False
    else:
        return True

while True:
    try:
        user_input = raw_input("Some string: ")
    except (KeyboardInterrupt, EOFError):
        print   # print ohne Parameter ergibt eine Leerzeile
                # print without parameter yields an empty line
        quit = raw_input("Really quit? (y/n) ")
        if quit.lower().startswith("y"):
            # durch lower und startswith ist es egal, ob er benutzer
            # Y, y, YES, yes, Yes, ... eingibt
            #
            # because of lower and startswith it doesn't matter whether
            # the user enters Y, y, YES, yes, Yes, ...
            break
        else:
            continue

    print "Palindrome?", is_palindrome(user_input)





