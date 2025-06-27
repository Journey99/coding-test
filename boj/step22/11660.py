# 구간 합 구하기 5
import sys
input= sys.stdin.readline

n, m = map(int, input().split())
matrix = []
prefix = [[0] * (n+1) for _ in range(n+1)]

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + matrix[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    p_sum = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
    print(p_sum)

'''
p[i][j] : (1,1) ~ (i,j) 까지 누적합

(x1, y1) ~ (x2, y2)
sum = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
'''