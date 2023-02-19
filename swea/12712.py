T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    di_1 = [0, 1, 0, -1]
    dj_1 = [1, 0, -1, 0]
    di_2 = [1, 1, -1, -1]
    dj_2 = [1, -1, -1, 1]

    max_sum = -1
    for i in range(N):
        for j in range(N):
            _sum = arr[i][j]
            for k in range(4):
                for mul in range(1, M):
                    ni = i + di_1[k] * mul
                    nj = j + dj_1[k] * mul
                    if 0 <= ni < N and 0 <= nj < N:
                        _sum += arr[ni][nj]
            if max_sum < _sum:
                max_sum = _sum

    for i in range(N):
        for j in range(N):
            _sum = arr[i][j]
            for k in range(4):
                for mul in range(1, M):
                    ni = i + di_2[k] * mul
                    nj = j + dj_2[k] * mul
                    if 0 <= ni < N and 0 <= nj < N:
                        _sum += arr[ni][nj]
            if max_sum < _sum:
                max_sum = _sum

    print(f'#{t} {max_sum}')