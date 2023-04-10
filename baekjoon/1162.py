import heapq, sys
input = sys.stdin.readline

def dijkstra(s):
    heap = []
    # 노드 가중치 포장횟수
    heapq.heappush(heap, (s, 0, 0))
    D[s] = [0 for _ in range(K+1)]
    while heap:
        node, dist, cnt = heapq.heappop(heap)
        if D[node][cnt] < dist:
            continue
        if node == N:
            return
        for v, w in graph[node]:
            if D[v][cnt] > dist + w:
                D[v][cnt] = dist + w
                heapq.heappush(heap, (v, D[v][cnt], cnt))

            if cnt+1 <= K:
                if dist < D[v][cnt+1]:
                    D[v][cnt + 1] = dist
                    heapq.heappush(heap, (v, D[v][cnt + 1], cnt+1))


INF = 987654321
N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
D = [[INF] * (K+1) for _ in range(N+1)]
for _ in range(M):
    v1, v2, w = map(int, input().split())
    # 양방향
    graph[v1].append([v2, w])
    graph[v2].append([v1, w])

dijkstra(1)
print(min(D[-1]))
