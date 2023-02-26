def bfs(f, s, g, u, d):
    q = []
    v = [0] * (F + 1)
    q.append(s)
    v[s] = 1
    while q:
        c = q.pop(0)
        if c == g:
            return v[c] - 1

        dr = [c + u, c - d]
        for di in dr:
            if 1 <= di < F + 1 and v[di] == 0:
                q.append(di)
                v[di] = v[c] + 1

    return 'use the stairs'


F, S, G, U, D = map(int, input().split())  # 총 층수 F, 강호 위치 S, 회사 위치 G
# U 위층 , D 아래층
print(bfs(F, S, G, U, D))