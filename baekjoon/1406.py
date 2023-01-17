import sys
T = input()
N = int(input())

ans = [i for i in T]

cursor = len(T)
for n in range(N):
    value = (sys.stdin.readline()).split()

    if value[0] == 'L':
        if cursor == 0:
            continue
        else:
            cursor -= 1

    elif value[0] == 'D':
        if cursor == len(T):
            continue
        else:
            cursor += 1

    elif value[0] == 'B':
        if cursor == 0:
            continue
        else:
            ans.pop(cursor-1)
            cursor -= 1

    elif value[0] == 'P':
        ans.insert(cursor, value[1])
        cursor += 1

for a in ans:
    print(*a, end='')


