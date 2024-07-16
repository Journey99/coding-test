# 1, 2, 3 더하기

t = int(input())
def plus(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return plus(n-1) + plus(n-2) + plus(n-3)


for _ in range(t):
   print(plus(int(input())))

