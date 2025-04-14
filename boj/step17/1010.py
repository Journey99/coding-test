# 다리 놓기
import sys
import math

t = int(input())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a = math.factorial(n)
    b = math.factorial(m)
    c = math.factorial((m-n))
    print(b//(a * c))

## 조합은 아래처럼 구할 수 있음
print(math.comb(m,n))