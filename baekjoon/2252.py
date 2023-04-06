from collections import deque

def topology_sort(): # 위상정렬 진행
    que = deque()
    # 초기 세팅
    for i in range(1, N+1):
        if degree[i] == 0: # 진입차수가 0인 값들을 enQ
            que.append(i)

    while que:
        v = que.popleft()
        print(v, end=' ')
        for w in graph[v]:
            # 진입차수를 감소시키고 0일 경우 enQ
            degree[w] -= 1 
            if degree[w] == 0:
                que.append(w)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    degree[v2] += 1 # 진입차수 카운트
topology_sort()