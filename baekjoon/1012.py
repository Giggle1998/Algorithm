import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    global cnt
    que = deque()
    que.append((i, j))

    while que:
        i, j = que.pop()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1:
                arr[ni][nj] = 9
                que.append((ni, nj))
    cnt += 1


T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    # visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        i, j = map(int, input().split())
        arr[i][j] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i, j)

    print(cnt)

