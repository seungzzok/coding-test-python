import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
list = [int(sys.stdin.readline()) for _ in range(n)]

if n == 1:
    print(list[0])
else:
    first = list[0]
    second = list[1]

    dp = [first + second, first, second, 0]

    for i in range(2, n):
        temp = [0] * 4

        temp[0] = dp[2] + list[i]
        temp[1] = max(dp[0], dp[2])
        temp[2] = max(dp[1], dp[3]) + list[i]
        temp[3] = dp[1]

        dp = temp

    print(max(dp))

# ========== 메모 ==========
# 맞췄드앙~! 모든 경우의 수만 잘 생각해서 고려해주면 풀 수 있음
