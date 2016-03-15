from socket import *
PORT=9999
server = socket()
# Bind to Port 9999
#Try using different IP addresses while binding. 
server.bind(("localhost",9999))
#server.bind(("192.168.0.2",9999))
server.listen(5)
(client,address)=server.accept()
inputString = "a"
#If the connection to the client closes, it will return an empty string
while inputString!="":
    inputString= client.recv(100)
    print inputString
print "Connection Closed"
