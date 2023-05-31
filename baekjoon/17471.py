'''
먼저 DFS를 활용해 두 그룹으로 나눠줍니다.
그 후 나눠준 두 그룹에 대해 BFS 탐색을 한다.
BFS 탐색을 한 후 그룹 내 구역만큼 탐색했다면 인구수를 반환한다.
반환한 인구수를 통해 최솟값을 도출한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(group):
    que = deque()
    check = [False] * N
    que.append(group[0])
    check[group[0]] = True

    cnt = 1
    ans = 0
    while que:
        g = que.popleft()
        ans += p_lst[g]
        for tmp in arr[g]:
            if tmp in group and not check[tmp]:
                check[tmp] = True
                cnt += 1
                que.append(tmp)

    if cnt == len(group):
        return ans
    else:
        return

def dfs(depth, start, end):
    global min_v

    if depth == end:
        group1 = []
        group2 = []
        for i in range(N):
            if visited[i]:
                group1.append(i)
            else:
                group2.append(i)

        rst1 = bfs(group1)
        if not rst1:
            return
        rst2 = bfs(group2)
        if not rst2:
            return

        min_v = min(min_v, abs(rst1-rst2))
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i, end)
            visited[i] = False


N = int(input())
p_lst = list(map(int, input().split()))
arr = [[] for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    for t in tmp[1:]:
        arr[i].append(t-1)

min_v = 10**9
for i in range(1, N//2+1):
    visited = [False] * N
    dfs(0, 0, i)

if min_v == 10**9:
    print(-1)
else:
    print(min_v)
