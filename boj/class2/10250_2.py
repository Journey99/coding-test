# ACM 호텔

t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    f = 0
    ho = 0
    if n % h == 0:
        f = h * 100
        ho = n // h
    else:
        f = (n % h) * 100
        ho = 1 + n // h
    print(f + ho)


# n에 h를 나눴을때 나머지를 층 수로 한다
# n에 h를 나눴을때 몫에 1을 더한값을 호로 한다
# n에 h를 나눴을때 나누어 떨어질때 주의