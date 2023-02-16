def gababo(front, back):
    if (arr[front] - arr[back] == 0) or (arr[front] - arr[back] == 1) or (arr[front] - arr[back] == -2):
        return front
    else:
        return back

def winner(s, e):
    start = s
    end = e

    if start == end:
        return start
    mid = (start + end) // 2
    front = winner(start, mid)
    back = winner(mid+1, end)

    return gababo(front, back)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{t} {winner(0, N-1)+1}')


