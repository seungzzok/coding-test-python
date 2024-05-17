from collections import deque
import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
list = [sys.stdin.readline().strip().split() for _ in range(n)]

queue = deque()
ans = []

for i in list:
    cmd = i[0]

    if cmd == "push_front":
        queue.appendleft(i[1])
    if cmd == "push_back":
        queue.append(i[1])
    if cmd == "pop_front":
        ans.append(queue.popleft() if len(queue) != 0 else -1)
    if cmd == "pop_back":
        ans.append(queue.pop() if len(queue) != 0 else -1)
    if cmd == "size":
        ans.append(len(queue))
    if cmd == "empty":
        ans.append(1 if len(queue) == 0 else 0)
    if cmd == "front":
        ans.append(queue[0] if len(queue) != 0 else -1)
    if cmd == "back":
        ans.append(queue[-1] if len(queue) != 0 else -1)


print("\n".join(map(str, ans)))

# ========== 메모 ==========
# 맞았드앙~ deque 쓰는법 까먹지 말자!!