#!/usr/bin/env python

import sys
import os

root = sys.argv[1]

for entry in os.listdir(root):
    name = os.path.join(root, entry)
    (base, ext) = os.path.splitext(entry)
    if ext == ".htm":
        newname = base + ".html"
        print "Benenne %s in %s um." % (name, newname)
        os.rename(name, newname)
        


