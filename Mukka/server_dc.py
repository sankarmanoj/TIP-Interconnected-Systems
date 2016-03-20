#Ver 0.1b <2016-03-20  Chaitanya  <chaitanya.mvs2007@gmail>

from socket import *
from time import *
import os, json

fileDetails = {}

def chkRequest(cli,snd):
	fileDetails["File"] = snd
	fileDetails["Size"] = os.path.getsize(snd)
	
	x = json.dumps(fileDetails)
	cli.send(x)
	
	chk = cli.recv(1)
	#print chk
	if chk == 'y':
		return
	else:
		print "\n\nRequest Cancelled"
		#exit(-1)
		os.system("pause")
	
maxSize = 1700

#socket oprations
a  = socket()
a.bind(("",5000))
a.listen(5)
cl,addr = a.accept()
print "Connection recieved from " + str(addr[0]) 


#file details
snd = "chk.jpg"
size = os.path.getsize(snd)
chkRequest(cl,snd)

print "\nNow Sending"
#sending files
fileSend = open(snd,'rb')


while size >= maxSize:
	sendStr = fileSend.read()
	cl.send(sendStr)
	size -= maxSize
	#print size

sendStr =  fileSend.read(size)
cl.send(sendStr)

if cl.recv(1):
	cl.send("r\a")

fileSend.close()
print "\nFile sent sucessfully!\n"
os.system("pause")
