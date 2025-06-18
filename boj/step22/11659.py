# 구간 합 구하기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

## 누적합 계산해두기
prefix = [0]
for num in nums:
    prefix.append(prefix[-1] + num)

for _ in range(m):
    start, end = map(int, input().split())
    print(prefix[end] - prefix[start-1])
