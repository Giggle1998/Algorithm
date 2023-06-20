from collections import deque

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split()) # S초뒤에 X와 Y위치에 있는 바이러스는?
visited = [[0] * N for _ in range(N)]

position = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            position.append((arr[i][j], i, j, 0))

position.sort()
que = deque(position)

while que:
    num, ci, cj, cnt = que.popleft()

    if cnt == S:
        break

    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 0:
                arr[ni][nj] = num
                que.append((num, ni, nj, cnt + 1))

print(arr[X-1][Y-1])

