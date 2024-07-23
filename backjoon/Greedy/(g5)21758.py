import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
places = list(map(int, sys.stdin.readline().strip().split()))

ans = 0
sum_places = []
sum_places.append(places[0])

# 누적합 배열 만들기
for i in range(1, n):
    sum_places.append(sum_places[i - 1] + places[i])

# 벌 하나는 반드시 한쪽 끝에서 시작해야함
# 1. 꿀벌벌
for i in range(1, n - 1):
    temp = (sum_places[i - 1]) + (sum_places[-1] - places[-1] - places[i])
    ans = max(ans, temp)

# 2. 벌벌꿀
for i in range(1, n - 1):
    temp = (sum_places[-1] - places[0] - places[i]) + (sum_places[-1] - sum_places[i])
    ans = max(ans, temp)

# 3. 벌꿀벌
for i in range(1, n - 1):
    temp = (sum_places[i] - places[0]) + (
        sum_places[-1] - sum_places[i - 1] - places[-1]
    )
    ans = max(ans, temp)

print(ans)

# ========== 메모 ==========
# 값들의 합을 필요로 하는 경우에는 누적합 배열을 만드는 것이 시간 단축에 효과적!!
# 벌과 벌통(꿀)의 위치의 경우를 나눠서 각각의 경우에 얻을 수 있는 꿀들을 전부 구해서
# 최댓값을 구하는 식으로 풀음
# 냅다 전부다 돌려도 시간초과가 안뜨는게 그저 신기하네...
