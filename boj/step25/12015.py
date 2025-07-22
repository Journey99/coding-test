# 가장 긴 증가하는 부분 수열2
import sys
import bisect
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [] 
for num in a:
    idx = bisect.bisect_left(dp, num)

    if idx == len(dp):
        dp.append(num)
    else:
        dp[idx] = num
    
print(len(dp))