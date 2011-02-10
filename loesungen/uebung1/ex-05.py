#!/usr/bin/env python

strings = []

for i in range(10):
    strings.append(raw_input("Ein String / A string: "))

for s in strings:
    print s.replace("a", "e")


# Bitte nicht:
#
# Please don't:
    
# for i in range(len(strings)):
#     print strings[i].replace("a", "e")
