# Difference in Run and Start
# Run function executes threads serially one after other
# Start function starts all the thready simultaneously

import threading

def function1():
    for x in range(1000):
        print("One")

def function2():
    for x in range(1000):
        print("Two")

t1 = threading.Thread(target= function1)
t2 = threading.Thread(target= function2)

#remove/add # to see the difference

#using start function
#t1.start()
#t2.start()

#using run function
t1.run()
t2.run()