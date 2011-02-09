#!/usr/bin/env python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Verbinde mit Server:
sock.connect(("localhost", 6666))

# Server muss zuerst gestartet werden. Beim Verbindung zu einem
# anderen Rechner richtigen Hostnamen oder IP-Adresse des Servers
# angeben und hoffen, dass keine Firewall blockiert.

while True:
    user_input = raw_input("> ")
    sock.send(user_input + "\n")

