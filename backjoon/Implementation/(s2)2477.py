import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(6)]
arr.append(arr[0])

width = 0
height = 0
empty_space = 0
last_dir = 0
last_len = 0

for idx in range(7):
    direction, length = arr[idx]

    # 전체 영역의 가로 세로길이 구하기
    if (direction == 1 or direction == 2) and width < length:
        width = length
    if (direction == 3 or direction == 4) and height < length:
        height = length

    # 빼야하는 영역 구하기
    if (
        (direction == 3 and last_dir == 1)
        or (direction == 4 and last_dir == 2)
        or (direction == 2 and last_dir == 3)
        or (direction == 1 and last_dir == 4)
    ):
        empty_space = last_len * length

    last_dir = direction
    last_len = length

print((width * height - empty_space) * n)


# ========== 메모 ==========
# 시작하는 곳의 가로 세로 부분을 계산안해서 틀림
# 처음 요소를 마지막 부분에 한번 더 넣어서 첫 부분까지 돌리면서 성공
