'''
-1은 익지않은 토마토
'''
import sys
from collections import deque
input = sys.stdin.readline
def bfs():
    while q:
        si, sj = q.popleft()
        for di, dj in ((1,0), (0,1), (-1,0), (0,-1)):
            ni = si + di
            nj = sj + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0:
                    arr[ni][nj] = arr[si][sj] + 1
                    q.append((ni, nj))

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i,j))
bfs()

flag = 0
for lst in arr:
    if lst.count(0):
        flag = 1 # 안 익은 토마토 존재
        break

ans = 0
for lst in arr:
    ans = max(ans, max(lst))

if flag:
    print(-1)
else:
    print(ans-1) # 처음 위치 포함
