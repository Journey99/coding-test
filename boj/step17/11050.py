# 이항 계수 1

n, k = map(int, input().split())
u = 1
d = 1

for i in range(n, n-k, -1):
    u = u * i
for i in range(k, 0, -1):
    d = d * i
print(u//d)
