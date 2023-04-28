from collections import deque

# INF = 10**9
M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
D = [[0]*M for _ in range(N)]
que = deque()
que.append((0, 0))

while que:
    i, j = que.popleft()
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and D[ni][nj] == 0:
            if arr[ni][nj] == 1:
                D[ni][nj] = D[i][j] + 1
                que.append((ni, nj))
            else:
                D[ni][nj] = D[i][j]
                que.appendleft((ni, nj))
print(D[N-1][M-1])



