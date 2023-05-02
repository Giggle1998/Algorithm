from collections import deque
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
ri, rj = 0, 0
bi, bj = 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            ri, rj = i, j
        if arr[i][j] == 'B':
            bi, bj = i, j

def bfs():
    que = deque()
    que.append((ri, rj, 0, bi, bj))
    ans = 0
    while que:
        flag = 0
        sri, srj, cnt, sbi, sbj = que.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nri, nrj = sri, srj
            nbi, nbj = sbi, sbj
            flag_red = 0
            flag_blue = 0
            while 1:
                nri += di
                nrj += dj
                if arr[nri][nrj] == '.':
                    continue
                if arr[nri][nrj] == '#' or (nri, nrj) == (nbi, nbj):
                    nri -= di
                    nrj -= dj
                    break
                if arr[nri][nrj] == 'O':
                    flag_red = 1
                    break

            while 1:
                nbi += di
                nbj += dj
                if arr[nbi][nbj] == '.':
                    continue
                if arr[nbi][nbj] == '#' or ((nri, nrj) == (nbi, nbj) and flag_red==0):
                    nbi -= di
                    nbj -= dj
                    break
                if arr[nbi][nbj] == 'O':
                    flag_blue = 1
                    break

            if flag_red == 1 and flag_blue == 0:
                ans = cnt + 1
                flag = 1
                break
            elif flag_red == 1 or flag_blue == 1:
                continue
            else:
                if cnt+1 <= 10:
                    que.append((nri, nrj, cnt+1, nbi, nbj))
        if flag:
            break

    if ans:
        return ans
    else:
        return -1

print(bfs())





