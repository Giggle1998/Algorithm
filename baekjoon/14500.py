N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

tetro = [
    [[1, 1, 1, 1]],
    [[1], [1], [1], [1]],

    [[1, 1], [1, 1]],

    [[1, 0],
     [1, 0],
     [1, 1]],
    [[1, 1],
     [1, 0],
     [1, 0]],
    [[1, 1],
     [0, 1],
     [0, 1]],
    [[0, 1],
     [0, 1],
     [1, 1]],
    [[1, 1, 1],
     [1, 0, 0]],
    [[1, 1, 1],
     [0, 0, 1]],
    [[1, 0, 0],
     [1, 1, 1]],
    [[0, 0, 1],
     [1, 1, 1]],

    [[1, 1, 0],
     [0, 1, 1]],
    [[0, 1, 1],
     [1, 1, 0]],
    [[1, 0],
     [1, 1],
     [0, 1]],
    [[0, 1],
     [1, 1],
     [1, 0]],

    [[1, 1, 1],
     [0, 1, 0]],
    [[0, 1, 0],
     [1, 1, 1]],
    [[1, 0],
     [1, 1],
     [1, 0]],
    [[0, 1],
     [1, 1],
     [0, 1]],
]

def search(shape, x, y):
    max_s = 0
    for i in range(N-y+1):
        for j in range(M-x+1):
            sum_tmp = 0
            for p in range(y):
                for q in range(x):
                    sum_tmp += shape[p][q] * arr[i+p][j+q]
            max_s = max(max_s, sum_tmp)
    return max_s

max_sum = 0
for shape in tetro:
    x = len(shape[0])
    y = len(shape)
    result = search(shape, x, y)
    max_sum = max(max_sum, result)
print(max_sum)


