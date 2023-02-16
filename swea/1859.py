T = int(input())

for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    ans_li = []
    max_ans = lst[-1]
    for i in range(len(lst) - 2, -1, -1):
        if max_ans >= lst[i]:
            ans_li.append(lst[i])
        else:
            ans += (max_ans * (len(ans_li))) - sum(ans_li)
            max_ans = lst[i]
            ans_li = []
    if ans_li:
        ans += (max_ans * (len(ans_li))) - sum(ans_li)
    print(f'#{t} {ans}')