n1, n2 = map(int, input().split())

ans_yak = []
ans_bae = []

dict_yak = {}
dict_bae = {}

yak_li = []
bae_li = []

for i in range(1, n1+1):
    if n1 % i == 0: # 최소공약수
        ans_yak.append(i)
    ans_bae.append(n2 * i) # 최대공배수

for j in range(1, n2+1):
    if n2 % j == 0: # 최소공약수
        ans_yak.append(j)
    ans_bae.append(n1 * j) # 최대공배수

# 딕셔너리로 중복 확인
for yak in ans_yak:
    if yak not in dict_yak:
        dict_yak[yak] = 1
    else:
        dict_yak[yak] += 1

for bae in ans_bae:
    if bae not in dict_bae:
        dict_bae[bae] = 1
    else:
        dict_bae[bae] += 1
# 최소공약수, 최소공배수 확인
for k, v in dict_yak.items():
    if v == 2:
        yak_li.append(k)

for k, v in dict_bae.items():
    if v == 2:
        bae_li.append(k)

print(yak_li[-1])
print(bae_li[0])

