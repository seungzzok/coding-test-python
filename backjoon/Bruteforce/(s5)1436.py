import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())

num = 666
cnt = 0

while True:
    if "666" in str(num):
        cnt += 1
    if cnt == n:
        break
    num += 1

print(num)

# 메모
# 아니 진짜 이거 개무식하게 푸네...?
# 더럽다고 생각한 그 코드가 맞을지도
# 그리고 input int처리 까먹지말고 꼭 하자
