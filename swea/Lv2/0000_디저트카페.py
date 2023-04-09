'''
완전 탐색, 백트래킹 / 꺾이는 횟수를 depth로 사용
'''

dr = [(1, -1), (1, 1), (-1, 1), (-1, -1)]

def dfs(n, si, sj, visited):
    global ans
    # 3번 이상 꺾이면 종료
    if n > 3:
        return
    # 정답 조건
    if n == 3 and i==si and j==sj and len(visited) > 2:
        ans = max(ans, len(visited))
        return

    # 중복처리 확인
    if 0 <= si < N and 0 <= sj < N and arr[si][sj] not in visited:
        n_visited = visited + [arr[si][sj]]

        # 직진하는 경우
        ni, nj = si + dr[n][0], sj + dr[n][1]
        dfs(n, ni, nj, n_visited)

        # 꺾어서 갈 수 있는 경우
        if n < 3:
            ni, nj = si + dr[n+1][0], sj + dr[n+1][1]
            dfs(n+1, ni, nj, n_visited)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = -1
    # 대각 회전을 할 수 있도록 범위 조정
    for i in range(N-2):
        for j in range(1, N-1):
            dfs(0, i, j, [])
    print(f'#{t} {ans}')