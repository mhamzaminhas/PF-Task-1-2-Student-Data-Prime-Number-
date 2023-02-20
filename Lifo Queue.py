import queue

myQueue = queue.LifoQueue()

myQueue.put(1)
myQueue.put(2)
myQueue.put(3)
myQueue.put(4)

print("Items in the LIFO queue:")
while not myQueue.empty():
    print(myQueue.get())