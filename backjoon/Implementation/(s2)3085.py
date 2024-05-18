import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

max_cnt = 0


def move(prev_row, prev_col, next_row, next_col):
    temp = graph[prev_row][prev_col]
    graph[prev_row][prev_col] = graph[next_row][next_col]
    graph[next_row][next_col] = temp


def check(row, col):
    global max_cnt

    if row == 0:
        for c in range(col, col + 2):
            cnt = 1
            color = graph[0][c]
            # 세로로 연속된 색상 비교
            for r in range(1, n):
                if color == graph[r][c]:
                    cnt += 1
                    if r == n - 1 and max_cnt < cnt:
                        max_cnt = cnt
                else:
                    if max_cnt < cnt:
                        max_cnt = cnt
                    color = graph[r][c]
                    cnt = 1

    if col == 0:
        for r in range(row, row + 2):
            cnt = 1
            color = graph[r][0]
            # 가로로 연속된 색상 비교
            for c in range(1, n):
                if color == graph[r][c]:
                    cnt += 1
                    if c == n - 1 and max_cnt < cnt:
                        max_cnt = cnt
                else:
                    if max_cnt < cnt:
                        max_cnt = cnt
                    color = graph[r][c]
                    cnt = 1

    return


for r in range(n):
    for c in range(n):
        if c < n - 1:
            # 가로 이동
            move(r, c, r, c + 1)
            check(0, c)
            move(r, c, r, c + 1)

        if r < n - 1:
            # 세로 이동
            move(r, c, r + 1, c)
            check(r, 0)
            move(r, c, r + 1, c)

        if max_cnt == n:
            break

    if max_cnt == n:
        break

print(max_cnt)

# ========== 메모 ==========
# 한번에 맞췄드앙~!~!
