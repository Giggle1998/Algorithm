'''
필름은 두께 D, 가로 크기 W의 보호 필름
단면의 모든 세로방향에 대해서 동일한 특성의 셀들이
K개 이상 연속적으로 있는 경우에만 성능검사를 통과
-> 두께 D, 가로크기 W인 보호 필름 단면의 정보와 합격기준 K가 주어졌을 때
약품 투입 횟수를 최소로 하여 성능검사를 통과할 수 있는 방법?
'''
def check(arr):
    for i in range(W):
        cnt = 1
        for j in range(D-1):
            if arr[j][i] == arr[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= K: # 조건을 만족한 경우 행 탐색 종료
                break
        if cnt < K: # 조건 만족하지 못하면 바로 실패
            return False
    return True # 조건 만족

def comb(r, k, s): # nCr
    global ans
    if k == r:
        if check(film):
            ans = min(ans, k)
        return

    for i in range(s, D):
        for j in range(2): # A, B 약품
            if visited[i] == 0:
                visited[i] = 1
                film[i] = change[j] # 약품투입
                comb(r, k+1, i+1)
                film[i] = tmp[i]  # 원본
                visited[i] = 0

T = int(input())
for t in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    tmp = [lst[:] for lst in film] # 깊은 복사
    change = [[0]*W, [1]*W] # 투입 약품
    visited = [0] * W
    ans = 10**9
    if check(film): # 약품 투입하지 않고 바로 통과하는 경우
        ans = 0
    else: # 약품 투입
        for i in range(1, D+1):
            comb(i, 0, 0)
            if ans != 10**9:
                break
    print(f'#{t} {ans}')
