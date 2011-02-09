#!/usr/bin/env python

import socket

server_socket = socket.socket(socket.AF_INET)
server_socket.bind(("localhost", 6666))

# Server muss zuerst gestartet werden. Beim Verbindung zu einem
# anderen Rechner richtigen Hostnamen oder IP-Adresse des Servers
# angeben und hoffen, dass keine Firewall blockiert.

server_socket.listen(1)
# Ab hier wartet der Server so lange, bis eine Client-Verbindung kommt.

# Eine eingehende Verbindung akzeptieren:
(sock, address) = server_socket.accept()

print "Got connection from", address

while True:
    income = sock.recv(1024)
    # Blockiert so lange, bis Daten empfangen werden
    
    if income:
        print income,
    else:
        # Es konnte nichts mehr gelesen werden, Verbindung ist
        # unterbrochen worden
        break


