N, M, K = map(int, input().split())
lst = list(map(int, input().split()))
# 최대 개수를 도출하기 위해 오름차순으로 탐색합니다.
lst.sort()

ani = []
for i in range(N):
    time = 0
    # 꾸러미가 가능한 경우
    if i < K:
        time = lst[i]
    # 꾸러미가 불가능한 경우
    else:
        time = ani[i-K] + lst[i]

    if time <= M:
        # 시청할 수 있는 애니
        ani.append(time)
    else:
        break

print(len(ani))