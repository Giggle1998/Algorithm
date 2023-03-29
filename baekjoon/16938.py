def comb(n, r, k, s):
    global cnt
    if r == k:
        if L <= sum(tmp) <= R:
            if max(tmp) - min(tmp) < X:
                return
            else:
                cnt += 1
        else:
            return
    else:
        for i in range(s, n-r+1+k):
            tmp[k] = lst[i]
            comb(n, r, k+1, i+1)

N, L, R, X = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for r in range(2, N+1):
    tmp = [0] * r
    comb(N, r, 0, 0)
print(cnt)