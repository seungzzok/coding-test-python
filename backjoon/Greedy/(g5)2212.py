import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensors = list(map(int, sys.stdin.readline().strip().split()))
sensors.sort()

distances = []

for i in range(len(sensors) - 1):
    distance = sensors[i + 1] - sensors[i]
    distances.append(distance)

distances.sort()


print(sum(distances[: n - k]))

# ========== 메모 ==========
# 와... 이건 ㄹㅇ 아이디어 싸움이네..
# 군집으로 나눠서 거리의 중간을 구할때에는 각 지점간의 거리의 오름차순을 한 후에 가장 거리가 큰걸 제외하고 더하기
