#daemon thread run in background, program can be terminated if the thread is still running
#Used for background tasks like synchronizing, loading or cleaning files

from os import read
import threading
import time
from typing import Text

path = "12_text.txt"
text = ""

def readFile():
    global path, text

    while True:
        with open(path) as file:
            text = file.read()
            time.sleep(3)

def printloop():
    global text

    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target= readFile, daemon= True)
t2 = threading.Thread(target= printloop)

t1.start()
t2.start()
