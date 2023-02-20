def nqueen(n):
    global cnt
    if n == N:
        cnt += 1
        return

    for i in range(N):
        if not visited_1[i] and not visited_2[n+i] and not visited_3[n-i]:
            visited_1[i] = visited_2[n+i] = visited_3[n-i] = 1
            nqueen(n+1)
            visited_1[i] = visited_2[n+i] = visited_3[n-i] = 0

N = int(input())
visited_1 = [False] * N # 열 탐색
visited_2 = [False] * (2*N-1) # 대각 탐색
visited_3 = [False] * (2*N-1) # 역대각 탐색
cnt = 0

nqueen(0) # 0 깊이부터 탐색
print(cnt)