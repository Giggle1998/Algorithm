import sys
input = sys.stdin.readline
N, K = map(int, input().split())

arr = [[0,0]]
for _ in range(N):
    W, V = map(int, input().split())
    arr.append([W, V])

# arr.sort(key = lambda x: x[1]) # 재홍님 반례
max_v = 0
cnt = 1

while cnt != N+1:
    dp = [[0, 0] for i in range(N + 1)]  # 이중 리스트로 dp 생성
    for i in range(cnt, N+1):
        dp[i][0] = arr[i][0]
        # print('무게 합', dp[i][0] + dp[i-1][0])
        if dp[i][0] + dp[i-1][0] <= K: # dp에 누적
            dp[i][0] += dp[i-1][0]
            dp[i][1] = dp[i-1][1] + arr[i][1]
        else:
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][1]

        if max_v < dp[i][1]: # 최대 가치 저장
            max_v = dp[i][1]
    # print('dp', dp)
    # print('cnt:', cnt)
    cnt += 1

print(max_v)





