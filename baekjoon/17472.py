from collections import deque
import sys
input = sys.stdin.readline
def bfs(i, j, tmp): # 섬 찾기
    que = deque()
    que.append((i, j))
    visited[i][j] = 1
    arr[i][j] = tmp
    land_li.append((i, j, tmp))
    while que:
        i, j = que.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                visited[ni][nj] = 1
                arr[ni][nj] = tmp
                land_li.append((ni, nj, tmp))
                que.append((ni, nj))

def make_node(): # 다리 만들기
    for i, j, num in land_li:
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dist = 0  # 최소 거리
            end = 0
            ni, nj = i + di, j + dj
            while 1: # 다리 놓기
                if not(0 <= ni < N and 0 <= nj < M): # 범위내에 없으면 종료
                    break
                if arr[ni][nj] == 0:
                    ni += di
                    nj += dj
                    dist += 1
                else:
                    if arr[ni][nj] == num: # 같은 섬에 위치
                        break
                    else: # 다른 섬 이동했으면 종료
                        end = arr[ni][nj]
                        break
            if dist < 2:
                continue
            else:
                if end != 0:
                    dist_li.append((num, end, dist))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
land_li = []
dist_li = []
tmp = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and arr[i][j] == 1:
            tmp += 1
            bfs(i, j, tmp)
make_node()

dist_li = list(set(dist_li))
dist_li.sort(key=lambda x: x[2])

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

parent = [i for i in range(tmp+1)]

result = 0
cnt = 0
for v1, v2, cost in dist_li:
    if find(parent, v1) != find(parent, v2):
        cnt += 1
        union(parent, v1, v2)
        result += cost

if result == 0 or cnt != tmp-1:
    print(-1)
else:
    print(result)