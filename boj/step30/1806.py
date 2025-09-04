# 부분합
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
current_sum = nums[0]
min_len = float('inf')

while left < n and right < n:
    if current_sum >= s:
        min_len = min(min_len, right-left+1)
        current_sum -= nums[left]
        left += 1

    else:
        right += 1
        if right < n:
            current_sum += nums[right]
    
print(0 if min_len == float('inf') else min_len)
