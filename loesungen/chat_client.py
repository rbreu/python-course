#!/usr/bin/env python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 6666))
print sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)

while True:
    user_input = raw_input("> ")
    sock.send(user_input + "\n")


