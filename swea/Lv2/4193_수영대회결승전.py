'''
즉, 시간을 기점으로 (Time % 3 == 2)일 경우 길이 생기게 된다. 이 경우 이동할 수 있게 된다
따라서 기존의 4방탐색과 달리, '기다린다'는 선택지를 추가해야 했다. 그렇기에 이동 배열에 {0, 0}을 추가하였다.
'''
from collections import deque
def bfs(si, sj):
    que = deque()
    que.append((si, sj, 0))

    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1
    while que:
        i, j, time = que.popleft()
        if i == ei and j == ej:
            return time
        for di, dj in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                # 방문 체크가 되었고 제자리인 경우
                if visited[ni][nj] == 1 and i==ni and j==nj:
                    que.append((ni, nj, time+1))
                if visited[ni][nj] == 0:
                    # 소용돌이를 만난경우와 일반 경로인 경우
                    if (time % 3 == 2 and arr[ni][nj] == 2) or arr[ni][nj] == 0:
                        visited[ni][nj] = 1
                        que.append((ni, nj, time+1))

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    ans = bfs(si, sj)
    print(f'#{t} {ans}')



