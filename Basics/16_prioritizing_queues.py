#we can provide priority to queue by assiging a level that determines when will it leave the queue

import queue

q = queue.PriorityQueue()

q.put((8, "Some Text"))
q.put((1, 95))
q.put((900, "Hello World"))
q.put((10, "EOF"))

while not q.empty():
    print(q.get())