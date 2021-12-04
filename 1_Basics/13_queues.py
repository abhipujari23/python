#Queue takes data in certain order and output it is the same order
#FIFO Queue: First In First Out

import queue

q = queue.Queue()

for x in range(5):
    q.put(x)

for x in range(5):
    print(q.get(x))
