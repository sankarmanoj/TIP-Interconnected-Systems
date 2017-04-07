
from socket import *
from time import *
import json
from threading import Thread

cli ={}

def printDict(dictn):
	print "\n"+dictn["Name"] + " @ " + dictn["Time"] + " :  " + dictn["Msg"]

def sndMsg(serv):
	while 1:
		cli["Msg"] = raw_input("\nEnter Your Msg: ")
		cli["Time"] = strftime("%H:%M:%S")
		b.send(json.dumps(cli))

print "What is Your name?? : "
cli["Name"] = raw_input()

b = socket()
b.connect(("localhost",5001))

Thread(target = sndMsg, args = (b,)).start()

while 1:
	serSend = json.loads(b.recv(1000))
	printDict(serSend)
	
