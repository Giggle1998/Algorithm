'''
방문한 정점은 체크하여 BFS 그래프 탐색 진행
'''
from collections import deque
import sys
input = sys.stdin.readline

def bfs(i):
    que = deque([i])
    visited[i] = 1

    while que:
        g = que.popleft()
        for v in graph[g]:
            if visited[v] == 0:
                visited[v] = 1
                que.append(v)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1
print(cnt)

