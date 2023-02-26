import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6+1)

def find_parent(v):
    for i in graph[v]:
        if v in graph[i] and visited[i] == 0:
            visited[i] = v
            find_parent(i)

V = int(input())
graph = [[] for _ in range(V+1)]
visited = [0] * (V+1)
for _ in range(V-1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
find_parent(1)
for i in range(2, V+1):
    print(visited[i])