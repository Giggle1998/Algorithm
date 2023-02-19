import sys
input = sys.stdin.readline

N = int(input())

st = list(input())
num_li = []
score = {}
result = []
for i in range(N):
    n = int(input())
    num_li.append(n)
cnt = -1
for s in st:
    if s.isalpha():
        if s in score:
            continue
        cnt += 1
        score[s] = num_li[cnt]

for s in st:
    if s.isalpha():
        result.append(score[s])
    else:
        if len(result) >= 2:
            num2 = result.pop()
            num1 = result.pop()

            if s == '+':
                result.append(num1 + num2)
            elif s == '-':
                result.append(num1 - num2)
            elif s == '*':
                result.append(num1 * num2)
            elif s == '/':
                result.append(num1 / num2)

print(f'{result[-1]:.2f}')


