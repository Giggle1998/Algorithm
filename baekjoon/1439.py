'''
문자열을 탐색하며 1, 0에 대한 연속된 문자열 구간을 카운트 합니다.
카운트 후 구간의 수가 젤 작은 숫자가 곧 행동의 최소 횟수이므로 정답처리 합니다.
1. 문자열을 탐색하며 최신 위치를 저장
2. 저장한 최신 위치를 바탕으로 현재 위치와 비교하여 1, 0에 대한 연속된 문자열을 카운트
3. 연속된 문자열 중 카운트 횟수가 작은 숫자를 정답 처리
'''
lst = list(input())

cnt_one = 0
cnt_zero = 0
cur = ''
for i in range(len(lst)):
    if lst[i] == '0':
        if cur != '0':
            cur = '0'
            cnt_zero += 1
    else:
        if cur != '1':
            cur = '1'
            cnt_one += 1
ans = min(cnt_zero, cnt_one)
print(ans)

