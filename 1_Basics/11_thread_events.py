# Events gives more control over threads
# we can pause a thread and wait for certain event to happen in order to continue it.

import threading

event = threading.Event()

def function():
    print("waiting for event...")
    event.wait()
    print("Continuing!")

thread = threading.Thread(target= function)
thread.start()

x = input("Trigger Event? ")
if(x == "yes" or x == "y"):
    event.set()