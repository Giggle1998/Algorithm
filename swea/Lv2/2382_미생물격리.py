T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    # 1 상 2 하 3 좌 4 우
    dr = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    arr = [list(map(int, input().split())) for _ in range(K)]
    # 세로 가로 미생물수 방향
    for _ in range(M):
        for i in range(len(arr)):
            arr[i][0] = arr[i][0] + dr[arr[i][3]][0]
            arr[i][1] = arr[i][1] + dr[arr[i][3]][1]
            if not(1 <= arr[i][0] < N-1 and 1 <= arr[i][1] < N-1):
                # 약품을 만난 경우 미생물 개수 처리 및 방향 전환
                arr[i][2] //= 2
                if arr[i][3] == 1 or arr[i][3] == 3:
                    arr[i][3] += 1
                else:
                    arr[i][3] -= 1
        # 미생물이 만난 경우 더욱 더 원활하게 처리하기 위해 내림차순 정렬 진행
        arr.sort(key=lambda x : (x[0], x[1], x[2]), reverse=True)

        idx = 1
        while idx < len(arr):
            if arr[idx-1][0:2] == arr[idx][0:2]: # 좌표가 같을 때
                arr[idx-1][2] += arr[idx][2]
                arr.pop(idx)
            else: # 좌표가 다를 때
                idx += 1

    ans = 0
    for x, y, c, d in arr:
        ans += c
    print(f'#{t} {ans}')






