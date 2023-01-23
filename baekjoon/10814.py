T = int(input())
ans = []
for t in range(T):
    age, name = input().split()
    age = int(age)
    ans.append([age, name])

ans.sort(key = lambda x: x[0])
for a in ans:
    print(a[0], a[1])