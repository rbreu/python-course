#!/usr/bin/env python

HAEUFIG = set("adehinrstu")

def haeufig_test(s):
    return set(s.lower()) <= HAEUFIG

def haeufig_rest(s):
    return set(s.lower()) - HAEUFIG


print haeufig_test("Rebecca"), haeufig_rest("Rebecca")
print haeufig_test("Einstein"),  haeufig_rest("Einstein")
