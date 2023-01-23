from collections import deque

card = int(input())
q = deque(range(1, card+1))

while len(q) != 1:
    q.popleft()
    q.append(q[0])
    q.popleft()

print(q[0])
