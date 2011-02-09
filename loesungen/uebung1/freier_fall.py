#!/usr/bin/env python

def freier_fall(h_0, t, g=9.81):
    # Durch die 2.0 als Float wird garantiert, dass immer in Float
    # gerechnet wird, auch wenn der Anwender nur Ints uebergibt:
    return h_0 - 1/2.0 * g * t**2



print freier_fall(10, 0.5, 7)

# Werden Parameternamen explizit angegeben, ist die Reihenfolge egal:
print freier_fall(t=0.5, g=3, h_0=10)

# Default-Parameter muessen nicht angegeben werden:
print freier_fall(t=2, h_0=10)
print freier_fall(10, 2)
