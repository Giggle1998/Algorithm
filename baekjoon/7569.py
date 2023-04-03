'''
하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
여섯 방향에 있는 토마토를 의미한다.
'''
from collections import deque

def find_pos(tomato): # 토마토 위치 찾기
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomato[z][y][x] == 1:
                    # 3차원 좌표
                    que.append((z, y, x))

def bfs(que): # 3차원 BFS 탐색 진행
    while que:
        z, y, x = que.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if tomas[nz][ny][nx] == 0:
                    que.append((nz,ny,nx))
                    tomas[nz][ny][nx] = tomas[z][y][x] + 1

def find_ans(tomato): # 정답 찾기 / 안익은 토마토가 남아있다면 -1 반환
    global ans
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomato[z][y][x] == 0:
                    return False
                ans = max(ans, tomato[z][y][x])
    return True
M, N, H = map(int, input().split())
tomas = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
que = deque()
find_pos(tomas)
# 3차원 델타 이동
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
bfs(que)
ans = 0
rst = find_ans(tomas)
if rst:
    print(ans-1)
else:
    print(-1)


