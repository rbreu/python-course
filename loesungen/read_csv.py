#!/usr/bin/env python

import csv

reader = csv.reader(open("adressen.csv"))

for row in reader:
    print "=" * 20
    for item in row:
        print item
