#!/usr/bin/env python

import sys
import re

name = (sys.argv[1])

in_data = open(name).read()
out_data = re.sub("<.*?>", "", in_data)

# Zum regulaeren Ausdruck:
# < > sucht nach den spitzen Klammern, interessant ist, was dazwischen steht:
# . matcht eine beliebiges Zeichen (ausser Zeilenumbruch)
# * ist ein Modifier fuer . sodass beliebig viele Zeichen gematcht werden
# ? ist ein Modifier und bedeutet non-greedy, d.h. nur der kleinstmoegliche
#   Match wird genommen. Ohne wuerde auch folgendes als gesamtes matchen:
#   <h1>bla</h1> sdfsdf <h2>blupp</h3>
#   Wir wollen aber nur die einzelnen Teile <h1>bla</h1> und <h2>blupp</h3>


outfile = open(name + ".txt", "w")
outfile.write(out_data)
outfile.close()
        


# Wiedereinmal schlampiger Umgang mit Dateiobjekten bzgl. close...
