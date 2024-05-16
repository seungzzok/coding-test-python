import sys

sys.stdin = open("input.txt", "r")
N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

dp = [0 for _ in range(N + 1)]

for i in range(N):
    for j in range(i + data[i][0], N + 1):
        if dp[j] < dp[i] + data[i][1]:
            dp[j] = dp[i] + data[i][1]

print(dp[-1])

# 메모
# 다이나믹 프로그래밍 나와서 갑자기 개어려워짐...
# 나중에 DP 문제 풀 때 다시한번 생각해보자
# -> 푸는법: 배열을 생성해서 계속 변동하는 값으로 대체해가면서 풀기
# ddd