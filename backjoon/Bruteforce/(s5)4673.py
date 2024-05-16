def constructor(n):
    return n + sum(map(int, str(n)))

range_num = 10000
is_self_num = [True] * (range_num)

for i in range(1, range_num):
    if constructor(i) < range_num :
        is_self_num[constructor(i)] = False

for idx, self_num in enumerate(is_self_num):
    if self_num and idx > 0:
        print(idx)

# 메모
# 진짜 파이썬 너무... 익숙하지가 않아...ㅠ

# 모범답안
All = set(i for i in range(1, 10001))
S= set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    S.add(i)

for i in sorted(All - S):
    print(i)