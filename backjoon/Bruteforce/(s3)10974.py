import sys

sys.stdin = open("input.txt", "r")
N = int(sys.stdin.readline())

stack = []


def dfs():
    if len(stack) == N:
        print(*stack)
        return

    for i in range(1, N + 1):
        if i not in stack:
            stack.append(i)
            dfs()
            stack.pop()


dfs()

# 메모
# DFS 파이썬으로 구현할 수 있어야함....
# *을 배열앞에 붙이면은 전부 알아서 풀어줌... 혁명아냐...?
# *을 string앞에 붙여도 각 string을 전부 풀어줌..
