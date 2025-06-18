# 나머지 합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))


mod_count = [0] * m
prefix_sum = 0

for num in nums:
    prefix_sum += num
    mod_count[prefix_sum % m] += 1

ans = mod_count[0]
for i in range(m):
    ans += mod_count[i] * (mod_count[i] -1) // 2       


print(ans)