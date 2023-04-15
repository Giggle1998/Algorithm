'''
DP를 활용해 이전의 값들과 비교해 
가장 긴 증가하는 부분 수열의 길이를 찾는다.
'''
N = int(input())
lst = list(map(int, input().split()))

dp = [1] * N
for i in range(1, N):
    for j in range(0, i):
        #이전값이 작은 경우 LIS 길이 갱신
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))