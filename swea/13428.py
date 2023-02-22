T = int(input())
for tc in range(1, T+1):
    lst = list(input())
    N = len(lst)
    mx = mn = int("".join(lst))
    # [1] N개 중에서 2개를 뽑는 가능한 모든 조합
    for i in range(N-1):
        for j in range(i+1, N):
            lst[i],lst[j] = lst[j],lst[i]   # 2개의 숫자를 교환
            if lst[0]!='0' and mx<int("".join(lst)):
                mx = int("".join(lst))
            if lst[0]!='0' and mn>int("".join(lst)):
                mn = int("".join(lst))
            lst[i],lst[j] = lst[j],lst[i]   # 2개의 숫자를 원상복구
    print(f'#{tc} {mn} {mx}')