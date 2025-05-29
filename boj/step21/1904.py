# 01타일

def tile(n):
    dp = [0] * (n+2)
    dp[1], dp[2] = 1, 2

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    
    return dp[n]

result = [0]
n = int(input())
print(tile(n))