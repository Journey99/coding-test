# 1로 만들기

'''
x % 3 == 0 ; x // 3
x % 2 == 0 ; x // 2
x - 1
위의 연산을 사용해서 숫자를 1로 만들기
연산을 사용하는 횟수의 최솟값

dp[i] = i를 1로 만들기 위한 최소 연산 횟수

'''

n = int(input())
cnt = 0
dp = [0] * (n+1)
dp[1] = 0

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 ==0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    
print(dp[n])