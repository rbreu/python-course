#!/usr/bin/env python

def ulam_folge(n):
    ulam = []
    
    while True:
        ulam.append(n)
        if n == 1:
            break
        elif n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1

    # Wir koennen beliebige Objekte zurueckgeben, hier eine Liste:
    #
    # We can return arbitrary objects, in this case a list:
    return ulam


print ulam_folge(1)
print ulam_folge(6)




