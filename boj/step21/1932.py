# 정수 삼각형
import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (i+1) for i in range(n)]
dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            dp[i][0] = dp[i-1][0] + triangle[i][0]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]


print(max(dp[n-1]))


