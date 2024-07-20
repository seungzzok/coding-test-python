import sys
from collections import deque

sys.stdin = open("input.txt", "r")
n, k = map(int, sys.stdin.readline().strip().split())

# BFS를 위한 큐 초기화
queue = deque([n])
# 각 위치까지의 최단 시간을 저장할 배열 초기화
visited = [-1] * 100001
visited[n] = 0

while queue:
    pos = queue.popleft()

    if pos == k:
        print(visited[pos])
        break

    for next_pos in (pos - 1, pos + 1, pos * 2):
        if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
            visited[next_pos] = visited[pos] + 1
            queue.append(next_pos)


# ========== 메모 ==========
# 아놔 이건 무조건 BFS로 풀어야하네...
# DFS로 풀면 시간초과 뜸
# 함수 두개로 재귀형식으로 구할랬더만 메모리초과, 시간초과, 런타임오류 오만거 다뜸
# 최단 경로를 구할 때는 BFS를 사용하기!!


# ========== 이전 풀이 ==========
# min_time = 999999


# def walk(time, pos):
#     global min_time

#     time += 1
#     go = pos + 1
#     back = pos - 1

#     if go > 100000 or back > 100000 or min_time <= time:
#         return

#     if go == k or back == k:
#         min_time = time
#         return

#     if go <= k:
#         walk(time, go)
#         teleport(time, go)

#     walk(time, back)
#     teleport(time, back)


# def teleport(time, pos):
#     global min_time

#     time += 1
#     pos *= 2

#     if pos > k or min_time <= time:
#         return

#     if pos == k:
#         min_time = time
#         return

#     walk(time, pos)
#     teleport(time, pos)


# walk(0, n)
# teleport(0, n)

# print(min_time)
