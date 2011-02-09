#!/usr/bin/env python

def freier_fall(h_0, t, g=9.81):
    return h_0 - 1/2.0 * g * t**2


print freier_fall(10, 0.5)
print freier_fall(t=0.5, g=9.81, h_0=10)
print freier_fall(t=2, g=3, h_0=10)
