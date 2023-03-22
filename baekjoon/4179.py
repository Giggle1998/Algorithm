from collections import deque

def fire_bfs(que, visited):
    while que:
        si, sj = que.popleft()
        for d in range(len(dr)):
            ni = si + dr[d][0]
            nj = sj + dr[d][1]
            if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == '.' and visited[ni][nj] == 0:
                que.append((ni, nj))
                visited[ni][nj] = visited[si][sj] + 1

def jihun_bfs(que, visited, tmp_visted):
    while que:
        si, sj = que.popleft()
        for d in range(len(dr)):
            ni = si + dr[d][0]
            nj = sj + dr[d][1]
            if not(0 <= ni < R and 0 <= nj < C):
                ans = visited[si][sj]
                return ans
            if visited[ni][nj] or arr[ni][nj] == '#':
                continue
            if tmp_visted[ni][nj] and visited[si][sj] + 1 >= tmp_visted[ni][nj]:
                continue
            # 지훈이의 방문 우선순위가 불보다 더 작으면 이동 가능
            que.append((ni, nj))
            visited[ni][nj] = visited[si][sj] + 1
    return 'IMPOSSIBLE'

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
jihun = deque()
fire = deque()
dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]
j_visited = [[0] * C for _ in range(R)]
f_visited = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'J':
            jihun.append((i,j))
            j_visited[i][j] = 1
        if arr[i][j] == 'F':
            fire.append((i, j))
            f_visited[i][j] = 1
fire_bfs(fire, f_visited)
print(jihun_bfs(jihun, j_visited, f_visited))




