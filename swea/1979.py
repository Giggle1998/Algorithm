T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(zip(*arr))

    ans = 0
    for i in range(N):
        cnt_w = 0
        cnt_h = 0
        for j in range(N):
            if arr[i][j]: # 가로
                cnt_w += 1
            else:
                if cnt_w == M:
                    ans += 1
                cnt_w = 0

            if arr[j][i]:
                cnt_h += 1
            else:
                if cnt_h == M:
                    ans += 1
                cnt_h = 0


    print(f'#{t} {ans}')

