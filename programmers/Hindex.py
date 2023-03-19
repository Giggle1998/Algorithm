def solution(citations):
    answer = 0 # H_index의 최대값
    # 내림차순으로 정리
    citations.sort(reverse=True)
    
    for idx, citation in enumerate(citations):
        # 인덱스와 비교해 인덱스가 더 큰 경우 정답으로 반환
        if idx >= citation:
            answer = idx
            return answer
    # 전부 다 탐색한 경우 길이를 반환
    return len(citations)