T = int(input())
for t in range(1, T+1):
    N, Q = map(int, input().split())

    box = [0] * (N+1)
    arr = [list(map(int, input().split())) for _ in range(Q)]

    for i in range(Q):
        for j in range(arr[i][0], arr[i][1]+1):
            box[j] = i+1
    print(f'#{t}', *box[1:])
