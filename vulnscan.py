#!/usr/bin/python

import socket
import os
import sys

def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return

def checkVulns(banner, filename):
	f = open(filename, "r") # file is open as read
	for line in f.readlines():	#function to read file line by line f.readlines
		if line.strip("\n") in banner:		#we strip out the new line character "\n"
			print("Server is vulnerable: ", banner.strip("\n"))
			# look for python .strip function


def main():
	if len(sys.argv) == 2:  # check we have provided the vuln filename
		filename = sys.argv[1]
		if not os.path.isfile(filename):	#check is file exist or not
			print("File doesn't exist!")
		if not os.access(filename, os.R_OK):	#check filename permission
			print("Access Denied!")
			exit(0)
		else:
			print("Usage: ", str(sys.argv[0]), " <vuln filename>") #how to use the python program
			exit(0)
		portlist = [21,22,25,80,110,443,445] 	# list of ports which we will scan on multiplehost
		for x in range(214,215) # (4 is localhost, 6 is metalsploitable) (1,255) for entire network

			#ip = "192.168.1." + str(x)
			ip = "10.3.79." + str(x)

			for port in portlist:
				banner = retBanner(ip,port)
				if banner:
					print(ip,"/", str(port), ":", banner)
					checkvulns(banner, filename)

main()
