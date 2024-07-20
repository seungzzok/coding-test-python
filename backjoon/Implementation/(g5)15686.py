import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")
n, m = map(int, sys.stdin.readline().strip().split())
city = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

home = []
chicken = []
min_distance = 999999

# 집과 치킨집 위치 구하기
for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            home.append([r, c])
        if city[r][c] == 2:
            chicken.append([r, c])

# 치킨거리 구하기
for i in combinations(chicken, m):
    temp = 0
    for j in home:
        dist = 999
        for k in range(m):
            dist = min(dist, abs(i[k][0] - j[0]) + abs(i[k][1] - j[1]))
        temp += dist

    min_distance = min(min_distance, temp)

print(min_distance)

# ========== 메모 ==========
# combinations를 써서 모든 경우를 다 비교해봐야 하는 문제였다...
# 아니 왤캐 새로운 라이브러리가 이렇게 끝도 없이 나오는거임?? 화가나네


# ========== 이전 풀이 ==========
# # 치킨거리 구하기
# for i in chicken:
#     temp = []
#     for j in home:
#         temp.append(abs(i[0] - j[0]) + abs(i[1] - j[1]))

#     distance.append(temp)

# # 치킨거리 최소가게 기준으로 폐업
# distance.sort(key=lambda x: sum(x))
# distance = distance[:m]

# # 치킨거리 최소값 구하기
# min_distance = [2500 for _ in range(len(home))]

# for i in distance:
#     for idx in range(len(i)):
#         if min_distance[idx] > i[idx]:
#             min_distance[idx] = i[idx]

# print(sum(min_distance))

# 기존 로직: 가게별 치킨거리의 최솟값이 가장 적은 치킨거리를 만든다고 생각
# 기존 로직 오류: 단순히 치킨거리의 합으로만 최솟값을 구할 수 없음 => 전체 다 돌려봐야함
