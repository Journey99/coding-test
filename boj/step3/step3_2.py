import sys

# 15552
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)


# 11021
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a+b}')


# 11022
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')


# 2438
n = int(input())
for i in range(n):
    print('*' * (i+1))


# 2439
n = int(input())
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i)


# 10952
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print(a+b)


# 10951
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break


