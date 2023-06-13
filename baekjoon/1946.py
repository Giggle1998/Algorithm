import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    lst = []
    for _ in range(N):
        tmp1, tmp2 = map(int, input().split())
        lst.append([tmp1, tmp2])
    # 오름차순으로 서류심사 성적을 정렬
    lst.sort()

    min_v = lst[0][1]
    cnt = 1
    for i in range(N):
        # 현재 성적보다 등수가 낮으면 선발 가능
        if min_v > lst[i][1]:
            cnt += 1
            # 현재 성적으로 재갱신
            min_v = lst[i][1]

    print(cnt)
