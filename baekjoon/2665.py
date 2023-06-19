import heapq

def bfs():
    heap = []
    visited = [[0]*N for _ in range(N)]
    # 힙에 변경횟수, x좌표, y좌표 순으로 push
    heapq.heappush(heap, (0, 0, 0))
    visited[0][0] = 1
    while heap:
        # 변경횟수가 가장 낮은 x, y좌표를 활용해 탐색 진행
        cnt, ci, cj = heapq.heappop(heap)
        if (ci, cj) == (N-1, N-1):
            return cnt
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if arr[ni][nj] == 1:
                    visited[ni][nj] = 1
                    heapq.heappush(heap, (cnt, ni, nj))
                elif arr[ni][nj] == 0:
                    visited[ni][nj] = 1
                    heapq.heappush(heap, (cnt+1, ni, nj))

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
print(bfs())