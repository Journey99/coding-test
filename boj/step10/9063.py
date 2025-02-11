# 대지

n = int(input())
cor_x = []
cor_y = []
for _ in range(n):
    x, y = map(int, input().split())
    cor_x.append(x)
    cor_y.append(y)

if n == 1:
    print(0)
else:
    min_x, min_y = min(cor_x), min(cor_y)
    max_x, max_y = max(cor_x), max(cor_y)
    print((max_x - min_x) * (max_y - min_y))