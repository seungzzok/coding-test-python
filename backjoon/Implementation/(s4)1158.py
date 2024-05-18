import sys
from collections import deque

sys.stdin = open("input.txt", "r")
n, k = map(int, sys.stdin.readline().strip().split())

people = [i + 1 for i in range(n)]
people = deque(people)
ans = []

while len(people):
    for _ in range(k - 1):
        people.append(people.popleft())
    ans.append(people.popleft())

print(f"<{', '.join(map(str,ans))}>")

# ========== 메모 ==========
# 아아아아 드디어 맞췄다...!
# pop(0)을 써야하는 경우(선입선출)라면은 걍 닥치고 deque 쓰자... 시간절약할 수 있음
