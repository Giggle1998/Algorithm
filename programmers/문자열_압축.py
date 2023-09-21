def solution(s):
    answer = 0
    
    min_length = 10**9
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)//2 + 1):
        
        rst = ''
        tmp = s[0:i]
        start = 0
        cnt = 0

        for j in range(0, len(s), i):
            if s[j:i+j] == tmp:
                cnt += 1
                
            else: # 일치하지 않는 경우
                if cnt == 1:
                    rst += tmp
                else:
                    rst += str(cnt) + tmp
                    
                tmp = s[j:i+j]
                start = j
                cnt = 1
                
        if cnt == 1:
            rst += s[start:]
        else:
            rst += str(cnt) + tmp
        
        length = len(rst)
        min_length = min(min_length, length)
        
    
    return min_length
    
                
                    
            