# 두 수의 합
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()
cnt = 0
left, right = 0, n-1

while left < right:
    s = nums[left] + nums[right]
    if s == x:
        cnt += 1
        left += 1
        right -= 1
    elif s < x:
        left += 1
    else:
        right -= 1


print(cnt)
