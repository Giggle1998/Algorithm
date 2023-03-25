N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

com = []
for _ in range(M):
    c1, c2 = map(int, input().split())
    com.append([c1, c2])
#구름 이동
dr = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))

first_c = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

def ans_sum():
    sum_v = 0
    for lst in arr:
        sum_v += sum(lst)
    return sum_v

for i in range(len(com)): # 총 커맨드 수
    next_c = []
    # 구름 이동
    for x, y in first_c:
        nx = (x + dr[com[i][0] - 1][0] * com[i][1]) % N
        ny = (y + dr[com[i][0] - 1][1] * com[i][1]) % N
        next_c.append((nx, ny))
        arr[nx][ny] += 1

    # 구름 초기화
    first_c = []

    # 물 복사
    for i, j in next_c:
        cnt = 0
        for d1, d2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            ni = i + d1
            nj = j + d2
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]:
                cnt += 1
        arr[i][j] += cnt

    # 구름 만들기
    for i in range(N):
        for j in range(N):
            if (i, j) in next_c:
                continue
            if arr[i][j] >= 2:
                arr[i][j] -= 2
                first_c.append((i, j))
# pprint.pprint(arr)
print(ans_sum())





