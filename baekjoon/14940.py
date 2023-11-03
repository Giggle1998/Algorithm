from collections import deque

n, m = map(int, input().split())

arr = []
visited = [[-1] * m for _ in range(n)]
que = deque()

for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            que.append([i, j])
            visited[i][j] = 0
            break
cnt = 0
while que:
    ci, cj = que.popleft()
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni = ci + di
        nj = cj + dj

        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == -1:
            if arr[ni][nj] == 1:
                visited[ni][nj] = visited[ci][cj] + 1
                que.append([ni, nj])
            elif arr[ni][nj] == 0:
                visited[ni][nj] = 0

for i in range(n):
    print(*visited[i])