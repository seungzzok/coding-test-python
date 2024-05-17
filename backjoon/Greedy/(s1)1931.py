import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
meetings = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))

end = 0
cnt = 0

for meeting in meetings:
    if meeting[0] >= end:
        end = meeting[1]
        cnt += 1


print(cnt)


# ========== 메모 ==========
# 끝나는걸 기준으로 정렬시키면 되네...?
# 요 아이디어 기억하기...!

# sorted() vs sort(): sorted는 새로운 정렬된 배열을 반환하고 sort는 원본을 정렬시킴
# 특정 값을 기준으로 정렬시키고 싶다면 Key= 속성을 사용할 수 있음!!
# 정렬 기준을 복수로 설정할 수도 있음!

# ========== 이전 풀이 ==========
# max_time = max([meetings[i][1] for i in range(n)])
# max_cnts = [0 for _ in range(max_time + 1)]


# def counting(time, cnt):
#     global max_cnts
#     if max_cnts[time] > cnt:
#         return

#     for meeting in meetings:
#         if time <= meeting[0]:
#             counting(meeting[1], cnt + 1)

#     if max_cnts[time] < cnt:
#         max_cnts[time] = cnt


# counting(0, 0)

# print(max_cnts[-1])

# 이전에 dynamic programming에서 배웠던 대로 써봤는데 시간초과 떴음
