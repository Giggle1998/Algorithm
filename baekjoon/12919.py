'''
S에서 T가 아니라 T에서 S로 변환
'''

S = input()
T = input()

def search(s):
    # 동일할 경우
    if s == S:
        return True
    # B일 경우
    if len(s) > 1 and s[0] == 'B' and search((s[1:])[::-1]):
        return True
    # A일 경우
    if len(s) > 1 and s[-1] == 'A' and search(s[:-1]):
        return True
    # 위의 조건에 해당하지 못하는 경우
    return False

if search(T):
    print(1)
else:
    print(0)

