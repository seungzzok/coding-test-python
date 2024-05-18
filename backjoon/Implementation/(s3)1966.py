import sys

sys.stdin = open("input.txt", "r")
case_num = int(sys.stdin.readline())


def printing():
    n, m = map(int, sys.stdin.readline().strip().split())
    num_list = list(map(int, sys.stdin.readline().strip().split()))
    arr = list(enumerate(num_list))
    target = arr[m]

    cnt = 0

    while len(arr):
        max_v = max([i[1] for i in arr])

        if arr[0][1] == max_v:
            now = arr.pop(0)
            cnt += 1

            if now == target:
                print(cnt)
                break

        else:
            now = arr.pop(0)
            arr.append(now)


for i in range(case_num):
    printing()

# ========== 메모  ==========
# 하놔.. 그냥 문제 보이는대로 바로 풀면 되는거였는데 시간초과 뜰까봐 괜히 다르게 푼다고 겁나 오래걸림ㅠㅠ
# while 최대한 안쓰는게 좋은줄 알았는데 브루트포스로 전부 다 탐색해야하는것 밖에 없는걸 깨달음...
# 어떤 경우에 브루트포스를 하고 어떤 경우에 시간감소를 위해서 다른식으로 수정해야하는지가 헷갈림;;
