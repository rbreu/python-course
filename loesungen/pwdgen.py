#!/usr/bin/env python

import string
import random

pwd = ""


for i in range(8):
    pwd += random.choice(string.letters+string.digits)

print pwd


