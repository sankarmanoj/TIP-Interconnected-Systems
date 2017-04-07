
from socket import *
import json
from time import *
from threading import Thread

serv={}

def printDict(dictn):
	print "\n"+dictn["Name"] + " @ " + dictn["Time"] + " :  " + dictn["Msg"]

def cliSend(cli):
	while 1:
		serv["Msg"] = raw_input("\nEnter your Message: ")
		serv["Time"] = strftime("%H:%M:%S")
		cli.send(json.dumps(serv))

def cliRec(cli):
	while 1:
		x = json.loads(cli.recv(1000))
		printDict(x)


print "What is Your name?? : "
serv["Name"] = raw_input()

#socket 
a  = socket()
a.bind(("",5001))
a.listen(5)



while(1):
	cl,addr = a.accept()
	print "\n\nConnection recieved from " + str(addr) + "\n\n"
	Thread(target =  cliRec, args=(cl,)).start()
	Thread(target = cliSend, args = (cl,)).start()
	
	
	
