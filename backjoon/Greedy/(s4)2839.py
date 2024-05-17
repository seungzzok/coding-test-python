import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
max = n // 5

cnt = [0, 0]
no_rest = False

for i in range(max, -1, -1):
    test = n
    test -= 5 * i
    cnt = [i, test // 3]
    test %= 3

    if test == 0:
        no_rest = True
        break

print(sum(cnt) if no_rest else -1)

# 메모
# 아... 맞췄다ㅠ
# 코드 쪼매 더럽긴한데 그래도 맞춘게 어디야