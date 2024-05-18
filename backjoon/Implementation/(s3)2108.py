import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()


def avg(arr):
    return int(round(sum(arr) / len(arr), 0))


def medium(arr):
    mid_idx = len(arr) / 2
    return arr[int(mid_idx)]


def most(arr):
    cnts = dict()
    for num in arr:
        if num in cnts:
            cnts[num] += 1
        else:
            cnts[num] = 1

    max_cnt = max(cnts.values())
    max_nums = []

    for i in cnts:
        if cnts[i] == max_cnt:
            max_nums.append(i)

    return max_nums[0] if len(max_nums) == 1 else max_nums[1]


def range(arr):
    return arr[-1] - arr[0]


print(avg(nums))
print(medium(nums))
print(most(nums))
print(range(nums))

# ========== 메모 ==========
# 아놔... 진짜 Dictionary 사용해서 풀어야하는 문제였음
# 그냥 JS에서 객체랑 똑같다고 보면 될듯
# 아니 왤캐 알아야할게 많이 생기냐고요....


# ========== 이전 풀이 ==========
# def most(arr):
#     temp_arr = [i for i in arr]
#     max_nums = []
#     max_cnt = 1
#     temp_cnt = 0

#     while len(temp_arr):
#         cur = temp_arr.pop(0)
#         temp_cnt += 1

#         if len(temp_arr) == 0 or cur != temp_arr[0]:
#             if temp_cnt > max_cnt:
#                 max_nums = []
#                 max_nums.append(cur)
#                 max_cnt = temp_cnt
#             elif temp_cnt == max_cnt:
#                 max_nums.append(cur)

#             temp_cnt = 0

#     return max_nums[0] if len(max_nums) == 1 else max_nums[1]
