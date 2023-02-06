T = 10
for t in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(100)]
    arr_t = list(list(zip(*arr)))

    cnt = 0
    max_palindrome = -1

    while cnt!=100:
        length = len(arr) - cnt + 1
        for i in range(100):
            for j in range(length):
                palindrome = arr[i][j:j+cnt]
                palindrome_t = arr_t[i][j:j+cnt]

                if palindrome == palindrome[::-1]:
                    if len(palindrome) > max_palindrome:
                        max_palindrome = len(palindrome)

                if palindrome_t == palindrome_t[::-1]:
                    if len(palindrome_t) > max_palindrome:
                        max_palindrome = len(palindrome_t)
        cnt += 1

    print(f'#{t} {max_palindrome}')
