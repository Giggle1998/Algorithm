import sys
T = int(sys.stdin.readline())

words_li = []
for t in range(T):
    words = sys.stdin.readline().rstrip()
    words_li.append(words)

# 단어 길이 비교 -> 동일 길이시 사전 순
# 사전 순 비교후 길이 비교를 해줘야 함
words_set = set(words_li)
words_ans = list(words_set)
words_sort = sorted(words_ans)
words_sort.sort(key=len)

for word in words_sort:
    print(word)