from socket import *
PORT = 9999
client = socket()
#Try using different IP addresses while binding. 
address=("localhost",9999)
# address = ("192.168.0.2",9999)
#connect to the given address
client.connect(address)
while True:
    #Take input from the user and set to the server
    userInput = raw_input("Enter some string")
    client.send(userInput)
