def swap(str):
    for i in range(len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
    else:
        return True    

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            sum_h = ''
            sum_w = ''
            for k in range(M):
                sum_w += arr[i][j+k]
                sum_h += arr[j+k][i]
                    
        if swap(sum_w):
            print(f'#{t} {sum_w}')
        if swap(sum_h):
            print(f'#{t} {sum_h}')    