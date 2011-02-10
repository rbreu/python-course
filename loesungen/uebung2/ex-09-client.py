#!/usr/bin/env python

from xmlrpclib import ServerProxy, Fault

server = ServerProxy("http://grow.zam.kfa-juelich.de:8000")
print server.system.listMethods()
print server.system.methodHelp("surprise")
print
print server.add(4, 5)
print server.surprise(0)

# Mal sehen was passiert....
#
# Let's see what happens....
print server.surprise(10)

# Das verursacht eine Ausnahme auf Client-Seite!
# Der Server laeuft noch.
#
# That causes an exception on client side, not on server side!
# The server is still running.

try:
    print server.surprise(10)
except Fault:
    print "Oops!"
