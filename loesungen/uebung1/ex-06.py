#!/usr/bin/env python

s = raw_input("Ein String / Some string: ")

# Auch ueber Strings kann man iterieren:
#
# You can iterate over strings:
for char in s:
    print ord(char),


# Bitte nicht:
#
# Please don't:
    
# for i in range(len(s)):
#     print ord[s[i]]
