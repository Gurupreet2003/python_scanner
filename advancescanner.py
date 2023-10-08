#!/usr/bin/python

from socket import *  #import socket why we dont use it like this we need to use it alot
import optparse  #this library allow us to specifi the help options
from threading import *

def connScan(tgtHost,tgtPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM) #change due to from socket import *
		sock.connect((tgtHost,tgtPort))
		print(tgtPort,'port is open')
	except:
		print(tgtPort,'is port is close')
	finally:
		sock.close()





def portScan(tgtHost,tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print('Unknown Host',tgtHost)
	try:
		tgtName = gethostbyaddr(tgtIP)
		print('Scan Results For:',tgtname[0])
	except:
		print('Scan Results for: ', tgtIP)

	setdefaulttimeout(5)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start() 



def main():
	parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports seperated by comma')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print(parser.usage)
		exit(0)
	portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
	main()
