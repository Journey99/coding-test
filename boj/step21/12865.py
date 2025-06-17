# 평범한 배낭
'''
dp[i][w] ; i번째 물건까지 고려했을 때, 배낭 무게가 w일 때의 최대 가치
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
thing = []
for _ in range(n):
    thing.append(tuple(map(int, input().split())))

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = thing[i-1]
    for j in range(1, k+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else: # 물건을 넣을 수 있음
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
            # 현재 물건을 넣으면 w만큼 차지하므로 남은 공간은 j-w
            # 그 공간에 대해서 이전 단계에서 최대 가치가 dp[i-1][j-w]

print(dp[n][k])