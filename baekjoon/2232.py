import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    tmp = int(input())
    lst.append(tmp)

ans = []
if len(lst) > 1:
    for i in range(N):
        if i == 0:
            if 0 <= lst[i] >= lst[i+1]:
                ans.append(i+1)
        elif i == N-1:
            if 0 <= lst[i] >= lst[i-1]:
                ans.append(i+1)
        else:
            if lst[i-1] <= lst[i] >= lst[i+1]:
                ans.append(i+1)

    for rst in ans:
        print(rst)
else:
    print(1)



