N = int(input())
lst = list(map(int, input().split()))
tmp = sorted(list(set(lst)))
dic = {tmp[i] : i for i in range(len(tmp))}

for l in lst:
    print(dic[l], end=' ')
