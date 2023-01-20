T = int(input())
for t in range(T):
    vps = input()

    ps = 0
    for i in range(len(vps)):
        if vps[i] == '(':
            ps += 1
        elif vps[i] == ')':
            if ps == 0:
                ps -= 2
            else:
                ps -= 1
    if ps == 0:
        print('YES')
    else:
        print('NO')