import sys

sys.stdin = open("input.txt", "r")
n, m = list(map(int, sys.stdin.readline().strip().split()))
a = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
b = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

cnt = 0


def turn(row, col):
    for r in range(row, row + 3):
        for c in range(col, col + 3):
            a[r][c] = 0 if a[r][c] == 1 else 1


if n >= 3 or m >= 3:
    for r in range(n - 2):
        for c in range(m - 2):
            if a[r][c] != b[r][c]:
                cnt += 1
                turn(r, c)

print(cnt if a == b else -1)

# ========== 메모 ==========
# 걍 못풀것 같아서 바로 답지 참고해서 풀었음
# 로직 보니까 최솟값 찾기 위한 노력없이 그냥 처음부터 끝까지 전부 돌려보는게 답이넹
# 이런 문제 나오면은 최솟값이고 뭐고 그냥 전부 돌리자

# 띄워쓰기 없는 경우에는 바로 list()로 string을 감싸면 배열로 변환해줌
