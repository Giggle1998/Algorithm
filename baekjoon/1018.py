n = 8
N, M = map(int, input().split())
board = []
result = []
for i in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        white_cnt = 0
        black_cnt = 0
        for p in range(i, n+i):
            for q in range(j, n+j):
                if (p+q) % 2 == 0:
                    if board[p][q] != 'W':
                        white_cnt += 1
                    if board[p][q] != 'B':
                        black_cnt += 1
                else:
                    if board[p][q] != 'W':
                        black_cnt += 1
                    if board[p][q] != 'B':
                        white_cnt += 1

        result.append(white_cnt)
        result.append(black_cnt)

print(min(result))





