N, M, K = map(int, input().split())

def search(n, m):
    dp = [[0] * (m+1)] * (n+1)

    for i in range(1, n+1):
        for j in range(1, m+1):
            # 첫 위치의 경우는 1
            if i == 1 and j == 1:
                dp[i][j] = 1
            # 아래와 오른쪽으로 이동하는 두 가지 경우를 합하기
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[n][m]

if K:
    # n1, m1은 K까지 이동할 수 있는 모든 경로를 탐색
    n1 = (K-1)//M + 1
    m1 = K - (n1 - 1) * M
    # n2, m2은 K에서 마지막까지 이동할 수 있는 모든 경로를 탐색
    n2 = N - (n1 - 1)
    m2 = M - (m1 - 1)
    rst1 = search(n1, m1)
    rst2 = search(n2, m2)
    # 모든 경우의
    print(rst1 * rst2)
# K가 0인 경우는 N부터 M까지의 모든 경로를 탐색
else:
    print(search(N, M))
