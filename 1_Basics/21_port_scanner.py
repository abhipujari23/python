#we learned multithreading, locking, queues and sockets
#using all this we can create a highly efficient port scanner

#Port Scanner tries to connect to certain port at the host or whole network in order to find loopholes or
#for future attacks
#Open ports means security breach
#Using our current knowledge we can code our own penetration testing tool

import socket
from queue import Queue
import threading

q = Queue()

target = "137.74.187.101"

for x in range(1, 500):
    q.put(x)

def portscanner(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((target, port))

        return True
    
    except:
        return False

def worker():
    while True:
        port = q.get()
        if portscanner(port):
            print("Port {} is open". format(port))
        else:
            print("Port {} is closed".format(x))

for x in range(50):
    t = threading.Thread(target= worker)
    t.start()