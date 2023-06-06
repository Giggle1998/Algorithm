'''
맥주 한 박스 = 맥주 20개
50m에 한 병씩
상근이네 집, 편의점, 페스티벌 좌표

1. bfs 탐색을 통해 페스티벌을 도착할 수 있는 경로를 탐색
2. 집 좌표를 큐에 push
3. 주어진 모든 편의점 좌표를 탐색하며 가능한 경우에 큐에 push
4. 큐에서 pop된 좌표 중 페스티벌 좌표에 도달할 수 있으면 happy
'''
from collections import deque
import sys

input = sys.stdin.readline

def bfs(i, j, x, y):
    que = deque()
    visited = [0] * N
    que.append([i, j])
    while que:
        ci, cj = que.popleft()
        # 페스티벌에 도착할 수 있는 경우
        if abs(x-ci) + abs(y-cj) <= 1000:
            return 'happy'
        for i in range(N):
            if visited[i] == 0:
                ni, nj = arr[i]
                # 이동가능 한 편의점인 경우
                if abs(ci-ni) + abs(cj-nj) <= 1000:
                    que.append([ni, nj])
                    visited[i] = 1
    # 페스티벌에 도착 못 하는 경우
    return 'sad'

T = int(input())
for _ in range(T):
    N = int(input())
    hx, hy = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    fx, fy = map(int, input().split())

    ans = bfs(hx, hy, fx, fy)
    print(ans)
