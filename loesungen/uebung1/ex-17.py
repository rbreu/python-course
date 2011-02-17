#!/usr/bin/env python

def factorial(n):
    
    if n<0:
        raise ValueError("Factorial not defined for negative numbers.")

    fac = 1
    for i in range(1, n+1):
        fac *= i

    return fac


if __name__ == "__main__":
    print factorial(0)
    print factorial(-2)
    print factorial(3)

    # Hat nichts mit dieser Aufgabe zu tun, aber die if-Abfrage sorgt
    # dafuer, dass dieser Block nur ausgefuehrt wird, wenn diese Datei
    # als Programm ausgefuehrt wird.
    # Beim Importieren als Modul erhaelt man nur die oben definierte
    # Funktion, und nicht diese print-Ausgaben in diesem Block.
    #
    # Unrelated to this exercise: the if condition ensures that the block
    # is only executed when we execute this file as a program.
    # On importing this file as a module, only the function definition
    # is executed and not the print statements in this block.
