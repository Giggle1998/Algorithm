import sys
input = sys.stdin.readline
T = int(input())

for t in range(T):
    arr = []
    dic = {}
    N = int(input())
    ans = 1
    for i in range(N):
        a, b = input().split()
        if b not in dic:
            dic[b] = 1
        else:
            dic[b] += 1

    if len(dic) == 1:
        print(dic[b])
    else:
        for v in dic.values():
            ans *= v+1
        print(ans-1)
