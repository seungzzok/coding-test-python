import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())

dp = [0] * 1000001

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)


print(dp[n])

# ==========  메모 ==========
# 다이나믹 프로그래밍 bottom-up 개념 익히기
# 이전에 만들어놨던 로직을 재활용하는 개념