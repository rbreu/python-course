#!/usr/bin/env python

import sys

with open("ex-15-in.txt", "r") as infile:
    with open("ex-15-out.txt", "w") as outfile:

        # Wir koennen direkt ueber Fileobjekte iterieren und erhalten
        # die einzelnen Zeilen:
        #
        # We can directly iterate over file objects and get the lines:
        for (i, line) in enumerate(infile):
            outfile.write("%i. %s" %(i, line))

