#!/usr/bin/env python

import socket

server_socket = socket.socket(socket.AF_INET)
server_socket.bind(("localhost", 6666))
server_socket.listen(1)
(sock, address) = server_socket.accept()

print "Got connection from", address

while True:
    income = sock.recv(1024)
    if income:
        print income,
    else: 
        break


