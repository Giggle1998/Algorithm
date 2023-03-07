import sys
input = sys.stdin.readline

def bt(n, depth, start):
    if n == depth:
        
        cnt_1 = cnt_2 = 0
        for t in tmp:
            if t in word:
                cnt_1 += 1
            else:
                cnt_2 += 1

        if 1 <= cnt_1 and cnt_2 >= 2:
            print(*tmp, sep='')            

    for i in range(start, M):
        tmp.append(lst[i])
        bt(n+1, depth, i+1) # 중요
        tmp.pop()

N, M = map(int, input().split())

lst = input().split()
lst.sort()
result = []
tmp = []
word = ['a', 'e', 'i', 'o', 'u']
bt(0, N, 0)
