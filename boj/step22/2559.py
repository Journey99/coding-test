# 수열
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

## 누적합 계산해두기
prefix = [0]
for num in nums:
    prefix.append(prefix[-1] + num)


results = []
for i in range(k, n+1):
    results.append(prefix[i] - prefix[i-k])

print(max(results))