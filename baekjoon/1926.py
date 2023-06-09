from collections import deque
def bfs(i, j):
    que = deque()
    que.append([i, j])
    visited[i][j] = 1
    rst = 1 # 넓이

    while que:
        ci, cj = que.popleft()

        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    rst += 1
                    que.append([ni, nj])

    return rst

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

cnt = 0
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            rst = bfs(i, j)
            cnt += 1
            ans = max(ans, rst)

print(cnt)
print(ans)

