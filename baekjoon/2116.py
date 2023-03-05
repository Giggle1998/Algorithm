N, L = map(int, input().split())

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

road = [2] * L
for i in range(len(lst)):
    road[lst[i][0] - 1] = False

time = 0
idx = 0

while idx != L:
    time += 1

    for i in lst:
        if road[i[0] - 1] == False:
            if time % i[1] == 0:
                road[i[0] - 1] = True
        elif road[i[0] - 1] == True:
            if time % i[2] == 0:
                road[i[0] - 1] = False

    if road[idx] != 2:
        if road[idx] == True:
            idx += 1
    else:
        idx += 1
print(time)