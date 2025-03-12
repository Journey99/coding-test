# 수 정렬하기2
import sys

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()
for i in nums:
    print(i)