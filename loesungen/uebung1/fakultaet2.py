#!/usr/bin/env python

def fakultaet(n):
    
    if n<0:
        raise ValueError("Fakultaet fuer negative Zahlen nicht definiert.")

    fak = 1
    for i in range(1, n+1):
        fak *= i

    return fak


if __name__ == "__main__":
    print fakultaet(0)
    print fakultaet(-2)
    print fakultaet(3)

    # Hat nichts mit dieser Aufgabe zu tun, aber die if-Abfrage sorgt
    # dafuer, dass dieser Block nur ausgefuehrt wird, wenn diese Datei
    # als Programm ausgefuehrt wird.
    # Beim Importieren als Modul erhaelt man nur die oben definierte
    # Funktion, und nicht diese print-Ausgaben in diesem Block.
