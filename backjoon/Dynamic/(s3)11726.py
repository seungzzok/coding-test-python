import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)

# ========== 메모 ==========
# 다이나믹 프로그래밍에서는 규칙 찾아내는게 제일 어려운 관건일듯!
# 규칙만 찾아내면 쉽게 사용 가능