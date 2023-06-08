'''
파이썬 함수인 replace를 적극! 활용할 수 있는 문제
'''
lst = input()
lst = lst.replace('XXXX', 'AAAA')
lst = lst.replace('XX', 'BB')

if 'X' in lst:
    print(-1)
else:
    print(lst)