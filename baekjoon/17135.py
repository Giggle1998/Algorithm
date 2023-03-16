'''
N+1행의 모든 칸에는 성이 존재
적들은 공격 끝나면 한 칸씩 아래로 이동 -> 첫 줄에 0 리스트 삽입 and 마지막줄 삭제

적이 없으면 게임 끝 count(1)==0이면 종료

궁수 3명 배치
공격 조건 : 거리가 D이하인 적 중에서 가장 가까운 적, range(1, D+1)까지 탐색
적이 여럿일 경우 가장 왼쪽에 있는 적을 공격

왼 오 위만 탐색
'''
from itertools import combinations
from collections import deque
import copy

def one_cnt(tmp_arr):
    for lst in tmp_arr:
        if lst.count(1):
            return True
    return False

def bfs(c):
    que = deque()
    que.append((N-1, c))
    while que:
        si, sj = que.popleft()
        distance = abs(N-si) + abs(c-sj)
        if distance <= D:
            if tmp_arr[si][sj] == 1: # 궁수 위치 찾으면
                return (si, sj)
            for di, dj in ((0, -1), (-1, 0), (0, 1)):
                ni = si + di
                nj = sj + dj
                if 0 <= ni < N and 0 <= nj < M:
                    que.append((ni, nj))
        else:
            return

N, M, D = map(int, input().split())

arr = deque(list(map(int, input().split())) for _ in range(N))
ans = 0
for combi in combinations(list(range(M)), 3):
    die = 0
    tmp_arr = copy.deepcopy(arr)
    while one_cnt(tmp_arr):
        enermy = set()
        for c in combi:
            position = bfs(c)
            if position:
                enermy.add(position)
        for x, y in enermy: # 죽인 적을 0으로 변경
            tmp_arr[x][y] = 0
        die += len(enermy)
        tmp_arr.pop()
        tmp_arr.appendleft([0] * M)
    ans = max(ans, die)
print(ans)




