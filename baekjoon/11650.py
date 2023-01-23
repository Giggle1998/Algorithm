import sys
input = sys.stdin.readline

T = int(input())
arr = []
for t in range(T):
    x,y  = map(int, input().split())
    arr.append([x, y])

# x좌표, y좌표 순으로, lambda식 이중 조건)
arr.sort(key = lambda x: (x[0],x[1]))

for ans in arr:
    print(ans[0], ans[1])