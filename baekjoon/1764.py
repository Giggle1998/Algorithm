'''
N, M이 최대 50,000이기 때문에 일반 리스트만 사용해서는 시간초과를 피할 수 없습니다.
시간 초과를 피하기 위해 파이썬 집합 set 자료구조와 & 비트 연산자를 활용해
교집합을 구해 최종적으로 문제를 해결했습니다.
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listen = [input().rstrip() for _ in range(N)]
see = [input().rstrip() for _ in range(M)]
# 교집합 구하기
ans = list(set(listen) & set(see))

ans.sort()
print(len(ans))
for a in ans:
    print(a)

