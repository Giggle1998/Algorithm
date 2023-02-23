data = list(input())
N = int(input())
backup = []
for i in range(N):
    com = input().split()
    if com[0] == 'L':
        if len(data) == 0: # 문자 처음
            continue
        backup.append(data.pop())
    elif com[0] == 'D':
        if len(backup) == 0: # 문자 끝
            continue
        data.append(backup.pop())
    elif com[0] == 'B':
        if len(data) == 0:
            continue
        data.pop()
    else:
        data.append(com[1])
for j in range(len(backup)):
    data.append(backup.pop())

print(''.join(data))