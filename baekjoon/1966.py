import sys
from collections import deque
input = sys.stdin.readline
# 중요한 문서가 뒤에 있으면 맨 뒤로 보내기 -> 중요한 문서 먼저 출력
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    que = deque(q)
    que_copy = que.copy() # 얕은 복사
    que[M] = str(que[M])
    cnt = 0

    if len(que) == 1:
        print(1)
    else:
        while 1:
            if int(que[0]) != max(que_copy):
                pop_index = que.popleft()
                pop_copy = que_copy.popleft()
                que.append(pop_index)
                que_copy.append(pop_copy)
                # print('if', que)
            elif int(que[0]) == max(que_copy):
                cnt += 1
                if not isinstance(que[0], int): # 정수가 아니라면 -> 찾고자하는 타켓값이라면
                    print(cnt+1)
                    break
                que.popleft()
                que_copy.popleft()
                # print('elif', que)
