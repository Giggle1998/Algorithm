import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    name, day, month, year = input().split()
    arr.append([int(year), int(month), int(day), name])
arr.sort(key=lambda x : (x[0], x[1], x[2]))
print(arr[-1][3])
print(arr[0][3])
