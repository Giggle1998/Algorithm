N = int(input())
arr = []
for _ in range(N):
    L, H = map(int, input().split())
    arr.append([L,H])
arr.sort(key=lambda x : x[0])

max_idx = arr.index(max(arr, key=lambda x : x[1])) # 가장 큰 기둥 인덱스

before_h = arr[0][1]
ans = 0
for i in range(max_idx):
    if before_h < arr[i+1][1]:
        ans += (arr[i+1][0] - arr[i][0]) * before_h
        before_h = arr[i+1][1]
    else:
        ans += (arr[i+1][0] - arr[i][0]) * before_h

after_h = arr[-1][1]
for i in range(N-1, max_idx, -1):
    if after_h < arr[i-1][1]:
        ans += (arr[i][0] - arr[i-1][0]) * after_h
        after_h = arr[i-1][1]
    else:
        ans += (arr[i][0] - arr[i-1][0]) * after_h
ans += max(arr, key=lambda x : x[1])[1]

print(ans)