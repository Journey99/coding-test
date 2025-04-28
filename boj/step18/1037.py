# 약수
import sys

num = int(input())
divisors = list(map(int, sys.stdin.readline().split()))

divisors = sorted(divisors)
print(divisors[0] * divisors[-1])