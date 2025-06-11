# 계단 오르기
import sys
input = sys.stdin.readline

n = int(input())
score = [int(input()) for _ in range(n)]
dp = [0] * n

if n == 1:
    print(score[0])
elif n == 2:
    print(score[0] + score[1])
else:
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0] + score[2], score[1] + score[2])
    
    for i in range(3, n):
        dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])
    
    print(dp[n-1])


'''
한번에 하나/두개
연속으로 세개 안됨
마지막 무조건 밟아야함

점프한 합이 6이어야함
1 / 2 / 2 / 1
1 / 1/ 2 / 2
1 / 2 / 1 / 2
2 /

dp[i] = i번째 계단까지 올랐을 때 얻을 수 있는 최대 점수

dp[i-2] + score[i] : 두 계단뛰어서
dp[i-3] + score[i-1] + score[i] : 한 계단 뛰어서(연속으로는 안되니까 i-3에서 두계단 오른 뒤 한계단)
dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])

dp[0] = 0
dp[1] = score[1]
dp[2] = max(score[1] + score[2] , score[2])

'''