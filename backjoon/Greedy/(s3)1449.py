import sys

sys.stdin = open("input.txt", "r")
n, length = map(int, sys.stdin.readline().strip().split())
locs = list(map(int, sys.stdin.readline().strip().split()))
locs = sorted(locs)

cnt = 0
loc = 1


for i in locs:
    if i >= loc:
        cnt += 1
        loc = i + length
    else:
        continue


print(cnt)

# ========== 메모 ==========
# 맞췄드아아앙~!
# while 쓰는 것보다 for문으로 하는게 훨씬 더 직관적이고 풀기 편한듯
