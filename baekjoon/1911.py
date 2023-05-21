N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x : x[0])

point = arr[0][0]
cnt = 0
for i in range(N):
    point = max(arr[i][0], point) # 널빤지의 최신 위치 비교
    tmp = arr[i][1] - point # 널빤지 설치에 필요한 길이

    if tmp % L: # 널빤지의 길이가 모자란 경우는 하나 더 추가
        cnt += (tmp // L + 1)
        point += (tmp // L + 1) * L
    else: # 널빤지의 길이가 딱 맞아 떨어지는 경우
        cnt += (tmp // L)
        point += (tmp // L) * L

print(cnt)
