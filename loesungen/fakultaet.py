#!/usr/bin/env python

def fakultaet(n):
    fak = 1
    for i in range(1, n+1):
        fak *= i

    return fak


print fakultaet(0)
print fakultaet(1)
print fakultaet(3)
