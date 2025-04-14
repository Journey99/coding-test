# 팩토리얼
import math

n = int(input())
result = 1

if n == 0:
    print(1)
else:
    for i in range(n, 0, -1):
        result = result * i
    print(result)

## math 모듈 사용
print(math.factorial(n))