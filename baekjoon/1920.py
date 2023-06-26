import sys
input = sys.stdin.readline

N = int(input())
N_li = sorted(map(int, input().split()))
M = int(input())
M_li = list(map(int, input().split()))

# for i in range(len(M_li)): ## 시간복잡도 logN^2
#     if M_li[i] in N_li:
#         print(1)
#     else:
#         print(0)

for num in M_li: # 시간복잡도 logN -> 이분탐색을 통해 문제 해결
    ans = 0
    start, end = 0, len(N_li) - 1

    while start <= end:
        mid = (start + end) // 2
        if N_li[mid] < num:
            start = mid + 1
        elif N_li[mid] > num:
            end = mid - 1
        else:
            ans = 1
            break

    print(ans)
