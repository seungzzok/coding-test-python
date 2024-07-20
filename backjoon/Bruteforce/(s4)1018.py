import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, sys.stdin.readline().strip().split())
board = [sys.stdin.readline().strip() for _ in range(n)]

minNum = n * m


def isWBboard(r, c):
    if (r % 2 == 0 and c % 2 == 0) or (r % 2 != 0 and c % 2 != 0):
        if board[r][c] == "W":
            return True
        else:
            return False
    if (r % 2 != 0 and c % 2 == 0) or (r % 2 == 0 and c % 2 != 0):
        if board[r][c] == "B":
            return True
        else:
            return False


# 8*8만큼 잘라내기
for i in range(n - 7):
    for j in range(m - 7):
        # 최소로 뒤집어야 하는 칸 개수세기
        WBnum, BWnum = 0, 0
        for r in range(i, i + 8):
            for c in range(j, j + 8):
                if isWBboard(r, c):
                    BWnum += 1
                else:
                    WBnum += 1

        minNum = min(WBnum, BWnum, minNum)

print(minNum)

# ========== 메모 ==========
# 우와.. 개무식하게 풀었는데 맞췄다...ㅎ
# 리스트에 모든 숫자를 다 넣고 한번에 min(list) 해도 됨