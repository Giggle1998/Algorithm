import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, max(arr)

ans = 0
while start <= end:

    mid = (start + end) // 2
    cnt = 0
    for tree in arr:
        if tree > mid:
            cnt += tree - mid

    if cnt < M:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)


