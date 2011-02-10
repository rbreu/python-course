#!/usr/bin/env python

from SimpleXMLRPCServer import SimpleXMLRPCServer

class MyFuncs:

    def __init__(self):
        self.log = open("xmlrpc.log", "w")

        self.data = """Once upon a midnight dreary, while I pondered weak and weary,
Over many a quaint and curious volume of forgotten lore,
While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
`'Tis some visitor,' I muttered, `tapping at my chamber door -
Only this, and nothing more.'""".splitlines()
    
    def add(self, x, y):
        """
        add(x, y)
        Adds two numbers.
        """

        self.log.write("%s\n" % (x + y))
        return x + y

    
    def surprise(self, i):
        """
        Takes an integer between 0 and 5.
        Don't you dare pass an invalid number!!!
        """

        self.log.write("secret\n")

        return self.data[i]

    
    
server = SimpleXMLRPCServer(("grow.zam.kfa-juelich.de", 8000))
server.register_instance(MyFuncs())
server.register_introspection_functions()
server.serve_forever()
