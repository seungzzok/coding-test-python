import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, sys.stdin.readline().strip().split())
rectangle = [list(sys.stdin.readline().strip()) for _ in range(n)]
min_len = min(n, m)

max_size = 1

for r in range(n):
    for c in range(m):
        num = rectangle[r][c]
        for len in range(1, min_len):
            if r + len >= n or c + len >= m:
                continue

            if (
                num
                == rectangle[r + len][c]
                == rectangle[r][c + len]
                == rectangle[r + len][c + len]
            ):
                if max_size < (len + 1) ** 2:
                    max_size = (len + 1) ** 2

print(max_size)

# ========== 메모 ==========
# ㅎㅎㅎ 한번에 맞췄드앙~!~! 브루트포스 엥간 알겠쥬
