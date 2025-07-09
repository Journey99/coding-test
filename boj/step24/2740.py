# 행렬곱셈
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = []
b = []

for _ in range(n):
    a.append(list(map(int, input().split())))

_, k = map(int,input().split())

for _ in range(m):
    b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(k):
        result = 0
        for l in range(m):
            result += a[i][l] * b[l][j]
        
        print(result, end=' ')
    
    print()