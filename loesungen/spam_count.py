#!/usr/bin/env python

import sys

f = open(sys.argv[1], "r")
content = f.read()
print "Spam count:", content.count("Spam")

