T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    cnt = 0
    tmp = list(range(arr[0][0], arr[0][1]))
    for i in range(len(arr)):
        if arr[i][0] in tmp or arr[i][1] in tmp:
            cnt += 1
            tmp = list(range(arr[i][0], arr[i][1]))

    print(f'#{t} {cnt}')
