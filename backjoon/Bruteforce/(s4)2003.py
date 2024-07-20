import sys
from collections import deque

sys.stdin = open("input.txt", "r")
n, m = map(int, sys.stdin.readline().strip().split())
arr = deque(list(map(int, sys.stdin.readline().strip().split())))
arr.append(0)

ans = 0
temp_list = deque()

while arr:
    temp_sum = sum(temp_list)

    if temp_sum < m:
        temp_list.append(arr.popleft())
    elif temp_sum == m:
        ans += 1
        temp_list.popleft()
    elif temp_sum > m:
        temp_list.popleft()


print(ans)

# ========== 메모 ==========
# 무작정 노가다해서 돌리니까 시간초과떠서 리스트로 숫자들을 관리하는 방식으로 풀었음
# list보다 deque를 사용해서 관리하는게 시간효율성이 높아서 채택하여 사용
# 맨 마지막 남은 리스트에 대해서도 한번 더 검증을 해야하기 때문에 arr.append(0) 추가
