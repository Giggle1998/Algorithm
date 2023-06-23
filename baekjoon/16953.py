def dfs(num, cnt):
    global ans
    # 타겟값보다 크다면 탐색 종료
    if int(num) > int(M):
        return
    # 타겟값과 동일하다면 최소횟수 도출
    if num == M:
        ans = min(ans, cnt)
        return
    # 2를 곱할 수 있는 경우
    dfs(str(int(num)*2), cnt + 1)
    # 문자열 끝에 1을 더할 수 있는 경우
    dfs(num+'1', cnt + 1)

N, M = map(str, input().split())

ans = 10**9
dfs(N, 1)
if ans == 10**9:
    print(-1)
else:
    print(ans)

