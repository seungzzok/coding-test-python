import sys

sys.stdin = open("input.txt", "r")
arr = sys.stdin.readline().strip().split("-")

ans = 0

for idx, item in enumerate(arr):
    num = sum(map(int, item.split("+")))
    if idx > 0:
        ans -= num
    else:
        ans += num

print(ans)

# ========== 메모 ==========
# 맞췄드앙~!~!
