import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
case_num = int(sys.stdin.readline())


def test():
    m, n, k = map(int, sys.stdin.readline().strip().split())
    # 배추밭 만들기
    ground = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        c, r = map(int, sys.stdin.readline().strip().split())
        ground[r][c] = 1

    next_row_list = [-1, 1, 0, 0]
    next_col_list = [0, 0, -1, 1]
    cnt = 0

    def DFS(r, c):
        if ground[r][c] == 0:
            return

        ground[r][c] = 0

        for idx in range(4):
            next_row = r + next_row_list[idx]
            next_col = c + next_col_list[idx]

            if 0 <= next_row < n and 0 <= next_col < m:
                DFS(next_row, next_col)

    for r in range(n):
        for c in range(m):
            if ground[r][c] == 1:
                cnt += 1
                DFS(r, c)

    print(cnt)


for _ in range(case_num):
    test()

# ========== 메모 ==========
# 파이썬에는 재귀한도가 정해져있는데 처음 제출할 때는 재귀한도에 걸려서 런타임에러가 뜸
# sys.setrecursionlimit(10**6) <- 해당 코드를 사용해서 재귀한도 늘리면 런타임에러 안뜸
# 기본 재귀한도: 1000
