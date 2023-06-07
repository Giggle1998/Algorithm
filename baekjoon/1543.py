data = input()
target = input()

cur_idx = 0
ans = 0
for i in range(len(data)):
    # 인덱스가 다르다면 건너뛰기
    if cur_idx > i:
        continue
    # 동일한 단어일 경우 정답 체크 및 인덱스 갱신
    if target == data[i:i+len(target)]:
        cur_idx = i + len(target)
        ans += 1

print(ans)
