#!/usr/bin/env python

FREQUENT = set("adehinrstu") # this is the German alphabet version

def frequent_test(s):
    return set(s.lower()) <= FREQUENT

def frequent_remain(s):
    return set(s.lower()) - FREQUENT


print frequent_test("Rebecca"), frequent_remain("Rebecca")
print frequent_test("Einstein"),  frequent_remain("Einstein")
