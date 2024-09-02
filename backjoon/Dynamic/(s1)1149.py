import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dp = list[0]

for i in range(1, n):
    temp = list[i]

    temp[0] = temp[0] + min(dp[1], dp[2])
    temp[1] = temp[1] + min(dp[0], dp[2])
    temp[2] = temp[2] + min(dp[0], dp[1])
    dp = temp


print(min(dp))

# ========== 메모 ==========
# 모범답안 참고해서 품
# 로직 되게 신기하당. 모든 경우의 수를 계속해서 다 더해서 값을 구해냄