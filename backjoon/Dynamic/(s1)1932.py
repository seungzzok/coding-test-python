import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dp = list[0]

for i in range(1, n):
    cur = list[i]

    for j in range(i + 1):
        if j == 0:
            cur[j] += dp[j]
        elif j == i:
            cur[j] += dp[j - 1]
        else:
            cur[j] += max(dp[j - 1], dp[j])

    dp = cur

print(max(dp))

# ========== 메모 ==========
# 맞췄다아ㅎㅎ
# 가능한 모든 경우의 수를 다 만드어준 다음에 비교
