import heapq, sys
input = sys.stdin.readline

INF = 987654321
def dijkstra(s, e):
    D = [INF] * (N + 1)
    heap = []
    D[s] = 0
    heapq.heappush(heap, (0, s))

    while heap:
        dist, node = heapq.heappop(heap)
        if D[node] < dist: # 거리가 더 큰 경우는 넘어감
            continue
        if D[node] > dist: # 거리가 작다면 거리 갱신
            D[node] = dist
        for v, w in graph[node]:
            if D[v] > dist + w:
                D[v] = dist + w # 거리 갱신
                heapq.heappush(heap, (D[v], v))

    return D[e]

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))

ans = 0
for num in range(1, N + 1):
    go = dijkstra(num, X) # 파티 갈 때
    back = dijkstra(X, num) # 파티 돌아올 때
    ans = max(ans, go+back)
print(ans)


