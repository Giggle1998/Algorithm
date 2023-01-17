T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(T):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    i, j, cnt, dr = 0, 0, 1, 0
    arr[i][j] = cnt
    cnt += 1
    while cnt <= n**2:
        ni, nj = i + di[dr], j + dj[dr]
        if 0<=ni<n and 0<=nj<n and arr[ni][nj] == 0:
            i, j = ni, nj
            arr[i][j] = cnt
            cnt += 1
        else:
            dr = (dr+1)%4

    print(f'#{t+1}')
    for lst in arr:
        print(*lst)