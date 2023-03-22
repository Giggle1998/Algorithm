from itertools import permutations
import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans_score = 0
for p in permutations(list(range(1, 9)), 8):
    per = list(p)
    per.insert(3, 0)
    cnt_out = 0
    score = 0
    idx = 0
    cnt = 0
    ruru = [0] * 3
    while cnt < N:
        n = per[idx]
        cur = arr[cnt][n]
        if cur == 0:
            cnt_out += 1
        elif cur == 1:
            if ruru[2]:
                score += 1
                ruru[2] = 0
            if ruru[1]:
                ruru[2] = 1
                ruru[1] = 0
            if ruru[0]:
                ruru[1] = 1
                ruru[0] = 0
            ruru[0] = 1
        elif cur == 2:
            if ruru[2]:
                score += 1
                ruru[2] = 0
            if ruru[1]:
                score += 1
                ruru[1] = 0
            if ruru[0]:
                ruru[2] = 1
                ruru[0] = 0
            ruru[1] = 1
        elif cur == 3:
            if ruru[2]:
                score += 1
                ruru[2] = 0
            if ruru[1]:
                score += 1
                ruru[1] = 0
            if ruru[0]:
                score += 1
                ruru[0] = 0
            ruru[2] = 1
        else: # 홈런
            if ruru[2]:
                score += 1
                ruru[2] = 0
            if ruru[1]:
                score += 1
                ruru[1] = 0
            if ruru[0]:
                score += 1
                ruru[0] = 0
            score+=1

        idx = (idx+1) % 9

        if cnt_out == 3:
            cnt += 1
            ruru = [0] * 3
            cnt_out = 0
    ans_score = max(ans_score, score)
print(ans_score)