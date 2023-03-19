def solution(s):
    # {{, }}를 제거 후 },{ 으로 나누기
    lst = s[2:-2].split("},{")
    # 길이 별로 오름차순 정렬
    lst = sorted(lst, key=len)
    answer = []
    for item in lst:
        # 각각의 원소로 분류 후
        item = list(map(int, item.split(",")))
        for value in item:
            # 포함되어 있지 않으면 input
            if value not in answer:
                answer.append(value)
    return answer