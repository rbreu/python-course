#!/usr/bin/env python

def fakultaet(n):
    
    if n<0:
        raise ValueError("Fakultaet fuer negative Zahlen nicht definiert.")

    fak = 1
    for i in range(1, n+1):
        fak *= i

    return fak


print fakultaet(0)
print fakultaet(-2)
print fakultaet(3)
