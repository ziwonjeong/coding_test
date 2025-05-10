# Queue: FIFO (first-in, first-out)
import queue

data_queue = queue.Queue()
data_queue.put(1)
data_queue.put(2)
data_queue.put(3)

print(data_queue.get())
print(data_queue.get())
print(data_queue)


# Priority Queue
data_queue = data_queue.PriorityQueue()
data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.put((15, "china"))

print(data_queue.get())
print(data_queue.get())
print(data_queue.get()) 