from collections import deque
# 다익스트라를 통해 최단 경로 탐색
def bfs(i, j):
    D[i][j] = 0
    que = deque()
    que.append((i, j))
    while que:
        x, y = que.popleft()
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if D[nx][ny] > D[x][y] + arr[nx][ny]:
                    D[nx][ny] = D[x][y] + arr[nx][ny]
                    que.append((nx, ny))
INF = 987654321
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    D = [[INF]*N for _ in range(N)]
    min_v = 10**9
    bfs(0, 0)
    print(f'#{t} {D[N-1][N-1]}')