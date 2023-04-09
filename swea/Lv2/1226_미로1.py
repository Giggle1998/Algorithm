def dfs(i, j):
    global ans
    if arr[i][j] == 3:
        ans = 1
        return 1
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni = i + di
        nj = j + dj
        # 길이거나 도착지인 경우 통과
        if 0 <= ni < 16 and 0 <= nj < 16 and visited[ni][nj] == 0 and (arr[ni][nj] == 0 and arr[ni][nj] == 3):
            visited[ni][nj] = 1
            dfs(ni, nj)

T = 10
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    si, sj = 0, 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                si, sj = i, j
    visited[si][sj] = 1
    ans = 0
    dfs(si, sj)
    print(f'#{N} {ans}')
