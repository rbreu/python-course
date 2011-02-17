#!/usr/bin/env python

def factorial(n):
    """
    Fakultaet von n, n! = 1 * 2 * ... * n

    Factorial of n, n! = 1 * 2 * ... * n
    """
    
    fac = 1
    for i in range(1, n+1):
        fac *= i

    return fac

# Eine rekursive Loesung ginge natuerlich auch, ist aber in diesem Fall
# weniger effizient und schwerer zu lesen
#
# A recursive solution is also possible, but is in this case less efficient
# and harder to read

print factorial(0)
print factorial(1)
print factorial(3)
