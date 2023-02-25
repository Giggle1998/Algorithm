def postorder(v):
    if tree[v][0] == '+':
        return postorder(tree[v][1]) + postorder(tree[v][2])
    elif tree[v][0] == '-':
        return postorder(tree[v][1]) - postorder(tree[v][2])
    elif tree[v][0] == '*':
        return postorder(tree[v][1]) * postorder(tree[v][2])
    elif tree[v][0] == '/':
        return postorder(tree[v][1]) // postorder(tree[v][2])
    else:
        return tree[v][0]

T = 10
for t in range(1, T + 1):
    N = int(input())
    tree = [[0] * 3 for _ in range(N + 1)]
    nums = []
    for i in range(1, N + 1):
        data = list(input().split())
        if len(data) == 2:
            tree[int(data[0])][0] = int(data[1])
        else:
            tree[int(data[0])][0] = data[1]
            tree[int(data[0])][1] = int(data[2])
            tree[int(data[0])][2] = int(data[3])

    print(f'#{t} {postorder(1)}')