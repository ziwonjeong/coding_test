# Queue: FIFO (first-in, first-out) 
'''
from collections impore deque VS. import queue VS. list
https://potato-robot.tistory.com/5
- Queue (fifo): deque > list
- Stack (filo): deque = list
'''

from collections import deque

queue = deque()
queue.append(1) # 오른쪽으로 넣기
queue.appendleft(2) # 왼쪽으로 넣기
queue.pop() #오른쪽에서 빼기
queue.popleft() #왼쪽에서 빼기
print(queue)


# Queue
for i in range(5):
    queue.append(i)

print(f"{queue=}")

queue.reverse()
print(queue)