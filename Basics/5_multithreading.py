# Threads are lightweight processes
# they are a small part of program
# threads can work in parallel as two application
# as they are in same process they share memory space for variable and data, can exchange information
# and communicate efficiently
# these are lightweight process as need less resource than processes

# sleep: it puts the thread on hold

# thread types:
#  Kernal Threads: part of OS
#  User Threads: managed by programmer

#to start thread we need to import it
import threading

#define target function for thread

def Hello():
    print("Hello World!")
              #Thread is used to create the thread
t1 = threading.Thread(target = Hello)
t1.start()