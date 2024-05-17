import sys

sys.stdin = open("input.txt", "r")
n, price = list(map(int, sys.stdin.readline().strip().split()))
coins = [int(sys.stdin.readline()) for _ in range(n)]
coins = sorted(coins, reverse=True)

cnt = 0

for i in coins:
    cnt += price // i
    price = price % i
    if price == 0:
        break

print(cnt)

# 메모
# 와웅... 또 맞췄당...ㅎㅎ
