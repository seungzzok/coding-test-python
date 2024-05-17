import sys

sys.stdin = open("input.txt", "r")
case_num = int(sys.stdin.readline())


def fn():
    n = int(sys.stdin.readline())
    ranks = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    ranks.sort()

    cnt = 1
    min_rank = ranks[0][1]

    for idx, rank in enumerate(ranks):
        if idx == 0:
            continue

        if rank[1] < min_rank:
            cnt += 1
            min_rank = rank[1]
            if min_rank == 1:
                break

    print(cnt)


for case in range(case_num):
    fn()

# ========== 메모 ==========
# 하씌.... 개오랫동안 풀었네...;;
# for문 많이 돌리지 말고 비교할 때 최솟값이나 최댓값 하나만 비교하려고 하자
# 순서가 정해진 문제 같은 경우 정렬한 후 계산하기!!!