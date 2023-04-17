N = int(input())
lst = list(map(int, input().split()))

tmp = [lst[0]]

def b_search(num):
    start = 0
    end = len(tmp)-1

    while start <= end:
        mid = (start+end)//2
        # 해당값과 일치하면 종료
        if tmp[mid] == num:
            return mid
        # 이분 탐색 진행
        elif tmp[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    # 더 작은 값으로 갱신
    return start

for i in range(1, len(lst)):
    if tmp[-1] < lst[i]:
        tmp.append(lst[i])
    else:
        idx = b_search(lst[i])
        tmp[idx] = lst[i]

print(len(tmp))

