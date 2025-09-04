# 두 용액
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

left, right = 0, n-1
result_1, result_2 = nums[left], nums[right]

min_value = abs(nums[left] + nums[right])

while left < right:
    s = nums[left] + nums[right]

    if abs(s) < min_value:
        min_value = abs(s)
        result_1, result_2 = nums[left], nums[right]

    if s < 0:  # 합이 음수 → 더 큰 수 필요
        left += 1
    else:      # 합이 양수 → 더 작은 수 필요
        right -= 1

print(result_1, result_2)
