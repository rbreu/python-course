#!/usr/bin/env python

import sys

infile = open("table_data.txt", "r")
outfile = open("table_data_out.txt", "w")

for zeile in infile.readlines():
    zahlen = zeile.strip().split(":")

    summe = 0.0
    for zahl in zahlen:
        summe += float(zahl)

    #Profi-Variante zum Berechnen der Summe:
    #summe = map(float, zahlen).sum()

    zahlen.append(str(summe))
    outfile.write(":".join(zahlen) + "\n")


infile.close()
outfile.close()


