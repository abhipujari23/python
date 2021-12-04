#if we want to wait for threads to finish before we move on with the code
#we can use join function

import threading

def function1():
    for x in range(1500):
        print("Hello World!")

t1 = threading.Thread(target=function1)
t1.start()

#join accepts number of seconds to wait to run
t1.join(1)
print("This is the end!")