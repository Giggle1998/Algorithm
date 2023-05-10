from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    que = deque() # 좌표, 부순 횟수
    que.append([0, 0, 0])
    visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    while que:
        i, j, cnt = que.popleft()
        if i == N-1 and j == M-1:
            return visited[i][j][cnt]

        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj][cnt] == 0:

                if arr[ni][nj] == 1 and cnt+1 <= K:
                    visited[ni][nj][cnt+1] = visited[i][j][cnt] + 1
                    que.append([ni, nj, cnt+1])

                elif arr[ni][nj] == 0:
                    visited[ni][nj][cnt] = visited[i][j][cnt] + 1
                    que.append([ni, nj, cnt])

    return -1

N, M, K = map(int, input().rstrip().split())

arr = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs())