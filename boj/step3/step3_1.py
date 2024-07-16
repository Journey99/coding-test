# 2739
n = int(input())
for i in range(1,10):
    print(f'{n} * {i} = {n*i}')


# 10950
t = int(input())
for i in range(t):
    a , b = map(int, input().split())
    print(a+b)


# 8393
n = int(input())
s = 0
for i in range(1, n+1):
    s += i
print(s)


# 25304
x = int(input())
n = int(input())
s = 0
for i in range(n):
    price, num = map(int, input().split())
    s += price * num

if s == x:
    print("Yes")
else:
    print("No")


# 25314
n = int(input())
x = n // 4
s = ''
for i in range(x):
    s += 'long '
s += 'int'
print(s)
