# 분수 합
def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n%m)


def lcm(n, m):
    return n * m // gcd(n, m)

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

denomi = lcm(b1, b2)
numer = denomi // b1 * a1 + denomi // b2 * a2

divisor = gcd(denomi, numer)

if divisor == 1:
    print(f"{numer} {denomi}")
else:
    print(f"{numer//divisor} {denomi//divisor}")
