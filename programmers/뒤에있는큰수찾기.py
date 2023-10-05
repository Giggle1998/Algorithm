def solution(numbers):
    # 스택
    stack = []
    answer = [0] * len(numbers)

    # 탐색 진행
    for i in range(len(numbers)):
            while stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            stack.append(i)
    while stack:
            answer[stack.pop()] = -1
    
    return answer