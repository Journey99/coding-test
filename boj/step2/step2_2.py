# 14681
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)


# 2884
h , m = map(int, input().split())

m -= 45

if m < 0:
    if h == 0:
        h = 23
        m += 60
    else:
        h -= 1
        m += 60

print(h, m)


# 2525
h , m = map(int, input().split())
t = int(input())

m += t

if m >= 60:
    plus_h = m // 60
    plus_m = m % 60

    h += plus_h
    m = plus_m

    if h >= 24:
        h -= 24

print(h, m)


# 2480
a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b:
    print(1000 + a * 100)
elif a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    m = max(a, b, c)
    print(m * 100)
