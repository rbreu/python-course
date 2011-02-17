#!/usr/bin/env python

import string
import random

pwd = ""

for i in range(8):
    pwd += random.choice(string.letters + string.digits + "-_.")

# sting.letters enthaelt alle Buchstaben (gross und klein),
# string.digits enthaelt alle Ziffern.
#
# string.letters contains all letters (capitalised and uncapitalised),
# string.digits contains all digits.
    
print pwd


