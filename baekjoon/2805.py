import sys
input = sys.stdin.readline   # 시간 초과

N, M = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(min(arr), max(arr)):
    _sum = 0
    for j in range(len(arr)):
        if arr[j] > i:
            _sum += arr[j] - i

    if _sum == M:
        print(i)
        break

