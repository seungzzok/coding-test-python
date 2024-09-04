import sys

sys.stdin = open("input.txt", "r")
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

s1_len = len(s1) + 1
s2_len = len(s2) + 1
dp = [[0] * (s2_len) for _ in range(s1_len)]

for r in range(1, s1_len):
    for c in range(1, s2_len):
        if s1[r - 1] == s2[c - 1]:
            dp[r][c] = dp[r - 1][c - 1] + 1
        else:
            dp[r][c] = max(dp[r][c - 1], dp[r - 1][c])

print(dp[s1_len - 1][s2_len - 1])

# ========== 메모 ==========
# LCS 알고리즘 개어렵네...
# 이거 이후 한번 더 복습 필요