import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, sys.stdin.readline().strip().split())
r, c, dir = map(int, sys.stdin.readline().strip().split())
room = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

cnt = 0


def move(block):
    global r, c, dir

    if dir == 0:  # 북쪽
        r -= block
    if dir == 1:  # 동쪽
        c += block
    if dir == 2:  # 남쪽
        r += block
    if dir == 3:  # 서쪽
        c -= block


def check():
    global r, c, dir

    if dir == 0:  # 북쪽
        return room[r - 1][c] == 0
    if dir == 1:  # 동쪽
        return room[r][c + 1] == 0
    if dir == 2:  # 남쪽
        return room[r + 1][c] == 0
    if dir == 3:  # 서쪽
        return room[r][c - 1] == 0


while True:
    # 작동 중지
    if room[r][c] == 1:
        break

    # 1번
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1

    # 3번: 주변 4칸 중 청소되지 않는 빈칸이 있는 경우
    if (
        room[r - 1][c] == 0
        or room[r + 1][c] == 0
        or room[r][c - 1] == 0
        or room[r][c + 1] == 0
    ):
        dir = dir - 1 if dir > 0 else 3
        if check():
            move(1)

    # 2번: 주변 4칸 중 청소되지 않은 빈칸이 없는 경우
    else:
        move(-1)

print(cnt)


# ========== 메모 ==========
# 으아아아 맞았다아~!~!
# 복잡하디 복잡하다... 시간만 주어진다면 충분히 풀 수 있을만한 구현문제
