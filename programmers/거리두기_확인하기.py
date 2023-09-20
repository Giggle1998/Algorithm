from collections import deque

def solution(places):
    answer = []
    
    for room in places:
        arr = []
        for r in room:
            lst = list(r)
            arr.append(lst)
        
        ans = 1
        for i in range(5):
            for j in range(5):
                flag = 0
                if arr[i][j] == 'P':
                    rst = bfs(i, j, arr)
                    # 한 명이라도 지키지 않는다면 바로 종료
                    if rst == 0:
                        ans = 0
                        flag = 1
                        break
            if flag:
                break
                
        answer.append(ans)
    return answer

def bfs(x, y, arr):
    que = deque()
    visited = [[False] * 5 for _ in range(5)]
    visited[x][y] = True
    que.append([x, y, 0])
    
    while que:
        cx, cy, cnt = que.popleft()
        
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = cx + di
            ny = cy + dj
            if (0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]):
                visited[nx][ny] = True
                if arr[nx][ny] == 'P':
                    if cnt + 1 <= 2:
                        return 0
                elif arr[nx][ny] == 'O':
                    if cnt + 1 == 1:
                        que.append([nx, ny, cnt+1])
                        
    return 1
    