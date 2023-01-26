N, M = map(int, input().split())

board = []
cnt = 0
for i in range(N):
    board.append(input())

board_t = list(zip(*board))

print(board)
print(board_t)        

# 8*8 check
B = 0
W = 0
range_board = len(board) - 7
for i in range(range_board):
    for j in range(N):
        if board[j][i:8+i]:
            B = board[j][i:8+i].count('B')
            W = board[j][i:8+i].count('W')
            



# for b in board:
#     for i in range(N-1):
#         if b[i] == 'B':
#             if b[i+1] == 'W':
#                 pass
#             else:
#                 cnt += 1
#             pass
#         elif b[i] == 'W':
#             if b[i+1] == 'B':
#                 pass
#             else:
#                 cnt += 1
            

