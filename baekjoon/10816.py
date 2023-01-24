import sys
input = sys.stdin.readline
N = int(input())
N_li = list(map(int, input().split()))
M = int(input())
M_li = list(map(int, input().split()))
N_dict = {}
for n in N_li:
    if n not in N_dict:
        N_dict[n] = 1
    else:
        N_dict[n] += 1


for m in M_li:
    if m in N_dict:
        print(N_dict[m], end=' ')
    else:
        print(0, end=' ')




