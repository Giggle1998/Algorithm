import sys
input = sys.stdin.readline

text = input().rstrip()
pattern = input().rstrip()
stack = []
for t in text:
    stack.append(t)
    if len(stack) >= len(pattern):
        # 슬라이싱 비교
        if ''.join(stack[-len(pattern):]) == pattern: # 글자수 일치
            for i in range(len(pattern)):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')