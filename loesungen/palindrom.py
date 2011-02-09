#!/usr/bin/env python

def palindrom(s):
    for (i, char) in enumerate(s):
        if char != s[-i-1]:
            return False
    else:
        return True


print palindrom("rebecca")
print palindrom("lagerregal")

print palindrom([1, 2, 3, 2, 1])
print palindrom([1, 2, 3, 4, 5])

