import re
sent = input()

# sent1 = sent.split('')
# print(sent1)

ho_1 = 0
ho_2 = 0
if sent[0] == '<':
    for i in range(len(sent)):
        if sent[i] == '>':
            ho_1 = i
            break

    for j in range(ho_1+1, len(sent)):
        if sent[j] == '<':
            ho_2 = j
            break
    #### 태그 안에 단어 처리
    ans = sent[ho_1 + 1:ho_2]
    ans = ans.split()
    print(sent[:ho_1 + 1],end="")
    for a in ans:
        print(a[::-1],end=" ")
    print(sent[ho_2:])

else:
    sent = sent.split()
    for i in range(len(sent)):
        print(sent[i][::-1], end=" ")






