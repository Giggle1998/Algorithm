n = int(input())
exp = input()
ans = -1e9

def calc(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2


def dfs(idx, pre):
    global ans

    if idx == n:
        ans = max(ans, pre)
        return
    
    if idx + 3 < n:
        # 괄호 사용 
        dfs(idx + 4, calc(pre, calc(int(exp[idx+1]), int(exp[idx+3]), exp[idx+2]), exp[idx]))
    # 괄호 사용 X
    dfs(idx + 2, calc(pre, int(exp[idx+1]), exp[idx]))


dfs(1, int(exp[0]))
print(ans)

    