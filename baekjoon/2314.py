'''
글자 사이의 간선을 통해 수평, 수직 두 가지 방향에서 문자가 다른 경우 자리를 교환해줍니다.
그 후 목표값인 2차원 배열과 확인하여 일치 여부를 체크합니다.

1. BFS 탐색을 진행합니다.
2. 수평, 수직 두 가지 방향을 고려하여 글자의 위치를 바꿔줍니다.
3. 큐에서 POP된 값을 확인하여 목표값과 비교합니다.
'''
from collections import deque

# 배열을 문자열 '1011011010111111'로 변환
def arr2bit(arr) :
    bit = ''
    for i in range(4):
        for j in range(4) :
            bit += arr[i][j]
    return bit

# 문자열을 4*4 배열로 변환
def bit2arr(bit) :
    arr = []
    for i in range(4):
        arr.append(list(bit[i*4:(i+1)*4]))
    return arr

inputs = []
while len(inputs) < 8 : # input 데이터의 공백 처리
    tmp = input()
    if not tmp :
        continue
    inputs.append(list(tmp.strip()))

current_board = inputs[:4]
target_board = inputs[4:]

trans = {
    'L' : '0',
    'P' : '1'
}
for i in range(4) :
    for j in range(4) :
        current_board[i][j] = trans[current_board[i][j]]
        target_board[i][j] = trans[target_board[i][j]]

targetbit = arr2bit(target_board)  #목표값
startbit = arr2bit(current_board)  #시작값

Q = deque()
Q.append(startbit)

# 방문처리 dictionary로
visited = dict()
visited[startbit] = 0  # count로 활용
while Q :
    bit = Q.popleft()
    board = bit2arr(bit)
    # 목표값과 비교
    if bit == targetbit :
        ans = visited[bit]
        break
    # 수평교환
    for i in range(4) :
        for j in range(3) :
            if board[i][j] != board[i][j+1]:
                board[i][j] , board[i][j+1] = board[i][j+1] , board[i][j]
                # 2차원 배열 -> 문자열
                newbit = arr2bit(board)
                if not visited.get(newbit) :
                    visited[newbit] = visited[bit] + 1
                    Q.append(newbit)
                board[i][j] , board[i][j+1] = board[i][j+1] , board[i][j]

    # 수직교환
    for i in range(3) :
        for j in range(4) :
            if board[i][j] != board[i+1][j]:
                board[i][j] , board[i+1][j] = board[i+1][j] , board[i][j]
                # 2차원 배열 -> 문자열
                newbit = arr2bit(board)
                if not visited.get(newbit) :
                    visited[newbit] = visited[bit] + 1
                    Q.append(newbit)
                board[i][j] , board[i+1][j] = board[i+1][j] , board[i][j]

# 출력
print(ans)