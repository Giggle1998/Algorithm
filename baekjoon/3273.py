N = int(input())
lst = list(map(int, input().split()))
X = int(input())
# 오름차순 정렬
lst.sort()
cnt = 0
# 왼쪽, 오른쪽 포인터
left, right = 0, N-1

while left < right:
    # 타겟값을 만족한다면 두 포인터를 이동 및 카운트 증가
    if lst[left] + lst[right] == X:
        cnt += 1
        right -= 1
        left += 1
    # 타겟값보다 작다면 왼쪽 포인터를 이동
    elif lst[left] + lst[right] < X:
        left += 1
    # 타겟값보다 크다면 오른쪽 포인터를 이동
    else:
        right -= 1

print(cnt)