#!/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #socket.AF_INET - ipv4 connection,
# sock is variable and rest is how we define an object
# socket.SOCK_STREAM - use tcp packet only as udp is connectionless 3 way handshake.

host = input("Enter the host to Scan: ")
port = int(input("Enter the port to Scan: "))

def portscanner(port):
        if sock.connect_ex((host,port)):     #if error is recieved port is closed connect_ex function look for error
                print ("Port %d is closed" % (port))
        else:
                print ("Port %d is opened" % (port))

portscanner(port)

