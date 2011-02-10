#!/usr/bin/env python

def is_palindrome(s):
    """
    Prueft ob ein String ein Palyndrom ist.
    
    Tests if a given string is a palindrome.
    """
    
    # Wenn wir doch Indizes benoetigen, ist enumerate meist
    # noch schoener als range(len(...)):
    #
    # Should we need indices, enumerate is probably nicer than
    # range(len(...)):
    for (i, char) in enumerate(s):
        if char != s[-i-1]:
            return False
    else:
        return True


print is_palindrome("rebecca")
print is_palindrome("lagerregal")


# Wir haben keine Besonderheiten von Strings in der Funktion verwendet.
# Allein Iterierbarkeit wird vorausgesetzt, sodass wir die Funktion auch
# auf andere Objekte als Strings anwenden koennen:
#
# We didn't use any attributes special to strings in our function.
# Only the possibility to iterate over the object is needed, thus we
# can use our function for other objects than strings:
print is_palindrome([1, 2, 3, 2, 1])
print is_palindrome((1, 2, 3, 4, 5))



# Eine andere Loesung, die auch wieder beliebige iterierbare Objekte nimmt:
#
# Another solution which also works for arbitrary iterable objects:

def is_palindrome2(s):
    l1 = list(s)
    l2 = list(s)
    l2.reverse()
    return l1 == l2


# Anmerkung zur letzten Zeile: Der boolsche Ausdruck liefert einen
# Wahrheitswert als Ergebnis, den wir wie Rechenergebnisse auch
# weiter verwenden koennen.
# Wir brauchen also nicht schreiben:
#
# Remark regarding the last line: The boolean expression returns
# a bool type, which we can directly use (the same as we can use
# return values of arithmetic operations).
# We don't have to write:

# if l1 == l2 :
#     return True
# else:
#     return False
