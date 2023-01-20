import sys
T = int(sys.stdin.readline())

que = []
for t in range(T):
    com = sys.stdin.readline().rstrip()

    if com == 'size':
        print(len(que))
    elif com == 'empty':
        if que == []:
            print(1)
        else:
            print(0)
    elif com == 'front':
        if que == []:
            print(-1)
        else:
            print(que[0])
    elif com == 'back':
        if que == []:
            print(-1)
        else:
            print(que[len(que)-1])
    elif com == 'pop':
        if que == []:
            print(-1)
        else:
            print(que.pop(0))
    elif com[0] == 'p':
        push_li = com.split()
        que.append(push_li[1])

