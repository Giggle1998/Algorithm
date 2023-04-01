def dfs(n, cnt, cur, x, y):
    global max_v
    if cnt > C:
        return
    if n == M: # 해당 깊이에 도달하면 최대값 반환
        max_v = max(max_v, cur)
        return

    # 하단 호출 : 깊이, 합, 곱, 좌표
    dfs(n+1, cnt+arr[x][y+n], cur+arr[x][y+n]**2, x, y)
    dfs(n+1, cnt, cur, x, y)

T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    # 1번 채취자
    for i in range(N):
        for j in range(N-M+1):
            max_v = 0
            # 백트래킹 진행
            dfs(0, 0, 0, i, j)
            fst = max_v
            # 2번 채취자
            for p in range(i, N):
                tmp = j+M if i==p else 0
                for q in range(tmp, N-M+1):
                    max_v = 0
                    # 백트래킹 진행
                    dfs(0, 0, 0, p, q)
                    ans = max(ans, fst+max_v)
    print(f'#{t} {ans}')





