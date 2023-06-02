'''
파이썬 힙큐 내장 모듈을 사용
힙큐의 자료구조 설명과 함께 블로그 게시
'''
import heapq, sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    tmp = int(input())
    if tmp == 0:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, tmp)


