import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))

ans = 0

a.sort()
b.sort(reverse=True)

for i in range(n):
    ans += a[i] * b[i]

print(ans)

# ========== 메모 ==========
# 뭐야.. 엄청 쉽게 맞춤..
