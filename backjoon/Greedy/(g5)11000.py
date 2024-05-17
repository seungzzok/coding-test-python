import sys
import heapq

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
timeline = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
timeline.sort(key=lambda x: (x[0], x[1]))

room = [0]

for time in timeline:
    if time[0] < room[0]:
        heapq.heappush(room, time[1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, time[1])

print(len(room))

# ========== 메모 ==========
# heap 자료구조 알아보자... 진짜 알아야 할거 드릅게 많네
# 시간초과떠서 다른 풀이 참고함

# 로직
# 1. 강의 순서대로 돌면서 들을 수 있는 강의실이 있는 경우 end time이 가장 빠른 강의실에 배정
# 2. 들을 수 있는 강의실이 없는 경우 새로운 강의실 파기
# 3. end time이 가장 빠른 경우를 쉽게 찾아야 하기 때문에 heap구조 사용해서 시간복잡도 줄임



# ========== 이전 풀이 ==========
# cnt = 0

# while len(timeline) != 0:
#     end = 0
#     temp_timeline = []
#     cnt += 1

#     for time in timeline:
#         if end <= time[0]:
#             end = time[1]
#         else:
#             temp_timeline.append(time)

#     timeline = temp_timeline

# print(cnt)

# 로직: 하나의 강의실에서 이용할 수 있는 모든 시간표를 순서대로 할당하며 진행
# -> 효율적으로 강의실을 사용하지 못하는 경우가 발생할 수 있음
