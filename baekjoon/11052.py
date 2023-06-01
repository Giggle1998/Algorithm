'''
DP로 접근하여 1 ~ N 까지 탐색하며
해당 인덱스에서 N개의 합이 되는 경우의 최대 금액을 갱신한다.
'''
N = int(input())
cost = [0]
tmp = list(map(int, input().split()))
cost.extend(tmp)

dp = [0] * (N+1)
for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], cost[j]+dp[i-j])
print(max(dp))