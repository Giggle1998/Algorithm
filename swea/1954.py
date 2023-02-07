T = int(input())

for t in range(T):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    i = j = 0
    cnt = 1
    d = 0

    arr[i][j] = cnt
    cnt += 1

    di = [0, -1, 0, 1]
    dj = [-1, 0, 1, 0]

    while cnt != n**2+1:
        ni, nj = i + di[d], j + dj[d]
        if 0<=ni<n and 0<=nj<n and arr[ni][nj] == 0:
            i, j = ni, nj
            arr[i][j] = cnt
            cnt += 1
        else:
            d = (d+1)%4

    print(f'#{t+1}')
    for lst in arr:
        print(*lst)