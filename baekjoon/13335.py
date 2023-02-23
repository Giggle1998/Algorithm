from collections import deque
N, W, L = map(int, input().split())
que_truck = deque(map(int, input().split()))
que_bridge = deque([0] * W) # 다리
cnt = 0
while que_truck:
    que_bridge.popleft()
    truck = que_truck[0]
    if sum(que_bridge) + truck <= L and len(que_bridge) < W:
        que_bridge.append(que_truck.popleft())
    else:
        que_bridge.append(0)
    cnt += 1

print(cnt + W)



