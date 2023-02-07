# ladder1
T = 10
for t in range(1, T+1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]
    visited = [[False for _ in range(100)] for _ in range(100)]
    s_i = 99
    s_j = 0
    for j in range(100):
        if arr[s_i][j] == 2:
            s_j = j

    while s_i > 0:
        visited[s_i][s_j] = True
        if s_j + 1 < 100 and arr[s_i][s_j+1] and visited[s_i][s_j+1] == False:
            s_j += 1
        elif s_j - 1 >= 0 and arr[s_i][s_j-1] and visited[s_i][s_j-1] == False:
            s_j -= 1
        else:
            s_i -= 1


    print(f'#{t} {s_j}')



