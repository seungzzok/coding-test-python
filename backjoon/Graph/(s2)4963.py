import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
w, h = -1, -1


def findIsland():
    global w, h

    w, h = map(int, sys.stdin.readline().strip().split())
    island = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(h)]

    if w == 0 and h == 0:
        return

    cnt = 0
    next_row_list = [1, -1, 0, 0, 1, 1, -1, -1]
    next_col_list = [0, 0, 1, -1, 1, -1, 1, -1]

    def DFS(r, c):
        if island[r][c] == 0:
            return

        island[r][c] = 0

        for i in range(8):
            next_row = r + next_row_list[i]
            next_col = c + next_col_list[i]

            if (
                next_row >= 0
                and next_row < h
                and next_col >= 0
                and next_col < w
                and island[next_row][next_col] == 1
            ):
                DFS(next_row, next_col)

    for r in range(h):
        for c in range(w):
            if island[r][c] == 1:
                DFS(r, c)
                cnt += 1

    print(cnt)


while True:
    findIsland()

    if w == 0 and h == 0:
        break

# ========== 메모 ==========
# DFS 써서 한번에 맞춤ㅎㅎ
# 런타임 에러 해결방안: sys.setrecursionlimit(10**6) 추가해주기
# 시간초과 해결방안: BFS 방법 사용해보기
