import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().strip().split()))

dp = [0] * n
dp[0] = list[0]

for i in range(1, n):
    if dp[i - 1] < 0:
        dp[i] = list[i]
    else:
        dp[i] = dp[i - 1] + list[i]

print(max(dp))

# ========== 메모 ==========
# 맞췄다아아~~
# 규칙만 찾아내면 됨