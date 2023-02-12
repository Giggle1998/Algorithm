# dr = 0(하) -1 (좌) 1 (우)

T = 10
for t in range(1, T+1):
    N = int(input())

    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    min_v = 99999999

    for sj in range(1, 101):
        if arr[0][sj] == 0:
            continue
        cj = sj
        dr = cnt = ci = 0
        while ci < 99:
            cnt += 1
            if dr == 0:
                ci += 1
                if arr[ci][cj-1] == 1:
                    dr = -1
                elif arr[ci][cj+1] == 1:
                    dr = 1

            else:
                cj += dr
                if arr[ci][cj+dr] == 0:
                    dr = 0

        if min_v > cnt:
            min_v = cnt
            ans = sj-1


    print(f'#{t} {ans}')
