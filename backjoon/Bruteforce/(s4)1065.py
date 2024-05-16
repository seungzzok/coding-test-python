import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
cnt = 0


def fn(n):
    if n < 100:
        return True
    else:
        str_num = str(n)
        gap = int(str_num[1]) - int(str_num[0])
        for i in range(len(str_num) - 1):
            if int(str_num[i + 1]) - int(str_num[i]) != gap:
                return False

        return True


for i in range(1, n + 1):
    cnt += 1 if fn(i) else 0

print(cnt)

# 메모
# 이것도 한번에 맞췄당ㅎㅎ
# 아 알고리즘 생각안하고 무식하게 돌리면 되니까 너무 편하당