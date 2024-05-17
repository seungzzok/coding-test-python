import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
road_lens = list(map(int, sys.stdin.readline().strip().split()))
oil_prices = list(map(int, sys.stdin.readline().strip().split()))

min_price = oil_prices[0]
ans = 0

for i in range(n - 1):
    if min_price > oil_prices[i]:
        min_price = oil_prices[i]
    ans += min_price * road_lens[i]

print(ans)


# ========== 메모 ==========
# 하놔....ㅎㅎ 이렇게 쉽게 풀 수 있는 방법이 있는데 너무 어렵게 풀었네
# 부분 성공이어서 다시 고쳐서 작성함
# index 구하는 법: arr.index(char)
# 특정 구간 slice 하는 법: arr[start:end] -> end는 포함안됨
# 처음부터 특정 index까지 slice: arr[:end]
# 특정 index부터 끝까지 slice: arr[star:]

# ========== 내 풀이 ==========
# min_oil_prices = [0 for _ in range(n - 1)]

# ans = 0
# cur_idx, last_idx = n, n

# while cur_idx != 0:
#     min_oil_price = min(oil_prices[:last_idx])
#     cur_idx = oil_prices[:last_idx].index(min_oil_price)

#     for i in range(cur_idx, last_idx):
#         if i < n - 1:
#             min_oil_prices[i] = min_oil_price
#     last_idx = cur_idx

# for i in range(n - 1):
#     ans += road_lens[i] * min_oil_prices[i]

# print(ans)
