n = int(input())
num = []

for i in range(n):
    num.append(int(input()))

num = sorted(set(num))
for j in num:
    print(j)
