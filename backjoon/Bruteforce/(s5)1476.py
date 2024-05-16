import sys

sys.stdin = open("input.txt", "r")
E, S, M = map(int, sys.stdin.readline().strip().split())

ans = 1

e, s, m = 1, 1, 1

while True:
    if [E, S, M] == [e, s, m]:
        break
    else:
        e = e + 1 if e < 15 else 1
        s = s + 1 if s < 28 else 1
        m = m + 1 if m < 19 else 1
        ans += 1

print(ans)

# 메모
# e, s, m = 1, 1, 1 <- 이런식으로 한번에 값 지정 가능
# [E, S, M] == [e, s, m] <- 이런식으로 한번에 비교도 가능
# e = e + 1 if e < 15 else 1 <- 삼항연산자 사용방법

# strip()을 사용해서 반드시 '\n' 값을 없애줘야함!
# 우와... 한번에 맞췄어..
# 파이썬 편하긴한데 좀만 더 적응해보자...
