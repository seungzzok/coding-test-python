import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())

arr = [0 if i**0.5 % 1 else 1 for i in range(n + 1)]  # 제곱수는 1로 저장

min_ = 4
for i in range(int(n**0.5), 0, -1):
    if arr[n]:  # n이 제곱수일 경우
        min_ = 1
        break
    elif arr[n - i**2]:  # 나머지가 제곱수일 경우
        min_ = 2
        break
    else:
        for j in range(int((n - i**2) ** 0.5), 0, -1):
            if arr[(n - i**2) - j**2]:  # 제곱수를 한번 더 뺀 나머지가 제곱수일 경우
                min_ = 3
print(min_)

# 메모
# 도저히 모르겠다. 그냥 배꼈다.
# 느끼는건데 그냥 다이나믹 프로그래밍 나오면 틀리자
# 제곱근 나타내는거 sqrt() 말고 num**0.5 로 표현하자!
