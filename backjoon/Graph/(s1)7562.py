import sys
from collections import deque

sys.stdin = open("input.txt", "r")
case_num = int(sys.stdin.readline())


def findMinMovement():
    length = int(sys.stdin.readline())
    start_row, start_col = map(int, sys.stdin.readline().strip().split())
    end_row, end_col = map(int, sys.stdin.readline().strip().split())

    queue = deque([[start_row, start_col]])
    visited = [[-1 for _ in range(length)] for _ in range(length)]
    next_row_list = [2, 1, -1, -2, -1, -2, 1, 2]
    next_col_list = [1, 2, 2, 1, -2, -1, -2, -1]

    visited[start_row][start_col] = 0

    while queue:
        [now_row, now_col] = queue.popleft()

        if now_row == end_row and now_col == end_col:
            print(visited[now_row][now_col])
            break

        for i in range(8):
            next_row = now_row + next_row_list[i]
            next_col = now_col + next_col_list[i]

            if (
                0 <= next_row < length
                and 0 <= next_col < length
                and visited[next_row][next_col] == -1
            ):
                visited[next_row][next_col] = visited[now_row][now_col] + 1
                queue.append([next_row, next_col])


for _ in range(case_num):
    findMinMovement()

# ========== 메모 ==========
# 아싸 한번에 맞췄다ㅎㅎ
# 최단경로 구하는 문제는 반드시 BFS 사용하기!!
