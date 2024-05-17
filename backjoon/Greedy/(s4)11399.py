import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
times = sorted(list(map(int, sys.stdin.readline().strip().split())))

ans = 0
temp = 0

for i in times:
    temp += i
    ans += temp

print(ans)

# 메모
# 엥...? 바로 맞췄다... 이거 난이도 브론즈 아냐..? 엄청 쉽네
