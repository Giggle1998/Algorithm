import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# sort 함수의 파라미터 중 key를 활용해, y값을 기준으로 오름차순 정렬 -> 동일시 x값을 기준으로 오름차순 정렬
arr.sort(key=lambda x : (x[1], x[0]))
for a, b in arr:
    print(a, b)
