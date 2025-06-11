# 쉬운 계단 수

'''
45656 을 보면 모든 자리의 차이가 1이다. 이런 수를 계단 수
n이 주어질 때, 길이가 N인 계단 수가 총 몇개 있는지 구하기
'''

n = int(input())
dp = [[0] * 10 for _ in range(n+1)] # dp[i][j] ; 길이가 i이고 끝자리가 j인 계단수 의 개수
for j in range(1, 10):
    dp[1][j] = 1

if n == 1:
    print(sum(dp[n]))
else:
    for i in range(2, n+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(sum(dp[n]) % 1000000000)

