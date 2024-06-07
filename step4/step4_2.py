# 10813
n, m = map(int, input().split())
basket = [i+1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
print(*basket)


# 5597
ls = [i for i in range(1,31)]
for _ in range(28):
    n = int(input())
    ls.remove(n)
print(min(ls), max(ls))


# 3052
ls = []
for _ in range(10):
    a = int(input())
    ls.append(a%42)
print(len(set(ls)))


# 10811
n, m = map(int, input().split())
ls = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    ls[i-1:j] = ls[i-1:j][::-1]
print(*ls)


# 1546
n = int(input())
ls = list(map(int, input().split()))
best = max(ls)
s = 0
for num in ls:
        s += (num / best) * 100
print(s/n)
