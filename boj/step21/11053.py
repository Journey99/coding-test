# 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
'''
dp[i] = i번째 원소를 마지막 원소로 가지는 ls의 길이
'''

for i in range(n):
    if i == 0:
        dp[i] = 1
    else:
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))