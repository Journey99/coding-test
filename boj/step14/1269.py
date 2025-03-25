# 대칭 차집합
import sys

anum, bnum = map(int, input().split())
a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))

a_b = a - b
b_a = b - a
print(len(a_b.union(b_a)))
