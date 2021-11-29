#CLIENT - SERVER Architecture

# Server opens up a session with every client that connects to it.
# This way Server will be able to serve multiple clients at once and individually


#SERVER SOCKET METHODS

# bind() binds the address that consists of hostname and port to the socket
# listen() wait for the message or a signal
# accept() accepts the connection with a client


#CLIENT SOCKET METHODS
#For a client, connect() is the only specifiv and very important method
# with this method client tries to connect to a server with then accepts this with the respective method


#OTHER SOCKET METHODS
#Important general socket methods

#recv() receive a TCP Message
#send() sends a TCP Message
#recvfrom() receives a UDP message
#sendto() sends a UDP Message
#close() closes a socket
#gethostname() returns hostname of a socket


#Creating a Server
#We are going to implement our server.
#we decided to use TCP and an internet socket.
#For the address we will use the localhost address 127.0.0.1
#and as a port we will choose 9999

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind method is use to assign IP-address and port, we pass tuple as parameter
s.bind(("127.0.0.1", 9999))

#we put our socket to listening mode by using the method listen()
s.listen()
print("Listening...")

#next we create server.py and client.py