import sys

sys.stdin = open("input.txt", "r")
t = int(sys.stdin.readline())


def maxProfit():
    n = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().strip().split()))
    maxPrice = 0
    profit = 0

    for i in prices[::-1]:
        if maxPrice < i:
            maxPrice = i

        profit += maxPrice - i

    print(profit)


for i in range(t):
    maxProfit()

# ========== 메모 ==========
# 아 리스트 방향을 역순으로 돌리는 방법도 생각해보자!!
