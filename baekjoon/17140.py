r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
ans = -1

def calArr():
    global arr

    newArr = []

    for a in arr:
        nums = set(a)
        tmp1 = []
        tmp2 = []

        for num in nums:
            if num == 0:
                continue

            cnt = a.count(num)
            tmp1.append([num, cnt])
        
        tmp1.sort(key = lambda x : (x[1], x[0]))
        
        for tmp in tmp1:
            tmp2.append(tmp[0])
            tmp2.append(tmp[1])
        
        # 100개로 개수 제한
        tmp2 = tmp2[:100]
        newArr.append(tmp2)
    
    # 0 채우기
    maxLen = max(map(len, newArr))
    for i in range(len(newArr)):
        while len(newArr[i]) != maxLen:
            newArr[i].append(0)
    
    arr = newArr

for i in range(101):
    if len(arr) >= r and len(arr[0]) >= c and arr[r-1][c-1] == k:
        ans = i
        break

    # R 연산
    if (len(arr) >= len(arr[0])):
        calArr()
    # C 연산
    else:
        arr = list(map(list, zip(*arr)))
        calArr()
        arr = list(map(list, zip(*arr)))
        
print(ans)