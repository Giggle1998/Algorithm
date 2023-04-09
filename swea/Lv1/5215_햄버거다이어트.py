def dfs(k, score, cal):
    global ans
    # 칼로리를 넘어가면 종료
    if cal > L:
        return
    # 정답 갱신
    if ans < score:
        ans = score

    if k == N:
        return
    # 먹을 수 있는 경우와 없는 경우
    dfs(k + 1, score + arr[k][0], cal + arr[k][1])
    dfs(k + 1, score, cal)


T = int(input())
for t in range(1, T+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    dfs(0, 0, 0)
    print(f'#{t} {ans}')