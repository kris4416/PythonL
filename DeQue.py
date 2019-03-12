from collections import deque

queue = deque(range(10))

queue = deque(range(10), maxlen=10)

queue.append('A')
queue.appendleft('A')

print(queue)

queue.pop()

print(queue)

queue.popleft()

print(queue)

queue.insert(2, 'A')

print(queue)

queue.reverse()

print(queue)

queue.clear()

print(queue)