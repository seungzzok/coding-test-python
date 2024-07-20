import sys
from collections import deque

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
ans = deque()

while arr:
    ans.insert(arr.pop(), n)
    n -= 1

print(*list(ans))

# ========== 메모 ==========
# 오웅 이것도 한방에 맞춤ㅎㅎ
# 오랜만에 푸는데도 제법 잘풀리넹
# 특정 index에 삽입하는 경우에도 deque.insert 사용하기!!
