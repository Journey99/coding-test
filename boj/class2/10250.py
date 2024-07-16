# 호텔 방배정

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    f = 0
    ho = 0

    if n % h == 0:
        f = h * 100
        ho = n // h
    else:
        f = ( n % h) * 100
        ho = n // h + 1

    print( f + ho)