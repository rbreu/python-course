#!/usr/bin/env python

s = raw_input("Ein String: ")

# Auch ueber Strings kann man iterieren:
for char in s:
    print ord(char),


# Bitte nicht:
# for i in range(len(s)):
#     print ord[s[i]]
