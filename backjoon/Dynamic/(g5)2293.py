import sys

sys.stdin = open("input.txt", "r")
n, k = map(int, sys.stdin.readline().strip().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = dp[i] + dp[i - coin]


print(dp[k])

# ========== 메모 ==========
# DP 문제풀이 방법
# 1) 문제를 작게 나눠서 보기
# 2) 점화식 찾기

# 점화식 찾는게 많이 어렵네ㅠㅠ 점화식만 잘 찾으면은 다 해결할 수 있음!!
