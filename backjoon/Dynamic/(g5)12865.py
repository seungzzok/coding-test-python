import sys

sys.stdin = open("input.txt", "r")
n, k = map(int, sys.stdin.readline().strip().split())
items = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dp = [0] * (k + 1)

for [w, v] in items:
    temp = dp.copy()

    for i in range(1, k + 1):
        if dp[i] != 0 and i + w <= k:
            temp[i + w] = max(dp[i + w], dp[i] + v)

    if w <= k:
        temp[w] = max(dp[w], v)

    dp = temp


print(max(dp))

# ========== 메모 ==========
# 내가 생각했던 로직이 맞았음ㅠ
# index 에러처리 주의하기!!
# 바로 dp의 값을 변경시키는것이 아니라 temp에다가 작업을 한 이후에 원데이터에 덮어씌우기