n = 8
str1 = "BWBWBWBW"
str2 = 'WBWBWBWB'
pivot1 = [str1, str2, str1, str2, str1, str2, str1, str2]
pivot2 = [str2, str1, str2, str1, str2, str1, str2, str1]
def solve():
    N, M = [int(x) for x in input().split()]
    board = []
    for i in range(N):
        board.append(input())
    result = float('inf')
    for i in range(N-n+1):
        for j in range(M-n+1):
            cnt = 0
            for p in range(n):
                for q in range(n):
                    if board[i+p][i+q] != pivot1[p][q]:
                        cnt += 1
            result = min(result, cnt)
            cnt = 0
            for p in range(n):
                for q in range(n):
                    if board[i+p][i+q] != pivot2[p][q]:
                        cnt += 1
            result = min(result, cnt)

    print(result)

solve()

            

