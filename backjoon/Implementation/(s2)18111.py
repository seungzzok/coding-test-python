import sys

sys.stdin = open("input.txt", "r")
n, m, b = map(int, sys.stdin.readline().strip().split())
ground = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

min_height = min(map(min, ground))
max_height = max(map(max, ground))
ans = []

for height in range(min_height, max_height + 1):
    minus = 0
    plus = 0

    for r in ground:
        for pos in r:
            if pos > height:
                plus += pos - height
            if pos < height:
                minus += height - pos

    if minus <= plus + b:
        time = minus + plus * 2
        ans.append([minus + plus * 2, height])
    else:
        break

ans.sort(key=lambda x: (x[0], -x[1]))

print(*ans[0])

# ========== 메모 ==========
# 아놔 진짜 반복문으로 시간초과 뜨면은 Pypy로 바꿔서 제출해보자
# 내가 작성한 코드가 답지보다 훨씬 더 효율적인데 댕빡치네 씨
