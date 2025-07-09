# 곱셈

a, b, c = map(int, input().split())

def pow_mod(a, b, c):
    if b == 1:
        return a % c
    half = pow_mod(a, b//2, c)
    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c
    
print(pow_mod(a, b, c))
