# 팩토리얼 0의 개수

from math import factorial

n = factorial(int(input()))
cnt = 0

while n % 10 == 0:
    n = n // 10
    cnt += 1

print(cnt)