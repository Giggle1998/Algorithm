def bt(idx, start):
    global ans
    if idx == M:
        min_sum = 0
        for h in home:
            min_v = 99999
            for c in rst:
                tmp = abs(h[0]-c[0])+abs(h[1]-c[1])
                min_v = min(tmp, min_v)
            min_sum += min_v
        ans = min(ans, min_sum)
        return

    for i in range(start, len(chicken)):
        rst.append(chicken[i])
        bt(idx+1, i+1)
        rst.pop()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))
ans = 99999
rst = []
bt(0, 0)
print(ans)
# min_sum = 99999
# for lst in combi:
#     tmp_sum = 0
#     for hi, hj in home:
#         min_dis = 99999
#         tmp = 0
#         for k in range(len(lst)):
#             x = lst[k][0]
#             y = lst[k][1]
#             d = abs(x-hi) + abs(y-hj)
#             min_dis = min(min_dis, d)
#         tmp += min_dis
#         tmp_sum += tmp
#     min_sum = min(min_sum, tmp_sum)
# print(min_sum)




