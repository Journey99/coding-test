import math
N, K = map(int, input().split())
a = math.factorial(N)
b = math.factorial(K)
c = math.factorial(N-K)

print(a // (b * c))

