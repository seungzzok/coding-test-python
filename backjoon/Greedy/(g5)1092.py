import sys

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
cranes = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().strip().split()))
cranes.sort()
boxes.sort()

ans = 0

if boxes[-1] > cranes[-1]:
    ans = -1
else:
    while boxes:
        for c in cranes[::-1]:
            if boxes and c < boxes[0]:
                continue
            for b in boxes[::-1]:
                if b <= c:
                    boxes.remove(b)
                    break

        ans += 1


print(ans)

# ========== 메모 ==========
# 아ㅠㅠ 골드 확실히 어렵네..
# remove(item) 을 사용하면 그렇게 시간복잡도 크지 않으니까 그냥 사용하자
# 로직 거의 비슷했는데 remove를 사용해서 리스트 중간만 삭제하게 되면 시간복잡도가 증가할거란 생각에 사용안했음ㅠ
