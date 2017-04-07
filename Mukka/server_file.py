from socket import *
import os, json

def chkRequest(cli,snd):
	fileDetails = {}
	fileDetails["File"] = snd
	fileDeatils["Size"] = os.path.getsize(snd)
	
	cli.send(json.dumps(fileDetails))
	if cli.recv(2) == 'y':
		return
	else
		print "\n\nRequest Cancelled"
		exit(-1)
	
maxSize = 1000000

#socket oprations
a  = socket()
a.bind(("",5000))
a.listen(5)
cl,addr = a.accept()
print "Connection recieved from " + str(addr[0]) + "\n"


#file details
snd = ""
size = os.path.getsize(snd)
chkRequest()


#sending files
fileSend = open(snd,'r')

while size >= maxSize:
	sendStr =  fileSend.read(maxSize)
	cl.send(sendStr)
	size -= maxSize

cl.send(size)
fileSend.close()

print "\nFile sent sucessfully!\n"

