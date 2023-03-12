N = int(input())
dp = [0] * 1001
'''
1, 3,  
'''
dp[1] = 1
dp[2] = 3
if N > 2:
    for i in range(3, N+1):
        dp[i] = dp[i-1] + 2*dp[i-2]
ans = dp[N] % 10007
print(ans)



