'''
[0][0] ~ [N-1][N-1]까지 이동 한 번에 상하좌우 인접한 곳으로 1칸씩 이동할 수 있다.
링크가 잃을 수밖에 없는 최소 금액은 얼마일까?
1. 상하좌우 델타 이동을 통해 BFS 탐색
2. 다익스트라 알고리즘을 활용해 방문 체크 대신 금액 비교로 탐색 진행
'''
from collections import deque

def dijkstra(i, j):
    que = deque()
    D[i][j] = arr[i][j]

    que.append((i, j))

    while que:
        i, j = que.popleft()
        # 도착점에 도달해도 바로 종료하지 말 것
        # 최소 금액을 찾기 위해서는 마지막까지 탐색 진행
        if (i, j) == (N-1, N-1):
            continue
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                # 현재까지 잃은 비용과 현재 비용의 합보다 작은 경우 금액 갱신
                if D[ni][nj] > D[i][j] + arr[ni][nj]:
                    D[ni][nj] = D[i][j] + arr[ni][nj]
                    que.append((ni, nj))

INF = 10**9
T = 0
while 1:
    N = int(input())
    T += 1
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[INF]*N for _ in range(N)]
    # 0, 0에서 탐색 시작
    dijkstra(0, 0)
    print(f'Problem {T}: {D[N-1][N-1]}')
