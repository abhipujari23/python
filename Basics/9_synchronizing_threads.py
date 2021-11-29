#in order to prevent locking i.e One thread is locking all other thread and they can only work when
#the lock is removed Syncing is used

import threading
import time

x = 8192
#lock makes sure the one function is completed before starting other
#to check the difference add # next to all lock eg. #lock.aquire() #lock.release() and run
lock = threading.Lock()

def halve():
    global x, lock
    lock.acquire()
    while(x > 1):
        x /= 2
        print(x)
        time.sleep(1)
    print("End!")
    lock.release()

def double():
    global x, lock
    lock.acquire()
    while(x < 16384):
        x *= 2
        print(x)
        time.sleep(1)
    print("End!")
    lock.release()

t1 = threading.Thread(target= halve)
t2 = threading.Thread(target= double)

t1.start()
t2.start()