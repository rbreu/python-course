#!/usr/bin/env python

import sys
import re

name = (sys.argv[1])

in_data = open(name).read()
out_data = re.sub("<.*?>", "", in_data)

# Zum regulaeren Ausdruck:
# < > sucht nach den spitzen Klammern; interessant ist, was dazwischen steht:
# . matcht eine beliebiges Zeichen (ausser Zeilenumbruch)
# * ist ein Modifier fuer . sodass beliebig viele Zeichen gematcht werden
# ? ist ein Modifier und bedeutet non-greedy, d.h. nur der kleinstmoegliche
#   Match wird genommen. Ohne wuerde auch folgendes als gesamtes matchen:
#   <h1>bla</h1> sdfsdf <h2>blupp</h3>
#   Wir wollen aber nur die einzelnen Teile <h1>bla</h1> und <h2>blupp</h3>
#
# Explanation fo the regular expression:
# < > matches angled brackets; the interesting bit is inbetween:
# . matches any character (execpt a line break)
# * is a modifier for . so that arbitrary many characters are matched
# ? is a modifier and means non-greedy, i.e. only the smallest possible match
#   is used. Without the modifier the following would match as a whole:
#   <h1>bla</h1> sdfsdf <h2>blupp</h3>
#   But we only want the parts <h1>bla</h1> and <h2>blupp</h3>


outfile = open(name + ".txt", "w")
outfile.write(out_data)
outfile.close()
        


# Wiedereinmal schlampiger Umgang mit Dateiobjekten bzgl. close...
#
# Once more sloppy file handling regarding close...
