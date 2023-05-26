def search(k, muscle):
    global ans

    if k == N: # 운동 키트 사용량에 해당하면 정답처리
        ans += 1
        return

    for i in range(N):
        # 근손실이 발생하지 않으면 탐색 진행
        if muscle + lst[i] - K >= 500:
            if visited[i] == 0:
                visited[i] = 1
                search(k+1, muscle + lst[i] - K)
                visited[i] = 0

N, K = map(int, input().split())
lst = list(map(int, input().split()))

visited = [0] * N
ans = 0
search(0, 500)
print(ans)