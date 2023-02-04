import sys
input = sys.stdin.readline

T = int(input())

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for _ in range(T):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)

    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1)

    ans = -1
    for true in visited:
        if true == True:
            ans += 1

    print(ans)


