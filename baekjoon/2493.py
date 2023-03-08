import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
check = []
result = [0] * N

for i in range(N):
    while check:
        if lst[check[-1][0]] < lst[i]:
            check.pop()
        else:
            result[i] = check[-1][0] + 1 # 조건에 맞는 탑을 찾은 경우
            break
    check.append([i, lst[i]])
print(*result)




