import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")
n, s = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

ans = 0

for i in range(1, n + 1):
    comb = combinations(arr, i)

    for j in comb:
        if sum(j) == s:
            ans += 1

print(ans)

# ========== 메모 ==========
# 부분수열이 순서대로가 아니더라도 해당된다는 사실을 몰랐음
# 음수가 들어가있기 때문에 무조건 전체를 다 돌려야 확인이 가능함
# 모든 경우의 조합을 구하려고 하는 경우 combinations library 사용하기!! (처음 알았음)