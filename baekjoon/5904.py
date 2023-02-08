N = int(input())
arr = [0] * (N+1)

def moo_game (N, arr):
    arr[0] = 'm'+'o'*2
    arr[1] = arr[0] + 'm'+'o'*(2+1) + arr[0]
    arr[2] = arr[1] + 'm'+'o'*(2+2) + arr[1]
    if N >= 3:
        for i in range(3, N+1):
            arr[i] = arr[i-1] + 'm'+'o'*(2+i) + arr[i-1]
    return arr        

print(moo_game(N, arr)[N][N-1])