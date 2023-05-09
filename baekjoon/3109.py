'''
각 칸은 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선으로
연결할 수 있고 각 칸의 중심끼리 연결
'''
def dfs(i, j):
    global cnt
    if j == C-1:
        cnt += 1
        return True

    for di, dj in ((-1, 1), (0, 1), (1, 1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0:
            if arr[ni][nj] == '.':
                visited[ni][nj] = 1
                if dfs(ni, nj):
                    return True

R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]

cnt = 0
visited = [[0]*C for _ in range(R)]
for r in range(R):
    if arr[r][0] == '.':
        dfs(r, 0)
print(cnt)