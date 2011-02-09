#!/usr/bin/env python

def fakultaet(n):
    """
    Fakultaet von n, n! = 1 * 2 * ... * n
    """
    
    fak = 1
    for i in range(1, n+1):
        fak *= i

    return fak

# Eine rekursive Loesung ginge natuerlich auch, ist aber in diesem Fall
# weniger effizient schwerer zu lesen

print fakultaet(0)
print fakultaet(1)
print fakultaet(3)
