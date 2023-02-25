def bfs(i, j, C):
    que = []
    que.append((i, j))
    visited[i][j] = 1

    while que:
        si, sj = que.pop(0)
        for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
            ni = si + di
            nj = sj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == C and visited[ni][nj] == 0:
                que.append((ni, nj))
                visited[ni][nj] = 1

before_cnt = 0
after_cnt = 0
N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for i in range(N): # before 적록색약
    for j in range(N):
        if arr[i][j] == 'R' and visited[i][j] == 0:
            bfs(i, j, 'R')
            before_cnt += 1
        elif arr[i][j] == 'G' and visited[i][j] == 0:
            bfs(i, j, 'G')
            before_cnt += 1
        elif arr[i][j] == 'B' and visited[i][j] == 0:
            bfs(i, j, 'B')
            before_cnt += 1

        if arr[i][j] == 'G': arr[i][j] = 'R' # 적록색약

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R' and visited[i][j] == 0:
            bfs(i, j, 'R')
            after_cnt += 1
        elif arr[i][j] == 'B' and visited[i][j] == 0:
            bfs(i, j, 'B')
            after_cnt += 1

print(before_cnt, after_cnt)



