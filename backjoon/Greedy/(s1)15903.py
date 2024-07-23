import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, sys.stdin.readline().strip().split())
cards = list(map(int, sys.stdin.readline().strip().split()))

for i in range(m):
    cards.sort()
    sumNum = cards[0] + cards[1]
    cards[0] = sumNum
    cards[1] = sumNum


print(sum(cards))

# ========== 메모 ==========
# 엥.....?
# sort()가 시간복잡도가 높아서 당연히 실패할줄 알았는데 한번에 맞춰서 좀 당황스럽...