#!/usr/bin/env python

from __future__ import with_statement
import subprocess
import os


with open("uebung1.tex") as f:
    tex_in = f.read()


for i in range(1112, 1140):
    filename = "uebung1.%04i" % i

    print "Generateing %s.tex", filename
    tex_out = tex_in.replace("XXXloginXXX", "username%i" % i)
    tex_out = tex_out.replace("XXXpasswortXXX", "secret")
    with open(filename+".tex", "w") as f:
        f.write(tex_out)

    print "Generating %s.pdf" % filename
    p = subprocess.Popen("pdflatex %s.tex > /dev/null" % filename, shell=True)
    os.waitpid(p.pid, 0)

    print "Cleaning up..."
    os.remove("%s.tex" % filename)
    os.remove("%s.log" % filename)
    os.remove("%s.aux" % filename)
    
