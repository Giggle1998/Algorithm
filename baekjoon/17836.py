'''
1. BFS 탐색을 통해 0인 경우 이동, 좌표와 이동 시간을 큐에 추가
2. 2를 만난 경우를 체크할 수 있도록 큐에 추가
3. 1을 만난 경우는 2의 변수가 존재하는 경우에만 이동하도록
4. N-1, M-1에 도달한 경우 종료
+ 칼을 사용하지 않은 경우가 최소 경로인 경우도 존재,
'''
from collections import deque

def bfs():
    que = deque()
    que.append([0, 0, 0]) # 좌표, 이동시간

    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    ans = 10**9
    while que:
        ci, cj, time= que.popleft()

        if time > T: # 시간을 초과한 경우 종료
            break

        if (ci, cj) == (N-1, M-1): # 목적지에 도달하면 정답 갱신
            ans = min(ans, time)
            break

        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if arr[ni][nj] == 0: # 칼을 사용하지 않는 경우
                    visited[ni][nj] = 1
                    que.append([ni, nj, time+1])

                elif arr[ni][nj] == 2: # 칼을 사용하는 경우
                    visited[ni][nj] = 1
                    rst = abs(N-1-ni) + abs(M-1-nj) + time + 1
                    if rst <= T:
                        ans = rst

    if ans > T: # 시간을 초과한 경우 실패
        return 'Fail'
    return ans

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(bfs())

