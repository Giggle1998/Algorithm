'''
치즈가 모두 녹아서 없어지기전 시간, 치즈 개수 출력
1. bfs 탐색을 통해 치즈 내부 구하기
2. 치즈 내부(0)를 제외하고 0과 마찰한 경우 녹는 치즈 -> 좌표 리스트에 추가
3. 좌표 리스트의 모든 치즈값을 녹이기
4. 치즈가 더이상 없으면 종료
'''
from collections import deque

def bfs(): # 치즈 내부의 공기 찾기
    visited = [[0] * M for _ in range(N)]
    que = deque()
    que.append((0, 0))
    visited[0][0] = 1
    while que:
        ci, cj = que.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                que.append((ni, nj))

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                visited[i][j] = 1

    pos_in = []
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                pos_in.append((i, j))
    return pos_in

def find_pos(): # 녹을 수 있는 치즈 찾기
    pos = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                        if (ni, nj) not in pos_in:
                            pos.append([i, j])
                            break
    return pos

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cnt += 1
time = 0
while 1:
    tmp = 0
    pos_in = bfs()
    pos = find_pos()  # 치즈 좌표

    for i, j in pos: # 동시에 녹이기
        arr[i][j] = 0
    for lst in arr: # 치즈 개수
        tmp += lst.count(1)
    time += 1  # 시간 추가
    if tmp == 0: # 치즈가 더 이상 없으면 종료
        break
    else:
        cnt = tmp
print(time)
print(cnt)

