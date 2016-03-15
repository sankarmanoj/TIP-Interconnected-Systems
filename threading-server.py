def clientHandler(clientSocket):
    inputString = "a"
    #If the connection to the client closes, it will return an empty string
    while inputString!="":
        inputString= clientSocket.recv(100)
        print inputString
    print "Connection Closed"
from socket import *
from threading import Thread
PORT=9999
server = socket()
# Bind to Port 9999
#Try using different IP addresses while binding.
server.bind(("localhost",9999))
#server.bind(("192.168.0.2",9999))
server.listen(5)
while True:
    (client,address)=server.accept()
    clientThreads=[]
    newThread = Thread(target=clientHandler,args=(client,))
    newThread.start()
    clientThreads.append(newThread)
