#!/usr/bin/env python

def free_fall(h_0, t, g=9.81):
    # Durch die 2.0 als Float wird garantiert, dass immer in Float
    # gerechnet wird, auch wenn der Anwender nur Ints uebergibt:
    #
    # By using the 2.0 as float we guarantee that all calculations
    # will be in float, even if the user passes ints only:
    return h_0 - 1/2.0 * g * t**2



print free_fall(10, 0.5, 7)

# Werden Parameternamen explizit angegeben, ist die Reihenfolge egal:
#
# If we use explicit parameter names, the order doesn't matter:
print free_fall(t=0.5, g=3, h_0=10)

# Default-Parameter muessen nicht angegeben werden:
#
# We can omit default parameters:
print free_fall(t=2, h_0=10)
print free_fall(10, 2)
