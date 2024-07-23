import sys

sys.stdin = open("input.txt", "r")
n, k = map(int, sys.stdin.readline().strip().split())
ans = 0

while bin(n).count("1") > k:
    n += 1
    ans += 1

print(ans)

# ========== 메모 ==========
# 이진법에서 1의 개수가 결국에는 k와 같아지면 되는 문제
# 1씩 더하면서 이진법의 1의 개수를 계속 비교하면 풀림
# 비트마스킹 처음 해봐서 다소 생소함ㅠㅠ
# 시간을 조금 더 줄이려고 하면 1의 idx를 가져와서 2의 idx승을 더해주면 더욱 빠르게 계산가능
