def solution(users, emoticons):    
    sale = [40, 30 , 20, 10]
    emoticons.sort(reverse=True)
    arr = []
    
    def permutation(check, idx):
        if idx == len(check):
            arr.append(check[:])
            return

        for num in sale:
            check[idx] += num
            permutation(check, idx+1)
            check[idx] -= num
    
    permutation([0] * len(emoticons), 0)

    max_cnt = -1
    max_don = -1

    for lst in arr:
        cnt = 0 # 총 고객
        don = 0 # 총 이윤
        for user in users:
            rst = 0
            for i in range(len(emoticons)):
                if (user[0] <= lst[i]): # 할인하는 퍼센트보다 작은 경우
                    tmp = emoticons[i] * (100 - lst[i]) // 100 # 할인 금액
                    if (rst + tmp >= user[1]): # 예산을 초과한다면 구매 취소
                        rst = 0 # 구매 취소
                        cnt += 1 # 가입
                        break
                    rst += tmp
                    
            don += rst
        
        if (max_cnt <= cnt):
            if (max_cnt == cnt):
                max_don = max(max_don, don)
            else:
                max_don = don    
            max_cnt = cnt
        
        
    ans = [max_cnt, max_don]
    return ans
        
    
    
            