import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))
one_min = min(nums)
two_min = 10000
three_min = 10000
two_combi = [
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 2),
    (1, 3),
    (1, 5),
    (2, 4),
    (2, 5),
    (3, 4),
    (3, 5),
    (4, 5),
]
three_combi = [
    (0, 1, 2),
    (0, 1, 3),
    (0, 2, 4),
    (0, 3, 4),
    (1, 2, 5),
    (1, 3, 5),
    (2, 4, 5),
    (3, 4, 5),
]

if n == 1:
    print(sum(nums) - max(nums))
else:
    for a, b in two_combi:
        min = nums[a] + nums[b]
        if two_min > min:
            two_min = min

    for a, b, c in three_combi:
        min = nums[a] + nums[b] + nums[c]
        if three_min > min:
            three_min = min

    one_min_sum = one_min * (n - 2) * (n - 2) + one_min * (n - 2) * (n - 1) * 4
    two_min_sum = two_min * (n - 2) * 4 + two_min * (n - 1) * 4
    three_min_sum = three_min * 4

    print(one_min_sum + two_min_sum + three_min_sum)

# ========== 메모 ==========
# 맞추긴했당...ㅎㅎ
# 그냥 좀 코드짜기 더러운 문제였지 뭐 알고리즘이 필요한 문제는 아니었던 듯
# n=1 인 경우에 대해 빼먹었다가 추가로 더 작성해서 최종적으로 맞춤

# ========== 모범답안 ==========
# import sys

# if __name__ == '__main__':
#     N = int(input())
#     arr = list(map(int, sys.stdin.readline().split()))
#     ans = 0
#     min_lists = []
#     if N == 1:
#         arr.sort()
#         for i in range(5):
#             ans += arr[i]
#     else:
#         min_lists.append(min(arr[0], arr[5]))
#         min_lists.append(min(arr[1], arr[4]))
#         min_lists.append(min(arr[2], arr[3]))
#         min_lists.sort()

#         # 1, 2, 3 면의 주사위 최소값
#         min1 = min_lists[0]
#         min2 = min_lists[0] + min_lists[1]
#         min3 = sum(min_lists)

#         # 1, 2, 3 면의 주사위 개수
#         n1 = 4 * (N - 2) * (N - 1) + (N - 2) ** 2
#         n2 = 4 * (N - 1) + 4 * (N - 2)
#         n3 = 4

#         ans += min1 * n1
#         ans += min2 * n2
#         ans += min3 * n3
#     print(ans)

# 마주보는 면의 최솟값만을 구해서 그 최솟값을 조합해서 만들어내는 식인데 이거는... 천재아니고는 생각하기 힘들듯
