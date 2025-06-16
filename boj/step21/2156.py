# 포도주 시식
'''
1. 잔을 선택하면 무조건 마셔야 하고, 마신 후 원래 위치에 놓기
2. 연속으로 놓여 잇는 3잔 모두 먹을 수 없음
'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * n # dp[i] ; i번째일 때 최대로 마실 수 있는 포도주의 양
graph = [int(input()) for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[i] = graph[0]
    elif i == 1:
        dp[i] = graph[0] + graph[1]
    elif i == 2:
        dp[i] = max(dp[1], graph[0] + graph[2], graph[1] + graph[2])
    else:
        dp[i] = max(dp[i-1], dp[i-3] + graph[i-1] + graph[i], dp[i-2] + graph[i])

print(max(dp))


'''
i번째 포도주를 마시지 않는 경우/ i번째만 마시는 경우 / i-1과 i번째 연속으로 마시는 경우
'''