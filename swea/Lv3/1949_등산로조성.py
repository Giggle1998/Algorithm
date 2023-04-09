def dfs(i, j, check, cnt):
    global ans
    # 정답 갱신
    if ans < cnt: ans = cnt

    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj]==0:

            # 다음 봉우리가 낮은 경우
            if arr[i][j] > arr[ni][nj]:
                visited[ni][nj] =  1
                dfs(ni, nj, check, cnt+1)
                visited[ni][nj] =  0

            # 다음 봉우리가 같거나 높은 경우
            if arr[i][j] <= arr[ni][nj] and check == 0:
                # 최대 깊이 만큼 봉우리 깎기
                for k in range(1, K+1):
                    arr[ni][nj] -= k # 봉우리 깎기
                    if arr[ni][nj] < arr[i][j]:
                        visited[ni][nj] = 1
                        check = 1 # 봉우리 깎은 것을 체크
                        dfs(ni, nj, check, cnt+1)
                        check = 0 # 체크 해제
                        visited[ni][nj] = 0
                    arr[ni][nj] += k # 봉우리 원상태

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for lst in arr:
        max_v = max(max(lst), max_v)

    ans = 0
    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]
            # 최고 높이인 경우 탐색 시작
            if arr[i][j] == max_v:
                visited[i][j] = 1
                dfs(i, j, 0, 1)

    print(f'#{t} {ans}')

