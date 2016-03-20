#Ver 0.1b <2016-03-20  Chaitanya  <chaitanya.mvs2007@gmail>

from socket import *
import json, os,time



def fileRecv(serv,Detail):
	recvStr = ""
	fileRecv = open(Detail["File"],'wb')
	size = Detail["Size"]
		
	while size >= maxSize:
		recvStr = serv.recv(maxSize)
		fileRecv.write(recvStr)
		size -= maxSize
		#print size
	
	recvStr = cl.recv(size)
	fileRecv.write(recvStr)
	serv.send("r");
	if serv.recv(1):
		fileRecv.close()
	
	
'''def fileRecv(serv,Detail):
	fileRecv = open(Detail["File"],'wb')
	size = Detail["Size"]

	serv.settimeout(10)
	
	while True:
		try:
			if not recvStr:
				recvStr = cl.recv(maxSize)
				time.begin()
				break
			else:
				fileRecv.write(recvStr)
		except timeout:
			break;
	fileRecv.close()'''
	

def actRequest(serv):
	fileDet = json.loads(serv.recv(1000))
	print "\nDo you really want to download the file? (y/n) ..."
	print "\nFileName: %s \nSize: %s\n\nChoice:" %(fileDet["File"],fileDet["Size"])
	
	if raw_input() == 'y':
		serv.send('y')
		fileRecv(serv,fileDet)
	else:
		print "Downloading Cancelled"
		exit(-1)
	
	
cl = socket()
cl.connect(("127.0.0.1",5000))

actRequest(cl)




	
