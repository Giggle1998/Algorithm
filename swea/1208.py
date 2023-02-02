T = 10

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):

        max_v = -1
        min_v = 99999999

        max_i = min_i = 0

        for i in range(len(arr)):

            if max_v < arr[i]:
                max_v = arr[i]
                max_i = i

            if min_v > arr[i]:
                min_v = arr[i]
                min_i = i

        arr[max_i] -= 1
        arr[min_i] += 1

    max_v = -1
    min_v = 99999999

    for i in range(len(arr)):
        if max_v < arr[i]:
            max_v = arr[i]

        if min_v > arr[i]:
            min_v = arr[i]

    print(f'#{t} {max_v - min_v}')

