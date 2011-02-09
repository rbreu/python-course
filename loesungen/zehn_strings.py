#!/usr/bin/env python

strings = []

for i in range(10):
    strings.append(raw_input("Ein String: "))

for s in strings:
    print s.replace("a", "e")
