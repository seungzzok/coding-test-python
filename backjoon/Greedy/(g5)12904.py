import sys

sys.stdin = open("input.txt", "r")
s = sys.stdin.readline().strip()
t = list(sys.stdin.readline().strip())
len_s = len(s)

while len_s != len(t):
    str = t.pop()
    if str == "A":
        continue
    if str == "B":
        t.reverse()

t = "".join(t)

print(1 if s == t else 0)

# ========== 메모 ==========
# 이거 답안지 참고함
# S를 T로 바꾸기 위해서 재귀함수를 쓰는 방법이 아니라 (첫번째 시도)
# T를 S로 바꾸고 나서 비교하는것이 훨씬 효율적 (두번째 시도)
