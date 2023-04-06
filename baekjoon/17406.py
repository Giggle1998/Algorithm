import copy
def move(si, sj, ei, ej, arr):
    while 1:
        # 시작점과 끝점이 동일해지면 회전 종료
        if si == ei and sj == ej:
            break
        n_num = arr[si][sj]
        i, j = si, sj
        d = 0
        # print(si, sj, ei, ej)
        while 1:
            if si <= i+dir[d][0] <= ei and sj <= j+dir[d][1] <= ej:
                tmp = n_num # 이전값
                i += dir[d][0]
                j += dir[d][1]
                n_num = arr[i][j] # 다음 값 빼놓기
                arr[i][j] = tmp # 이동
            else:
                d = (1 + d) % 4 # 방향이동

            # 원위치로 오면 종료
            if i == si and j == sj:
                break
        # 좌표 이동
        si += 1
        sj += 1
        ei -= 1
        ej -= 1

def perm(n, k):
    global min_v
    if n == k:
        board = copy.deepcopy(arr)
        for r, c, s in order: # 이동
            si, sj = r-s, c-s
            ei, ej = r+s, c+s
            move(si-1, sj-1, ei-1, ej-1, board)
        for lst in board: # 정답 찾기
            min_v = min(min_v, sum(lst))
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            order[k] = pos[i]
            perm(n, k+1)
            visited[i] = 0


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = 10**9
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
board = copy.deepcopy(arr)
pos = []
for _ in range(K):
    r, c, s = map(int, input().split())
    pos.append((r, c, s))

visited = [0] * K
order = [0] * K
perm(K, 0)
print(min_v)
