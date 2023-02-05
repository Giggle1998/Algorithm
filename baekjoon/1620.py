import sys
input = sys.stdin.readline

N, M = map(int, input().split())

N_li = []
M_li = []

for _ in range(N):
    n = input()
    N_li.append(n)

for _ in range(M):
    m = input()
    if m.isalpha():
        print(N_li.index(m)+1)

    if m.digit():
        print(N_li[int(m)])







