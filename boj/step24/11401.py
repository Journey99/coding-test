# 이항 계수 3
import sys
input = sys.stdin.readline

MOD = 1_000_000_007

n, k = map(int, input().split())

# 1. n!까지의 팩토리얼을 미리 계산
fact = [1] * (n + 1)
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % MOD  # 항상 MOD로 나눠주기

# 2. 모듈러 역원 함수: 페르마의 소정리 이용
def modinv(a):
    return pow(a, MOD - 2, MOD)
    # pow(a, b, c)는 (a^b) % c 를 빠르게 계산해주는 파이썬 내장함수

# 3. 이항계수 계산: n! * (k!)^-1 * ((n-k)!)^-1 mod MOD
result = fact[n]
result = result * modinv(fact[k]) % MOD
result = result * modinv(fact[n - k]) % MOD

print(result)
