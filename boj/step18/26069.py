# 붙임성 좋은 총총이
import sys

n = int(input())
result = set()

for _ in range(n):
    a, b = sys.stdin.readline().split()
    if a == 'ChongChong' or b == 'ChongChong':
        result.add(a)
        result.add(b)
    if a in result:
        result.add(b)
    elif b in result:
        result.add(a)
    
print(len(result))


