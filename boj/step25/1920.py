# 수 찾기 
import sys
input = sys.stdin.readline

def binary_search(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2 
        
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0

n = int(input())
nums = sorted(list(map(int, input().split())))
m = int(input())
targets = list(map(int, input().split()))

for t in targets:
    print(binary_search(nums, t))

