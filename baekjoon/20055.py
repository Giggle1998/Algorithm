'''
N에서 전환
'''
from collections import deque
N, K = map(int, input().split())
que = deque(map(int, input().split()))
robot = [0] * N
def check():
    cnt = 0
    for q in que:
        if q == 0:
            cnt += 1
        if cnt >= K:
            return False
    return True

time = 0
while check():
    time += 1
    que.rotate(1)

    robot.pop()
    robot = [0] + robot
    robot[-1] = 0

    for i in range(N-1, 0, -1):
        if robot[i] == 0 and que[i] >= 1:
            if robot[i-1] != 0:
                robot[i] = 1
                robot[i - 1] = 0
                que[i] -= 1

    if que[0] != 0:
        robot[0] += 1
        que[0] -= 1

print(time)



