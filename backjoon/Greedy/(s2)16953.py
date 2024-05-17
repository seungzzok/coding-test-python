import sys

sys.stdin = open("input.txt", "r")
a, b = map(int, sys.stdin.readline().strip().split())

min_cnt = 1000


def multiple(n, cnt):
    global min_cnt
    n *= 2
    cnt += 1

    if n > b:
        return

    if n == b:
        if min_cnt > cnt:
            min_cnt = cnt
        return

    if n < b:
        multiple(n, cnt)
        add(n, cnt)


def add(n, cnt):
    global min_cnt
    n = n * 10 + 1
    cnt += 1

    if n > b:
        return

    if n == b:
        if min_cnt > cnt:
            min_cnt = cnt
        return

    if n < b:
        multiple(n, cnt)
        add(n, cnt)


multiple(a, 0)
add(a, 0)

print(min_cnt + 1 if min_cnt != 1000 else -1)

# ========== 메모 ==========
# 우와 이것도 한번에 맞췄어ㅋㅋㅋㅋ 꽤나 복잡한뎅
# 오늘 되게 잘풀리네

# ========== 다른 풀이 ==========
# a, b = map(int, input().split())
# r = 1
# while b != a:
#     r += 1
#     temp = b
#     if b % 10 == 1:
#         b //= 10
#     elif b % 2 == 0:
#         b //= 2

#     if temp == b:
#         print(-1)
#         break
# else:
#     print(r)

# 다이나믹 프로그래밍 top-down 형식으로 풀었음