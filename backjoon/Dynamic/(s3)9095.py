import sys

sys.stdin = open("input.txt", "r")
case_num = int(sys.stdin.readline())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for i in range(case_num):
    n = int(sys.stdin.readline())
    print(dp[n])

# ========== 메모 ==========
# 다이나믹 프로그래밍 bottom-up 로직 사용해서 한번에 품