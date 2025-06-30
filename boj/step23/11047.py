# 동전 0
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0

for coin in coins[::-1]:
    if k >= coin:
        cnt += k // coin  # 현재 동전으로 최대한 거슬러줌
        k %= coin            # 남은 금액 갱신

print(cnt)