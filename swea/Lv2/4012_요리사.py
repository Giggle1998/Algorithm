def check(tmp_arr): # 요리의 조합
    rst = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            rst += arr[tmp_arr[i]][tmp_arr[j]] + arr[tmp_arr[j]][tmp_arr[i]]
    return rst


def comb(k, s):
    global ans
    if k == N//2:
        front = []
        back = []
        # 절반으로 나누어 진행
        for i in range(N):
            # 조합에 있는 경우
            if visited[i]:
                front.append(i)
            # 조합에 없는 경우
            else:
                back.append(i)
        front_rst = check(front)
        back_rst = check(back)
        ans = min(ans, abs(front_rst - back_rst))
        return

    for i in range(s, N):
        if visited[i] == 0:
            visited[i] = 1
            comb(k+1, i+1)
            visited[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 10**9
    comb(0, 0)
    print(f'#{t} {ans}')
