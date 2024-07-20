import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

graph = [list() for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
cnt = 0

for a, b in arr:
    graph[a].append(b)
    graph[b].append(a)


def DFS(node):
    global graph, visited, cnt

    if visited[node]:
        return

    visited[node] = True
    cnt += 1

    for i in graph[node]:
        DFS(i)


DFS(1)

print(cnt - 1)

# ========== 메모 ==========
# DFS BFS 보통 둘중에 하나만 써서 사용해도 되는 경우가 많음
# 난 DFS의 재귀함수 사용해서 그래프 문제 푸는걸루 정하자 (제일 깔끔하고 간편함)
# 혹시나 stack을 사용해서 DFS나 BFS를 풀어야 한다면 무조건 deque() 사용하기!!

# 간단한 원리
# DFS: stack에 이후에 넣은 순서대로 빼기 (pop())
# BFS: stack에 먼저 넣은 순서대로 빼기 (popleft())

# 파이썬 문법
# boolean 반대값을 나타내는 연산자가 '!'가 아니라 'not'을 앞에 붙여줘야함!!