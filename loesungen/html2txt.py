#!/usr/bin/env python

import sys
import re

name = (sys.argv[1])

in_data = open(name).read()
out_data = re.sub("<.*>", "", in_data)

outfile = open(name + ".txt", "w")
outfile.write(out_data)
outfile.close()
        


