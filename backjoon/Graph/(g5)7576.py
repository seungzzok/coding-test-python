import sys
from collections import deque

sys.stdin = open("input.txt", "r")
m, n = map(int, sys.stdin.readline().strip().split())

ans = -1
box = []
next_row_list = [0, 0, 1, -1]
next_col_list = [1, -1, 0, 0]
queue = deque()

# box 저장하면서 시작위치 찾기
for r in range(n):
    one_row = list(map(int, sys.stdin.readline().strip().split()))
    box.append(one_row)

    for c in range(len(one_row)):
        if one_row[c] == 1:
            queue.append([r, c])


# BFS로 최단 기간 입력하기
while queue:
    [now_row, now_col] = queue.popleft()

    for i in range(4):
        next_row = now_row + next_row_list[i]
        next_col = now_col + next_col_list[i]

        if 0 <= next_row < n and 0 <= next_col < m and box[next_row][next_col] == 0:
            box[next_row][next_col] = box[now_row][now_col] + 1
            queue.append([next_row, next_col])

# box 한바퀴 돌면서 최단기간 찾기
for r in range(n):
    for c in range(m):
        pos = box[r][c]

        if pos == 0:
            ans = 0
            break

        if ans < pos:
            ans = pos

    if ans == 0:
        break


print(ans - 1)


# ========== 메모 ==========
# 하ㅠㅠ 한번에 맞췄당..
# 제법 복잡해서 작성하는데 오래걸리긴 했지만
# BFS 알고리즘만 제대로 사용하면 되는 문제라 어렵진 않았음
