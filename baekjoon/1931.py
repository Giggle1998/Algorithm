import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    start, end = map(int, input().split())
    arr.append([start, end])

stack = []
arr.sort(key = lambda x: (x[1], x[0])) # 끝나는 시간 기준으로

for i in range(len(arr)):
    if stack:
        if stack[-1][1] <= arr[i][0]:
            stack.append(arr[i])
    else:
        stack.append(arr[i])

print(len(stack))
