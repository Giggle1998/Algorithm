'''
1. 완전탐색을 통해 수식의 조합을 생성
2. 수식이 만들어졌을 때 우선순위에 따라 계산을 진행
3. 먼저 곱셈과 나눗셈을 진행한 수식을 새로 생성
4. 그 다음 순차적으로 수식에 따른 덧셈과 뺄셈을 진행
'''
def pm_cal(cursum):
    tmp = cursum[0]
    for i in range(1, len(cursum) - 1, 2):
        if cursum[i] in '+-*/':
            if cursum[i] == '+':
                tmp += cursum[i + 1]
            elif cursum[i] == '-':
                tmp -= cursum[i + 1]
    return tmp

def cal(cursum):
    susik = []
    flag = 0
    for i in range(len(cursum)-1):
        if cursum[i] == '*':
            susik[-1] = susik[-1] * cursum[i+1]
            flag = 1
        elif cursum[i] == '/':
            susik[-1] = int(susik[-1] / cursum[i + 1])
            flag = 1
        else:
            if flag == 0:
                susik.append(cursum[i])
            if flag == 1:
                flag = 0
    if susik[-1] in ['+','-']:
        susik.append(cursum[-1])
    rst = pm_cal(susik)
    return rst

def dfs(n, cursum):
    global plus, minus, mul, div, min_ans, max_ans

    if n == N-1:
        rst = cal(cursum)
        if rst < min_ans:
            min_ans = rst
        if rst > max_ans:
            max_ans = rst
        return
    else:
        if plus:
            plus -= 1
            dfs(n+1, cursum+['+']+[lst[n+1]])
            plus += 1
        if minus:
            minus -= 1
            dfs(n+1, cursum + ['-'] + [lst[n+1]])
            minus += 1
        if mul:
            mul -= 1
            dfs(n+1, cursum + ['*'] + [lst[n+1]])
            mul += 1
        if div:
            div -= 1
            dfs(n+1, cursum + ['/'] + [lst[n+1]])
            div += 1

N = int(input())
lst = list(map(int, input().split()))
# + - * //
plus, minus, mul, div = list(map(int, input().split()))
max_ans = -(10**9+1)
min_ans = 10**9+1
dfs(0, [lst[0]])
print(max_ans)
print(min_ans)
