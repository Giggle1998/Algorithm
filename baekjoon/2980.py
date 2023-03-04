from collections import deque
N, L = map(int, input().split())

# D R G
arr = deque(list(map(int, input().split())) for _ in range(N))
cnt = 0
for i in range(1, L+1):
    cnt += 1
    if arr:
        if arr[0][0] == i:
            cnt += max(0, arr[0][1] - cnt % (arr[0][1]+arr[0][2]))
            arr.popleft()
print(cnt)