'''
N : j + 1, E : i + 1, S : j - 1, W : i-1
명령은 각 로봇들간 순차적으로 실행
'''
def check(n, ci, cj):
    if 0 >= ci or 0 >= cj or A < ci or B < cj:
        return f'Robot {n} crashes into the wall'

    for i in range(len(pos)):
        if i == n-1:
            continue
        if (ci, cj) == (pos[i][0], pos[i][1]):
            return f'Robot {n} crashes into the robot {i+1}'

    return 0

A, B = map(int, input().split())
N, M = map(int, input().split())
pos = []
tmp = 1
for _ in range(N):
    x, y, d = input().split()
    x, y = int(x), int(y)
    pos.append([x, y, d])

rst = 0
L_lst = ['N', 'E', 'S', 'W']
R_lst = ['N', 'W', 'S', 'E']
for _ in range(M):
    flag = 0
    # 로봇번호, 명령 종류, 횟수
    n, t, c = input().split()
    n, c = int(n), int(c)
    if t == 'L':
        dir = 0
        if pos[n - 1][2] == 'N': dir = 0
        elif pos[n - 1][2] == 'E': dir = 1
        elif pos[n - 1][2] == 'S': dir = 2
        elif pos[n - 1][2] == 'W': dir = 3
        pos[n-1][2] = L_lst[(dir+1)%4]
    elif t == 'R':
        dir = 0
        if pos[n - 1][2] == 'N':dir = 0
        elif pos[n - 1][2] == 'E':dir = 3
        elif pos[n - 1][2] == 'S':dir = 2
        elif pos[n - 1][2] == 'W':dir = 1
        pos[n - 1][2] = R_lst[(dir + 1) % 4]
    else:
        for _ in range(c):
            if pos[n-1][2] == 'N': pos[n-1][1] += 1
            elif pos[n-1][2] == 'E': pos[n - 1][0] += 1
            elif pos[n-1][2] == 'S': pos[n - 1][1] -= 1
            elif pos[n-1][2] == 'W': pos[n - 1][0] -= 1
            rst = check(n, pos[n-1][0], pos[n-1][1])
            if rst:
                flag = 1
                break
    if flag:
        break
if rst == 0:
    print('OK')
else:
    print(rst)



