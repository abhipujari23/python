# Sockets are endpoints of the communication channel, they talk to each other
#Communication can happen between same process or even across different continents over internet

#Creating Socket: we need to import socket
import socket

#before we start we need to know few things in advance
#Are we using internet socket or a UNIX socket?
#Which protocol are we going to use?
#Which IP-address are we using?
#Which port number are we using?

#AF_INET states that we want internet socket rather than UNIX Socket
#SOCK_STREAM is for protocol that we choose in this case it stands for TCP
#if we want to use UDP we would choose SOCK_DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
