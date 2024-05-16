import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

def get_rank(arr, all):
    cnt = 1
    for i in all:
        if arr[0] < i[0] and arr[1] < i[1]:
            cnt += 1
    return cnt

for i in data:
    print(get_rank(i, data), end=" ")

# 메모
# 이제 좀 알겠다. 아아니 진짜 파이썬 기본 설정하는데만 해도 개오래걸림;;;
# 제일 처음 input값 불러올 때 int처리 꼭 해주기!!!
