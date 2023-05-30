import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    data = input().rstrip()
    N = int(input())

    dic = {}
    rst_len = []
    for idx, value in enumerate(data):
        if value in dic:
            dic[value].append(idx)
        else:
            dic[value] = [idx]

    for value in dic:
        tmp = dic[value]
        tmp_len = len(tmp)
        if tmp_len < N:
            continue
        for i in range(tmp_len-N+1):
            rst = tmp[i+N-1] - tmp[i] + 1
            rst_len.append(rst)
    if rst_len:
        print(min(rst_len), max(rst_len))
    else:
        print(-1)