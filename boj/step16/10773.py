# 제로
import sys

k = int(input())
stack = []
for _ in range(k):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))