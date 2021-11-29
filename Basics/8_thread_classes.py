# alternative way to build threads is to create a class that inherits the Thread class
#This way we can modify the class function

import threading

class MyThread(threading.Thread):

    def __init__(self, message):
        threading.Thread.__init__(self)
        self.message = message

    def run(self):
        for x in range(100):
            print(self.message)

mt1 = MyThread("This is the message!")
mt1.start()