'''
S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.

위의 조건을 해석해보자면, A의 최소값과 B의 최대값을 곱한 결과값을 누적시켜주면 된다는 것이다.
1. A는 오름차순, B는 내림차순으로 정렬합니다.
2. 리스트의 길이가 동일하므로 동일 인덱스에서의 곱을 누적시켜줍니다.
'''
N = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst1.sort()
lst2.sort(reverse=True)

ans = 0
for i in range(N):
    ans += (lst1[i] * lst2[i])
print(ans)

