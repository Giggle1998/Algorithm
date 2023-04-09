'''
["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
'''
def solution(record):
    answer = [] # 최종 output을 저장하는 정답 리스트
    name_dic = dict() # 중복없이 하나의 이름만을 저장하기 위해 딕셔너리 사용
    com_li = []
    for lst in record:
        # 명령어, 유저아이디, 닉네임
        command, uid, *name = lst.split()
        # 추후 output을 도출하기 위해 명령어와 유저아이디 저장
        com_li.append((command, uid))
        # 이름이 존재하면 이름값을 최신화
        if name != []:
            name_dic[uid] = name[0]

    for com, uid in com_li:
        # 채팅방 입장
        if com == 'Enter':
            answer.append(f'{name_dic[uid]}님이 들어왔습니다.')
        # 채팅방 퇴장
        elif com == 'Leave':
            answer.append(f'{name_dic[uid]}님이 나갔습니다.')

    return answer




