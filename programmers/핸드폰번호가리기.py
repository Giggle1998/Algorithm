def solution(phone_number):
    if len(phone_number) >= 4 and len(phone_number) <= 20:
        lis = list(phone_number)
        back_num = lis[-4:]
        front_num = []
        
        for i in range(len(phone_number[:-4])):
            front_num.insert(i, "*")
        
        front_num.extend(back_num)
        answer = "".join(front_num)
        return answer