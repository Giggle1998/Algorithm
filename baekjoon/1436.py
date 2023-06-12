N = int(input())
num = 665
cnt = 0
ans = 0
while 1:
    num += 1
    # 666이 있으면 카운트 증가
    if '666' in str(num):
        cnt += 1
        # 카운트가 N이라면 정답 처리
        if cnt == N:
            ans = num
            break
print(ans)

