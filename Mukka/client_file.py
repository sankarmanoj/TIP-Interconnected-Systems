from socket import *
import json, os

maxSize = 1000000

def fileRecv(serv,Detail):
	fileRecv = open(Detail["Name"],'w+')
	size = Detail["Size"]
	
	while size >= maxSize:
		recvStr = cl.recv(maxSize)
		fileRecv.write(recvStr)
		size -= maxSize
	
	recvStr = cl.recv(size)
	fileRecv.write(recvStr)
	fileRecv.close()

def actRequest(serv):
	fileDet = json.loads(serv.recv(1000))
	print "\nDo you really want to download the file? (y/n) ..."
	print "\nFileName: %s \nSize: %s\n\n Choice:" %(fileDet["Name"],fileDet["Size"])
	
	if raw_input() == 'y':
		fileRecv(serv,fileDet)
	else
		print "Downloading Cancelled"
		exit(-1)
	
	
cl = socket()
cl.connect(("127.0.0.1",5000))

actRequest()
fileRecv()



	
