#!/usr/bin/python

import socket

def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket() 	#socket object
		s.connect((ip,port))	#connection
		banner = s.recv(1024)	# we will recieve 1024 bytes from the target recv=recieve
		return banner
	except:
		return


def main():
	ip = input("Enter target ip \t")
	for port in range(1,100):
		banner = retBanner(ip,port)
		if banner:
			print(ip,'/',port, ':' ,banner)
main()
